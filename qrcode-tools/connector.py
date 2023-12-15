""" Copyright start
  Copyright (C) 2008 - 2023 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from connectors.core.connector import Connector
from connectors.core.connector import get_logger, ConnectorError
from . import operations

logger = get_logger('qrcode-tools')

def get_available_operations(operations, operation):
    '''returns the function object defined by operation str'''
    for func in filter(callable, operations.__dict__.values()):
        if operation in func.__qualname__:
            return func

class QrCodeTools(Connector):
    def execute(self, config, operation, params, **kwargs):
        try:
            params.update({'operation': operation})
            action = get_available_operations(operations, operation)
            return action(config, params)
        except Exception as Err:
            raise ConnectorError(Err)

    def check_health(self, config):
        try:
            import cv2, zxingcpp
        except Exception as Err:
            logger.error('Required import failed: [{0}]'.format(Err))
            raise ConnectorError(Err)
