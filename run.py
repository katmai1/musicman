"""
PyQt5-Template

Usage:
  pyqt5_template [--debug]
  pyqt5_template -h | --help
  pyqt5_template -v | --version


Options:
  -h --help     Show this screen.
  -v --version  Show version.
  --debug       Execute in debug mode.
"""

__version__ = '0.1.0'

import docopt

from app.context import ContextoApp


# ─── MAIN ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    args = docopt.docopt(__doc__, version=__version__)
    appctx = ContextoApp(args)
    appctx.app.installTranslator(appctx.app_language)
    appctx.app.installTranslator(appctx.system_language)
    exit_code = appctx.run()
