#storm shadow
#shows content of %AppData/local/temp

import idaapi
import sip

from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import (QApplication, QColumnView, QFileSystemModel,
                         QSplitter, QTreeView)
from PyQt4.QtCore import QDir, Qt

idahome = QDir.tempPath()


class MyWidget(QtGui.QDialog):
    def __init__(self):
        super(MyWidget, self).__init__()

    def paintEvent(self, event):
        self.splitter = QSplitter()
        model = QFileSystemModel()
        model.setRootPath(QDir.rootPath())
        # model.setRootPath(idahome)
        # using ida home instead
        views = []
        for ViewType in (QColumnView, QTreeView):
            view = ViewType(self.splitter)
            view.setModel(model)
            view.setRootIndex(model.index(idahome))
            view.setDragEnabled(True)
            view.setAcceptDrops(True)
            view.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        # splitter.show()
        # Create layout
        layout = QtGui.QVBoxLayout(self)
        # layout.addWidget(self.comboList)
        layout.addWidget(self.splitter)
        # layout.addWidget(splitter)




class MyTemptree(idaapi.PluginForm):
    def OnCreate(self, form):
        self.parent = self.FormToPyQtWidget(form)
        l = QtGui.QVBoxLayout()
        w = MyWidget()
        w.resize(self.parent.size())
        # print w.size()
        l.addWidget(w)
        self.parent.setLayout(l)

    def OnClose(self, form):
        pass


f = MyTemptree()
f.Show("Temp folder right now")