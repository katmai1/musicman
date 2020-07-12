
from PyQt5.QtWidgets import QMainWindow

from app.ui.mainwindow_Ui import Ui_MainWindow


# ─── MAINWINDOW CLASS ───────────────────────────────────────────────────────────

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, ctx, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.ctx = ctx

# ────────────────────────────────────────────────────────────────────────────────
