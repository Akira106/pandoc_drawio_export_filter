import subprocess
import os
import sys
from typing import Tuple

import panflute as pf

from . import utils


logger = utils.get_logger()



def prepare(doc):
    pass


def action(elem, doc):
    """
    各ヘッダーにセクション番号を付与する。
    """
    if isinstance(elem, pf.Image):
        if elem.url.endswith(".drawio.svg"):
            src = elem.url
            dst = elem.url.replace(".drawio.svg", ".png")
            ret, emsg = _export_drawio(src, dst)
            if ret is False:
                logger.error(f"{emsg}")
                sys.exit(1)

            elem.url = dst


def finalize(doc):
    pass


def _export_drawio(src: str, dst: str) -> Tuple[bool, None | str]:
    """Drawioの画像をPNGにエクスポートします"""
    cwd = os.getcwd()
    cmd = f"docker run --rm -it --ipc=host -w /data -v {cwd}:/data rlespinasse/drawio-desktop-headless -x -f png --scale 2.5 -o {dst} {src}"

    out = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True).stdout

    # エラーチェック
    err_prefix = "Error: "
    for log in out.split("\n"):
        if log.startswith(err_prefix):
            return False, log[len(err_prefix):]

    return True, None
