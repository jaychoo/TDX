import sys
import logging


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TDUtility:
    main_op_name = 'main'

    @staticmethod
    def clean_up():

        all_ops = parent().findChildren()

        for item in all_ops:
            if item.name == TDUtility.main_op_name:
                pass
            else:
                logger.info("Removing {}".format(item))
                op(item).destroy()


TDUtility.clean_up()
