import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def mandelbrot_point(c, iters=256):
    return 0


def process_request(data):
    xmin = data.get("xmin")
    ymin = data.get("ymin")
    xxmax = data.get("xmax")
    yxmax = data.get("ymax")
    size = data.get("size")

    return 1


def handler(event, context):
    logger.debug(f"{event=}")
    raw_request_body = event.get("body")
    logger.debug(f"{raw_request_body=}")
    request_body = json.loads(raw_request_body)

    result = process_request(request_body)

    body = {"request": request_body, "result": result}
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response
