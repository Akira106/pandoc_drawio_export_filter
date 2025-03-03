import logging
import sys

import panflute as pf

# ロガーの名前
LOGGER_NAME = "drawio_export"


def set_logger(log_level):
    # フォーマット
    log_format = logging.Formatter("%(levelname)s: %(message)s")
    # 標準エラー出力(標準出力はpandocが使う)
    stderr_handler = logging.StreamHandler(stream=sys.stderr)
    stderr_handler.setLevel(log_level)
    stderr_handler.setFormatter(log_format)
    # 設定の適用
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(log_level)
    logger.addHandler(stderr_handler)


def get_logger():
    return logging.getLogger(LOGGER_NAME)
