from PyQt5.QtCore import QAbstractTableModel, Qt


class TracksTableModel(QAbstractTableModel):

    def __init__(self, data=[], headers=[]):
        QAbstractTableModel.__init__(self)
        self._data = data
        self.headers = headers

    def flags(self, index):
        col_name = self.headers[index.column()]
        if col_name == "filename" or col_name == "absolutePath":
            return Qt.ItemIsEnabled
        return Qt.ItemIsEditable | Qt.ItemIsEnabled

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            valor = self._data[index.row()][index.column()]
            return valor

    def setData(self, index, value, role=Qt.EditRole):
        row = index.row()
        col = index.column()
        self._data[row][col] = value
        return True

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self.headers)
