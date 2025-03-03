#!/usr/bin/env python3

import logging

import panflute as pf

from . import utils
from .drawio_export_filter import action, prepare, finalize


utils.set_logger(logging.DEBUG)
#utils.set_logger(logging.WARNING)
logger = utils.get_logger()


def main():
    try:
        pf.run_filter(action, prepare=prepare, finalize=finalize)
    except Exception as e:
        logger.exception(e)


if __name__ == "__main__":
    main()
