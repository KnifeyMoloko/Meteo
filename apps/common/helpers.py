"""
Helper functions for common app tasks
Author: Maciej Cisowski
"""
import logging
import os
import requests
import pandas as pd

logger = logging.getLogger("meteo.common")


def get_env_vars(app_name="FLASK") -> dict:
    logger.debug("Getting environment variables")
    vars = os.environ
    logger.debug(f"Filtering for env vars starting with {app_name}")
    filtered = [x for x in list(vars.keys()) if x.startswith(app_name)]
    # return dict output for key, val pair for filtered keys
    return {y: vars[y] for y in filtered}


def get_file_at_url(url: str, timeout: int = 12) -> requests.Response:
    logger.debug(f"Trying to get file at {url} with timeout {timeout}")
    return requests.get(url=url, timeout=timeout)


def parse_csv_to_data_frame(csv_file):
    logger.debug("Attempting to decode the csv file with encoding ISO-8859-2")
    decoded = csv_file.decode("ISO-8859-2")
    logger.debug("Split up the decoded string")
    split_up = [x.split(",") for x in decoded.splitlines()]
    logger.debug("Creating pandas Data Frame from decoded csv")
    return pd.DataFrame(split_up)
