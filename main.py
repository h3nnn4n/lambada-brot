import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, _context):
    logger.info(f"got {event=}")
    return {"message": "hi"}
