import os
from signal import signal, SIGINT, SIG_DFL
from cached_property import cached_property

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QLibraryInfo, QTranslator

from .main.mainwindow import MainWindow


# ─── CONTEXTO APP ───────────────────────────────────────────────────────────────

class ContextoApp:

    language = "en_EN"

    def __init__(self, args):
        self.app = QApplication([])
        self.debug = args['--debug']
        signal(SIGINT, SIG_DFL)

    def run(self):
        self.window.show()
        return self.app.exec()

    def tr(self, context, message):
        return self.app.translate(context, message)

    # ─── PROPIEDADES ────────────────────────────────────────────────────────────────

    @cached_property
    def window(self):
        return MainWindow(self)

    @cached_property
    def app_language(self):
        qtrans = QTranslator()
        qtrans.load(self.language, os.path.join("app", "i18n"))
        return qtrans

    @cached_property
    def system_language(self):
        qtrans = QTranslator()
        lang = f"qtbase_{self.language}"
        qtrans.load(lang, QLibraryInfo.location(QLibraryInfo.TranslationsPath))
        return qtrans

# ────────────────────────────────────────────────────────────────────────────────
