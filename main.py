import json
import logging
from decimal import Decimal

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


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

    dx = (xmax - xmin) / size
    dy = (ymax - ymin) / size

    data = []
    for ix in range(size):
        for iy in range(size):
            x = xmin + dx * ix
            y = ymin + dy * iy
            c = complex(x, y)
            data.append(mandelbrot_point(c, max_iters))

    return data


def handler(event, context):
    logger.debug(f"{event=}")
    raw_request_body = event.get("body")
    logger.debug(f"{raw_request_body=}")
    request_body = json.loads(raw_request_body)

    result = process_request(request_body)

    body = {"request": request_body, "result": result}
    logger.debug(f"returning {body=}")
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response
