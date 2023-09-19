#!/usr/bin/env python3

from copy import deepcopy

from .pyppeteer_builder import PyppeteerPDFBuilder
from typing import Dict, Any, Callable, Optional, List
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util.osutil import make_filename

import pkg_resources
__version__ = pkg_resources.get_distribution(__package__).version
__version_info__ = tuple(int(v) for v in __version__.split('.'))

DEFAULT_PDF_OPTIONS: Dict[str, Optional[bool|str|Dict[str,Optional[bool|str]]]] = {
    'printBackground': True,
    'format': 'A4',
    'margin': {
        'top': '20mm',
        'bottom': '20mm',
        'left': '10mm',
        'right': '10mm'
    }
}

DEFAULT_PYPPETEER_ARGS: List[str] = [
    '--allow-file-access-from-file',
    '--disable-web-security',
    '--no-sandbox',
]


def on_config_inited(app: Sphinx, config: Config):
    """ Change config on the fly """
    pdf_options:Dict[str, Any] = deepcopy(DEFAULT_PDF_OPTIONS)
    pdf_options.update(app.config.pyppeteer_pdf_options)
    app.config["pyppeteer_pdf_options"] = pdf_options
    app.set_html_assets_policy("always")


def setup(app: Sphinx) -> Dict[str, Any]:
    app.setup_extension('sphinx.builders.html')

    app.add_builder(PyppeteerPDFBuilder)
    _ = app.connect('config-inited', on_config_inited)

    theme_options_func:Callable[[Config], str] = lambda self:\
        self.html_theme_options
    app.add_config_value(
        'pyppeteer_theme_options',
        theme_options_func,
        'pyppeteer'
    )
    app.add_config_value(
        'pyppeteer_pdf_options',
        DEFAULT_PDF_OPTIONS,
        'pyppeteer'
    )
    app.add_config_value(
        'pyppeteer_args',
        DEFAULT_PYPPETEER_ARGS,
        'pyppeteer'
    )

    basename_func:Callable[[Config], str] = lambda self:\
        make_filename(self.project)
    app.add_config_value(
        'pyppeteer_basename',
        basename_func,
        'pyppeteer'
    )

    theme_func:Callable[[Config], str] = lambda self:\
        self.html_theme
    app.add_config_value(
        'pyppeteer_theme',
        theme_func,
        'pyppeteer'
    )

    title_func:Callable[[Config], str] = lambda self:\
        self.html_title
    app.add_config_value(
        'pyppeteer_title',
        title_func,
        'pyppeteer'
    )

    theme_path_func:Callable[[Config], str] = lambda self:\
        self.html_theme_path
    app.add_config_value(
        'pyppeteer_theme_path',
        theme_path_func,
        'pyppeteer'
    )

    short_title_func:Callable[[Config], str] = lambda self:\
        self.html_short_title
    app.add_config_value(
        'pyppeteer_short_title',
        short_title_func,
        'pyppeteer'
    )
    app.add_config_value(
        'pyppeteer_style',
        None,
        'pyppeteer',
        [str]
    )
    app.add_config_value(
        'pyppeteer_css_files',
        [],
        'pyppeteer'
    )
    app.add_config_value(
        'pyppeteer_show_copyright',
        True,
        'pyppeteer'
    )
    app.add_config_value(
        'pyppeteer_show_sphinx',
        True,
        'pyppeteer'
    )
    app.add_config_value(
        'pyppeteer_main_selector',
        '',
        'pyppeteer'
    )
    app.add_config_value(
        'pyppeteer_footer_selector',
        '',
        'pyppeteer'
    )
    app.add_config_value(
        'pyppeteer_header_selector',
        '',
        'pyppeteer'
    )
    app.add_config_value(
        'pyppeteer_baseurl',
        '#',
        'pyppeteer'
    )

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
