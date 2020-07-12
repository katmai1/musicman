
from PyQt5.QtWidgets import QMainWindow, QFileSystemModel
from PyQt5.QtCore import QDir

from app.ui.mainwindow_Ui import Ui_MainWindow
from .album import AlbumAnalyzer
from .widgets import TracksTableModel


# ─── MAINWINDOW CLASS ───────────────────────────────────────────────────────────

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, ctx, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.ctx = ctx
        #
        self.setupDirModel()
        self.treedir.clicked.connect(self.onDirClicked)

    def setupDirModel(self):
        """ Show folders on tree view """
        path = QDir.homePath()
        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(path)
        self.dirModel.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)

        self.treedir.setModel(self.dirModel)
        self.treedir.setRootIndex(self.dirModel.index(path))
        self.treedir.setColumnWidth(0, 200)

    def onDirClicked(self, index):
        """ Receive absolute path of selected folder """
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        album = AlbumAnalyzer(path)
        # add tracks model to table
        data, header = album.getData()
        self.tracksModel = TracksTableModel(data, header)
        self.tb_tracks.setModel(self.tracksModel)
        self.tb_tracks.resizeColumnsToContents()
        # add possibles albums and artists to combos
        self.cb_artist.addItems(list(set(album.artist_possibles)))
        self.cb_album.addItems(list(set(album.album_possibles)))
        
        
# ────────────────────────────────────────────────────────────────────────────────
