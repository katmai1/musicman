from PyQt5.QtWidgets import QDockWidget, QFileSystemModel
from PyQt5.QtCore import QDir

from app.ui.dock_folders_Ui import Ui_dock_folders


# ─── DOCK FOLDERS ───────────────────────────────────────────────────────────────

class DockFolders(QDockWidget, Ui_dock_folders):

    def __init__(self, parent):
        QDockWidget.__init__(self, parent=parent)
        self.setupUi(self)
        self.mw = parent
        #
        self.ed_path.setText(self.mw.cfg.value("root_path", defaultValue=QDir.homePath()))
        self.setupDirModel()
        self.tree.clicked.connect(self.onDirClicked)
        # self.btn_selectdir.clicked.connect(self.onButtonSelectDir)
        self.ed_path.returnPressed.connect(self.setupDirModel)

    def setupDirModel(self):
        """ Show folders on tree view """
        path = self.ed_path.text()
        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(path)
        self.dirModel.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
        self.tree.setModel(self.dirModel)
        self.tree.setRootIndex(self.dirModel.index(path))
        self.tree.hideColumn(1)
        self.tree.hideColumn(2)
        self.tree.hideColumn(3)
        self.tree.resizeColumnToContents(0)

    def onDirClicked(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.mw.loadAlbum(path)

# ────────────────────────────────────────────────────────────────────────────────
