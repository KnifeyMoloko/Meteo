"""
Helper functions for common app tasks
Author: Maciej Cisowski
"""
import logging
import os
from pprint import pprint

logger = logging.getLogger("meteo.common")


def get_env_vars(app_name="FLASK") -> dict:
    logger.debug("Getting environment variables")
    vars = os.environ
    logger.debug(f"Filtering for env vars starting with {app_name}")
    filtered = [x for x in list(vars.keys()) if x.startswith(app_name)]
    # return dict output for key, val pair for filtered keys
    return {y: vars[y] for y in filtered}