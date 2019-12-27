"""
Main executable script for the Meteo download_lookup_table service.
Author: Maciej Cisowski
"""

# imports
from apps.common import get_env_vars
from apps.download_lookup_table.app import DownloadLookupTableApp
import logging.config, logging
import config

# logger config
logging.config.dictConfig(config.LOGGING)
logger = logging.getLogger(__name__)


def main():
    logger.debug("Running")
    DownloadLookupTableApp.run()
    return 0


if __name__ == "__main__":
    main()
