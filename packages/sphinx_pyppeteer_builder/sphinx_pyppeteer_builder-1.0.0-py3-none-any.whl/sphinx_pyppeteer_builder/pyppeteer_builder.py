#!/usr/bin/env python3

import os
import asyncio
from typing import Set, Optional, Dict, Any

from typing_extensions import override

from sphinx.builders.singlehtml import SingleFileHTMLBuilder
from sphinx.util.display import progress_message
from sphinx.util.logging import getLogger, SphinxLoggerAdapter
from sphinx.util.osutil import os_path
from sphinx.config import Config
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.theming import Theme
from sphinx.locale import __

import pyppeteer
from .loghandler import init_ppsphinx_log


logger: SphinxLoggerAdapter = getLogger('pyppeteer*')


class PyppeteerPDFBuilder(SingleFileHTMLBuilder):
    name = 'pyppeteer'
    epilog = __('The PDF file has been saved in %(outdir)s.')
    embedded = True
    search = False

    def __init__(self, app: Sphinx, env: BuildEnvironment) -> None:
        self.config: Config
        self.theme: Theme
        self.globalcontext: Dict[str, Any]
        self.outdir: str
        super(PyppeteerPDFBuilder, self).__init__(app, env)

    def _get_translations_js(self) -> str:
        return ""

    @override
    def copy_translation_js(self) -> None:
        return

    @override
    def copy_stemmer_js(self) -> None:
        return

    @override
    def copy_html_favicon(self) -> None:
        return

    @override
    def get_theme_config(self) -> tuple[str, Dict[str, Any]]:
        return (
            self.config.pyppeteer_theme,
            self.config.pyppeteer_theme_options
        )

    @override
    def init_js_files(self) -> None:
        return

    @override
    def add_js_file(self, filename: str, **kwargs: str) -> None:
        return

    @override
    def prepare_writing(self, docnames: Set[str]) -> None:
        super(PyppeteerPDFBuilder, self).prepare_writing(docnames)
        if self.config.pyppeteer_style is not None:
            stylename = self.config.pyppeteer_style
        elif self.theme:
            stylename = self.theme.get_config('theme', 'stylesheet')
        else:
            stylename = 'default.css'

        self.globalcontext['use_opensearch'] = False
        self.globalcontext['docstitle'] = self.config.pyppeteer_title
        self.globalcontext['shorttitle'] = self.config.pyppeteer_short_title
        self.globalcontext['show_copyright'] = \
            self.config.pyppeteer_show_copyright
        self.globalcontext['show_sphinx'] = self.config.pyppeteer_show_sphinx
        self.globalcontext['style'] = stylename
        self.globalcontext['favicon'] = None

    @override
    def finish(self) -> None:
        super(PyppeteerPDFBuilder, self).finish()
        _ = progress_message('Starting conversion to PDF with Pyppeteer')
        infile:str = os.path.join(
            self.outdir,
            os_path(self.config.master_doc) + self.out_suffix
        )
        outfile:str = os.path.join(
            self.outdir,
            self.config.pyppeteer_basename + '.pdf'
        )

        url:str = 'file://' + infile
        pdf_options:Dict[str, Optional[bool|str|Dict[str,Optional[bool|str]]]] \
            = self.config.pyppeteer_pdf_options
        pdf_options['path'] = outfile
        init_ppsphinx_log()

        evloop = asyncio.get_event_loop()
        evloop.run_until_complete(
            self.generate_pdf(url, pdf_options)
        )

    async def generate_pdf(self, url: str, pdf_options: Dict[str, Optional[bool|str|Dict[str,Optional[bool|str]]]]) -> None:
        """
        Generate PDF

        Parameters
        ----------

        url:
            Url to the file

        pdf_options:
            Dict with options for the pdf coroutine
        """
        # Disable security to allow SVG use.
        browser = await pyppeteer.launch({
            'args': self.config.pyppeteer_args,
        })
        try:
            page = await browser.newPage()
            _ = await page.goto(url, {"waitUntil": ["networkidle2"]})
            _ = await page.pdf(pdf_options)
            await browser.close()
        finally:
            await browser.close()
