# -*- coding: utf-8 -*-

import os
import copy
import errno

from loguru import logger
from pydantic import validate_call

from ._const import WarnEnum


@validate_call
def create_dir(create_dir: str, warn_mode: WarnEnum = WarnEnum.DEBUG):
    """Create directory if `create_dir` doesn't exist.

    Args:
        create_dir (str, required): Create directory path.
        warn_mode  (str, optional): Warning message mode, for example: 'LOG', 'DEBUG', 'QUIET'. Defaults to "QUIET".
    """

    if not os.path.isdir(create_dir):
        try:
            _message = f"Creaing '{create_dir}' directory..."
            if warn_mode == WarnEnum.LOG:
                logger.info(_message)
            elif warn_mode == WarnEnum.DEBUG:
                logger.debug(_message)

            os.makedirs(create_dir)
        except OSError as err:
            if err.errno == errno.EEXIST:
                logger.debug(f"'{create_dir}' directory already exists!")
            else:
                logger.error(f"Failed to create '{create_dir}' directory!")
                raise

        _message = f"Successfully created '{create_dir}' directory."
        if warn_mode == WarnEnum.LOG:
            logger.success(_message)
        elif warn_mode == WarnEnum.DEBUG:
            logger.debug(_message)


@validate_call
def deep_merge(dict1: dict, dict2: dict) -> dict:
    """Return a new dictionary that's the result of a deep merge of two dictionaries.
    If there are conflicts, values from `dict2` will overwrite those in `dict1`.

    Args:
        dict1 (dict, required): The base dictionary that will be merged.
        dict2 (dict, required): The dictionary to merge into `dict1`.

    Returns:
        dict: The merged dictionary.
    """

    _merged = copy.deepcopy(dict1)
    for _key, _val in dict2.items():
        if (
            _key in _merged
            and isinstance(_merged[_key], dict)
            and isinstance(_val, dict)
        ):
            _merged[_key] = deep_merge(_merged[_key], _val)
        else:
            _merged[_key] = copy.deepcopy(_val)

    return _merged
