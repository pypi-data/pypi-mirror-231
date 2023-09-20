import os
import logging
import asyncio

from ._load_dotenv import load_dotenv
from ..verbose import write_message

def _check_env_file(filename:str="./.env", verbose:bool=False):
    """
    :param str filename: Environment filename
    :param bool verbose:
    """

    try:
        last_modified_time = os.path.getmtime(filename)
        if last_modified_time != _check_env_file.last_modified_time:
            _check_env_file.last_modified_time = last_modified_time
            msg = "Le fichier {filename} a été modifié. "
            msg += "Mise à jour des variables d'environnement..."
            write_message(msg, verbose=verbose)
            load_dotenv(filename, verbose=verbose)
        #
    except FileNotFoundError:
        pass
    #
#

async def task_watch_dotenv_file(sleep_time:int=1, filename:str="./.env", **kwargs):
    """
    :param int sleep_time: Duration between 2 sync
    :param str filename: Environment filename
    """
    _check_env_file.last_modified_time = 0

    while True:
        _check_env_file(filename=filename, **kwargs)
        await asyncio.sleep(sleep_time)
    #
#
