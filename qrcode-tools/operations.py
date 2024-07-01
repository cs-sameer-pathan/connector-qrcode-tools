""""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import logging
import zxingcpp
import cv2
import json
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
    return file_path


"""
Operations: connector's actions implementation
"""


def read_qr_code(config, params):
    """Reads QRcode from an image file"""
    codes = []
    if params.get('type') == 'File Path':
        file_id = str(params.get("file_iri"))
        file_path = file_id if file_id.startswith('/tmp') else '/tmp/{0}'.format(file_id)
    else:
        file_path = _get_file_path(params.get("file_iri"))
    img = cv2.imread(file_path)
    results = zxingcpp.read_barcodes(img)
    for result in results:
        codes.append({
            "text": f'{result.text}',
            "format": f'{result.format}',
            "content": f'{result.content_type}',
            "position": f'{result.position}'.replace('\u0000', '')
        })
    logger.debug(_print_json(codes))
    if len(codes) == 0:
        logger.warning("No QR Code found")
        return {'status': 'success', 'message': 'No QR Code found'}
    else:
        return codes
