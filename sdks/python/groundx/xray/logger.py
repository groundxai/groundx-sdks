# coding: utf-8


import logging


TRACE_LEVEL_NUM = 5
logging.addLevelName(TRACE_LEVEL_NUM, "TRACE")

class CustomLogger(logging.Logger):
    def trace(self, message, *args, **kws):
        if self.isEnabledFor(TRACE_LEVEL_NUM):
            self._log(TRACE_LEVEL_NUM, message, args, **kws)

def setup_custom_logger(name) -> CustomLogger:
    logging.setLoggerClass(CustomLogger)
    logger = logging.getLogger(name)
    if not isinstance(logger, CustomLogger):
        raise TypeError("Logger is not an instance of CustomLogger")
    logging.basicConfig(
        level=logging.DEBUG,
        format="[groundx] - %(levelname)s - %(message)s",
    )

    return logger