import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.debug("call")
    response = {"statusCode": 200, "body": "hi"}
    return response
