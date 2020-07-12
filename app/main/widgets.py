from PyQt5.QtCore import QAbstractTableModel, Qt


class TracksTableModel(QAbstractTableModel):

    def __init__(self, data, headers):
        QAbstractTableModel.__init__(self)
        self._data = data
        self.headers = headers
    
    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            valor = self._data[index.row()][index.column()]
            return valor
    
    def setData(self, index, value, role=Qt.EditRole):
        # if index.isValid():
        row = index.row()
        col = index.column()
        self._data[row][col] = value
        return True
        # self._data.iloc[row][col] = value
        #     self.dataChanged.emit(index, index, (Qt.DisplayRole, ))
        #     return True
        # return False

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self.headers)
