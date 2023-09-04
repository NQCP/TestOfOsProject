import logging
import testofosproject._version


__version__ = testofosproject._version.__version__



logger = logging.getLogger(__name__)
logger.info(f'Imported testofosprojectversion: {__version__}')
