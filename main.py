import json
import logging
from decimal import Decimal

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def mandelbrot_point(c, max_iters=256):
    z = 0
    n = 0

    while abs(z) <= 2 and n < max_iters:
        z = z * z + c
        n += 1

    return n


def process_request(data):
    xmin = Decimal(data.get("xmin"))
    ymin = Decimal(data.get("ymin"))
    xmax = Decimal(data.get("xmax"))
    ymax = Decimal(data.get("ymax"))
    size = int(data.get("size"))
    max_iters = int(data.get("max_iters"))

    c = complex(xmin, ymin)

    return mandelbrot_point(c, size)


def handler(event, context):
    logger.debug(f"{event=}")
    raw_request_body = event.get("body")
    logger.debug(f"{raw_request_body=}")
    request_body = json.loads(raw_request_body)

    result = process_request(request_body)

    body = {"request": request_body, "result": result}
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response
