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


def parse_csv_to_data_frame(csv_file: bytes, columns: list = None, index: str = None):
    logger.debug("Attempting to decode the csv file with encoding Windows-1250")
    decoded = csv_file.decode("Windows-1250")
    logger.debug("Splitting up the decoded string and inferring data types for record elements")
    split_up = [x.split(",") for x in decoded.splitlines()]
    corrected = []
    for rec in split_up:
        # Strip outer quotation marks
        rec = [r[1:-1] for r in rec]
        # Create new record with recast values
        new_rec = []
        for e in rec:
            # strip out the whitespace at the beginning
            if e.startswith(" "):
                e = e.strip(" ")
            # infer datatype and cast the string accordingly
            if e.isdigit():
                new_rec.append(int(e))
            elif e.isdecimal() and e.find(".") != -1:
                new_rec.append(float(e))
            else:
                new_rec.append((str(e)))
        corrected.append(new_rec)

    logger.debug("Creating pandas Data Frame from decoded csv")
    df = pd.DataFrame(corrected, columns=columns)
    logger.debug("Setting index for Data Frame")
    df.set_index([index])
    return df


# df = parse_csv_to_data_frame(get_file_at_url(
#     url="https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/wykaz_stacji.csv").content,
#     columns=["kod_stacji", "nazwa_stacji", "5_znakowy_kod_stacji"],
#     index="5_znakowy_kod_stacji")
# print(df.tail(10))
# print((df["kod_stacji"] == 252150270))
# print(df[df["kod_stacji"].isin([252150270])])
# print(list(df))
