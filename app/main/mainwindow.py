
import shutil

from PyQt5.QtWidgets import QMainWindow, QFileSystemModel, QFileDialog
from PyQt5.QtCore import QDir, QSettings, Qt

from app.ui.mainwindow_Ui import Ui_MainWindow
from app.folders.dock import DockFolders

from .album_analyzer import AlbumAnalyzer
from .album_export import AlbumExport
from .widgets import TracksTableModel


# ─── MAINWINDOW CLASS ───────────────────────────────────────────────────────────

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, ctx, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.ctx = ctx
        self.cfg = QSettings("MusicMan", "Music1")
        #
        try:
            self.resize(self.cfg.value("win_size"))
            self.move(self.cfg.value("win_pos"))
        except Exception:
            pass
        self.btn_export.clicked.connect(self.onButtonExport)
        self.dock_folders = DockFolders(self)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_folders)
    
    def closeEvent(self, event):
        self.cfg.setValue("win_size", self.size())
        self.cfg.setValue("win_pos", self.pos())

    def loadAlbum(self, path):
        """ Receive absolute path of selected folder """
        self.clearAlbumFields()
        album = AlbumAnalyzer(path)
        if album.isAlbumFolder:
            self.current_album_path = path
            # add tracks model to table
            data, header = album.getData()
            self.tracksModel = TracksTableModel(data, header)
            self.tb_tracks.setModel(self.tracksModel)
            self.tb_tracks.resizeColumnsToContents()
            # add possibles albums and artists to combos
            self.cb_artist.addItems(album.artists)
            self.cb_album.addItems(album.albums)
            self.cb_genre.addItems(album.genres)
            index = self.cb_artist.findText(album.most_common(album.artist_possibles))
            self.cb_artist.setCurrentIndex(index)
            index2 = self.cb_album.findText(album.most_common(album.album_possibles))
            self.cb_album.setCurrentIndex(index2)
            index3 = self.cb_genre.findText(album.most_common(album.genre_possibles))
            self.cb_genre.setCurrentIndex(index3)

    def clearAlbumFields(self):
        self.cb_album.clear()
        self.cb_artist.update()
        self.cb_artist.clear()
        self.cb_artist.update()
        self.cb_genre.clear()
        model = TracksTableModel()
        self.tb_tracks.setModel(model)

    def onButtonExport(self):
        data = dict(
            artist=self.cb_artist.currentText(),
            album=self.cb_album.currentText(),
            genre=self.cb_genre.currentText(),
            tracks=self.tb_tracks.model()._data,
            output_folder=self.cfg.value("output_folder", defaultValue="/home/q/Music")
        )
        album = AlbumExport(data)
        if album.alreadyExists:
            self.statusbar.showMessage(self.tr("this album already exists"))
        else:
            album.export()
            shutil.rmtree(self.current_album_path)
            self.statusbar.showMessage(self.tr("Album exported"))
            self.clearAlbumFields()

# ────────────────────────────────────────────────────────────────────────────────
