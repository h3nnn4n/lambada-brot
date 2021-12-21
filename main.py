import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.debug(f"{event=}")
    raw_request_body = event.get("body")
    logger.debuginfo(f"{raw_request_body=}")
    request_body = json.loads(raw_request_body)

    body = {"event": request_body}
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response
