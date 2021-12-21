import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info(f"got {event=}")
    logger.info(f"got {context=}")
    return "message"
