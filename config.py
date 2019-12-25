"""
Logger configuration dict for the Meteo apps
Author: Maciej Cisowski
"""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {
            "format": '%(asctime)s::%(levelname)s::%(message)s'
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "simple",
            "maxBytes": 2048,
            "backupCount": 3,
            "filename": "./logs/download_lookup_table.log"
        }
    },
    "loggers": {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
}
