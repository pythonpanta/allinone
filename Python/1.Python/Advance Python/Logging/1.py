'''
A Python logging configuration consists of four parts:

Loggers
Handlers
Filters
Formatters


'''



# from logging import *
# basicConfig(filename='logfile.log')
# logger=getLogger('')
# logger.debug('this is debug')
# logger.warning('this is warning')
# logger.error('this is error')
# logger.critical('this is critical')

import logging
logger = logging.getLogger('django')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'timestamp': {
            'format': '{asctime} {levelname} {message} {lineno} ',
            'style': '{',

        },

    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'timestamp'
        },


    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },

    },
}

try:
    n1=input('enter number')
    n2=int(input('enter number'))
    print('sum is ',n1+n2)
except  Exception as e:
    logger.error(str(e), exc_info=True)