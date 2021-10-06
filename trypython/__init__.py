"""
初期処理を実施します.
"""
from typing import Dict, Callable

from trypython import extlib


def make_mappings() -> Dict[str, Callable[[], None]]:
    """サンプル名と実行する関数のマッピングを生成します"""
    # noinspection PyDictCreation
    m = {}

    extlib.regist_modules(m)

    return m


mappings = make_mappings()
