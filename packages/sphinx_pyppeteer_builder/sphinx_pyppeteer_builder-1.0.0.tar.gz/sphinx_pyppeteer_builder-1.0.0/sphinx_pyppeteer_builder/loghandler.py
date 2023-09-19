#!/usr/bin/env python3

import sys
from logging import StreamHandler, Formatter, LogRecord, DEBUG

from typing import TYPE_CHECKING, Optional, TextIO
from typing_extensions import override

from sphinx.util.logging import getLogger, SphinxLoggerAdapter

logger: SphinxLoggerAdapter = getLogger('pyppeteer')

if TYPE_CHECKING:
    _StreamHandler = StreamHandler[TextIO]
else:
    _StreamHandler = StreamHandler

ppsphinx_log_inited = False


def init_ppsphinx_log() -> None:
    """
    Initialize logging for Pyppeteer.
    """
    if ppsphinx_log_inited:
        return

    formatter = Formatter('%(message)s')
    pphandler = SphinxPyppeteerHandler()
    pphandler.setLevel(DEBUG)
    pphandler.setFormatter(formatter)
    logger_names = (
        'pyppeteer',
        'pyppeteer.browser',
        'pyppeteer.chromium_downloader',
        'pyppeteer.command',
        'pyppeteer.connection',
        'pyppeteer.coverage',
        'pyppeteer.element_handle',
        'pyppeteer.execution_context',
        'pyppeteer.frame_manager',
        'pyppeteer.helper',
        'pyppeteer.launcher',
        'pyppeteer.navigator_watcher',
        'pyppeteer.network_manager',
        'pyppeteer.page',
        'pyppeteer.worker',
    )
    for logger_name in logger_names:
        pplogger = getLogger(logger_name)
        pplogger.logger.addHandler(pphandler)


class SphinxPyppeteerHandler(_StreamHandler):
    """
    Resend Pyppeteer logging to Sphinx output.
    """
    def __init__(self, stream: Optional[TextIO]=None) -> None:
        super(SphinxPyppeteerHandler, self).__init__(stream or sys.stderr)

    @override
    def emit(self, record: LogRecord) -> None:
        logger.handle(record)
