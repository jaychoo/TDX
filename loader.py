import sys
import json
import logging


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TDLoader:
    def __init__(self, config='config.json'):
        try:
            with open(config, 'rb') as f:
                data = json.load(f)
                self.config = data
        except Exception as e:
            logger.exception(e)

    def __getattribute__(self, name):
        try:
            val = self.config[name]
        except KeyError:
            return super(TDLoader, self).__getattribute__(name)

        
