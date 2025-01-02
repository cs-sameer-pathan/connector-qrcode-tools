""""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

import logging
import zxingcpp
import cv2
import json, io, os
import zipfile
from PIL import Image
from pdf2image import convert_from_path, pdfinfo_from_path
from connectors.core.connector import get_logger, ConnectorError
from integrations.crudhub import make_request
from connectors.cyops_utilities.builtins import download_file_from_cyops

logger = get_logger('qrcode-tools')
logger.setLevel(logging.DEBUG)

"""
Utilities: support functions
"""


def _print_json(json_object):
    return json.dumps(json_object, indent=4)


def _get_file_path(file_id):
    iri_type = 'attachment'
    file_name = None
    if not file_id.startswith('/api/3/'):
        file_id = '/api/3/attachments/' + file_id
    elif file_id.startswith('/api/3/files'):
        iri_type = 'file'

    if iri_type == 'attachment':
        attachment_data = make_request(file_id, 'GET')
        file_iri = attachment_data['file']['@id']
        file_name = attachment_data['file']['filename']
    else:
        file_iri = file_id

    res = download_file_from_cyops(file_iri)
    if not file_name:
        file_name = res['filename']
    logger.info("res: {}".format(res))
    file_path = "{0}/{1}".format('/tmp', res['cyops_file_path'])
    return file_path, file_name


"""
Operations: connector's actions implementation
"""


def read_qr_code(config, params):
    """Reads QRcode from an image, PDF or DOCX file or attachment"""
    if params.get('type') == 'File Path':
        file_id = str(params.get("file_iri"))
        file_path = file_id if file_id.startswith('/tmp') else '/tmp/{0}'.format(file_id)
        file_name = os.path.basename(file_path)
    else:
        file_path, file_name = _get_file_path(params.get("file_iri"))

    if not os.path.exists(file_path):
        raise ConnectorError("File {0} does not exists.".format(file_path))
    results = []
    if file_name.lower().endswith('.pdf') or get_file_type(file_path) == 'PDF':
        pdf_info = pdfinfo_from_path(file_path)
        total_pages = pdf_info.get("Pages")
        for i in range(0, total_pages+1, 5):
            pages = convert_from_path(file_path, dpi=200, first_page=i, last_page=min(i+4, pdf_info.get("Pages")))
            for page_num, image in enumerate(pages):
                results.extend(zxingcpp.read_barcodes(image))
    elif file_name.lower().endswith('.docx') or get_file_type(file_path) == 'DOCX':
        zipf = zipfile.ZipFile(file_path)
        filelist = zipf.namelist()
        for f_name in filelist:
            _, extension = os.path.splitext(f_name)
            if extension in [".jpg", ".jpeg", ".png", ".bmp"]:
                image_bytes = zipf.read(f_name)
                image = Image.open(io.BytesIO(image_bytes))
                results.extend(zxingcpp.read_barcodes(image))
        zipf.close()
    else:
        img = cv2.imread(file_path)
        if img is not None:
            results = zxingcpp.read_barcodes(img)
        else:
            logger.warning(f"Failed to load image from {file_path}. Please check the file path.")
            results = []
    codes = []
    for result in results:
        codes.append({
            "text": f'{result.text}',
            "format": f'{result.format}',
            "content": f'{result.content_type}',
            "position": f'{result.position}'.replace('\u0000', '')
        })
    if len(codes) == 0:
        logger.warning("No QR Code found")
        return {'status': 'success', 'message': 'No QR Code found'}
    else:
        return codes


def get_file_type(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_header = file.read(4)
            if file_header == b'%PDF':
                return 'PDF'
            elif file_header == b'PK\x03\x04':
                return 'DOCX'
        return 'Other'
    except Exception as e:
        logger.exception("Error occurred while getting file extension: {0}".format(e))
