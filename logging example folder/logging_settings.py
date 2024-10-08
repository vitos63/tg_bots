import logging
import sys
from logging_filters import ErrorLogFilter, DebugWarningFilter, CriticalLogFilter

logging_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_1': {
            'format': '[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_2': {
            'format': '#%(levelname)-8s [%(asctime)s] - %(filename)s:%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_3': {
            'format': '#%(levelname)-8s [%(asctime)s] - %(message)s'
        }
    },
    'filters': {
        'critical_filter': {
            '()': CriticalLogFilter
        },
        'debug_filter': {
            '()': DebugWarningFilter
        },
        'error_filter': {
            '()': ErrorLogFilter
        }
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },

        'error_file': {
            'class': 'logging.FileHandler',
            'filename': 'error.log',
            'mode': 'w',
            'level': 'DEBUG',
            'formatter': 'formatter_1',
            'filters': ['error_filter']
        },

        'stdout_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_2',
            'filters': ['debug_filter'],
            'stream': sys.stdout
        },

        'stderr_handler': {
            'class': 'logging.StreamHandler'
        },

        'critical_handler': {
            'class': 'logging.FileHandler',
            'filename': 'critical.log',
            'mode': 'w',
            'formatter': 'formatter_3',
            'filters': ['critical_filter']
        }
    },

    'loggers': {
        'module_1': {
            'level': 'DEBUG',
            'handlers': ['error_file']
        },

        'module_2': {
            'handlers': ['stdout_handler']
        },

        'module_3': {
            'handlers': ['critical_handler', 'stderr_handler']
        },

        'root': {
            'formatter': 'default',
            'handlers': ['default']
        }


    }
}
