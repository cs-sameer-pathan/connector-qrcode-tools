# Edit the config_and_params.json file and add the required parameter values.
# Add any specific assertions in each test case, based on the expected response.
# Add logic for validating conditional_output_schema.

"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

import os
import pytest
from pprint import pformat
from testframework.conftest import initial_setup, info_json, params_json, validate_params, connector_id, connector_details,\
    valid_configuration, invalid_configuration, valid_configuration_with_token, conn_cleanup
from testframework.helpers.test_helpers import run_health_check_success, run_invalid_config_test, run_success_test,\
    run_output_schema_validation, run_invalid_param_test, set_report_metadata, create_attachment, delete_attachment
from testframework.helpers.test_constants import VALID_CONFIG_TITLE, VALID_INPUT_TITLE, INVALID_PARAM_TITLE,\
    SCHEMA_VALIDATION_TITLE, STATUS_MISMATCH_ERROR


@pytest.mark.check_health
@pytest.mark.success
def test_check_health_success(valid_configuration, connector_details):
    set_report_metadata(connector_details, "Health Check", VALID_CONFIG_TITLE)
    result = run_health_check_success(valid_configuration, connector_details)
    assert result.get('status', '').lower() == 'available',\
        STATUS_MISMATCH_ERROR.format(expected='available', result=pformat(result))
    

@pytest.mark.read_qr_code
@pytest.mark.success
def test_read_qr_code_success(cache, valid_configuration_with_token, connector_details, params_json, request):
    set_report_metadata(connector_details, "Read QR Code", VALID_INPUT_TITLE)
    test_dir = os.path.dirname(request.fspath)
    resources_dir = os.path.join(test_dir, 'resources')
    attachment = create_attachment(os.path.join(resources_dir, 'qrcode.png'))
    file_iri = attachment.get("@id")
    params = params_json['read_qr_code']
    for param in params:
        if param.get("type") == "IRI":
            param.update({"file_iri": file_iri})
    for result in run_success_test(cache, connector_details, operation_name='read_qr_code',
                                   action_params=params):
        assert result.get('status') == "Success",\
            STATUS_MISMATCH_ERROR.format(expected='Success', result=pformat(result))
        assert result.get('data')[0].get('text') == "5012345678900", "Data Missmatch"
    delete_attachment(attachment)


@pytest.mark.read_qr_code
@pytest.mark.schema_validation
def test_validate_read_qr_code_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Read QR Code", SCHEMA_VALIDATION_TITLE)
    run_output_schema_validation(cache, 'read_qr_code', info_json, params_json['read_qr_code'])
    

@pytest.mark.read_qr_code
@pytest.mark.invalid_input
def test_read_qr_code_invalid_file_iri(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Read QR Code", INVALID_PARAM_TITLE.format(param='File IRI/Attachment IRI'))
    result = run_invalid_param_test(connector_details, operation_name='read_qr_code', param_name='file_iri',
                                    param_type='text', action_params=params_json['read_qr_code'])
    assert result.get('status') == "failed",\
        STATUS_MISMATCH_ERROR.format(expected='failed', result=pformat(result))
    
