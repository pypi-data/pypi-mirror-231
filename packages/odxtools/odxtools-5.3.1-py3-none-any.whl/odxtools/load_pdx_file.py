# SPDX-License-Identifier: MIT
from zipfile import ZipFile

from .database import Database
from .globals import logger


def load_pdx_file(pdx_file: str):
    u = ZipFile(pdx_file)
    container = Database(pdx_zip=u)
    logger.info(f"--- --- --- Done with parsing --- --- ---")
    return container
