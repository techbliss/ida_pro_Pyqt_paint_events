#strom shadow
#drag new window out of ide and scrool and watch output window
#add your own function to emited signal
import idaapi
import sip
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QDir, pyqtSignal, pyqtSlot, QObject

idahome = idaapi.idadir("plugins")

class MyWidget(QtGui.QDialog):
    itemChanged = pyqtSignal()
    def __init__(self):
        super(MyWidget, self).__init__()

    def paintEvent(self, event):
        # Create layout
        d = QDir(idahome)
        files = d.entryList(QDir.Files)
        self.filer = files

        self.comboList = QtGui.QComboBox(self)
        self.comboList.addItems(files)
        self.comboList.setCurrentIndex(-1)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.comboList)
        self.comboList.activated[str].connect(self.pass_Net_Adap)

    def pass_Net_Adap(self, item):
        if self.comboList.currentText != self.comboList.currentIndex():
            self.comboList.currentText = item
            self.itemChanged.emit()

            print str(self.comboList.currentText)



class MyCombo(idaapi.PluginForm):
    def OnCreate(self, form):
        self.parent = self.FormToPyQtWidget(form)
        l = QtGui.QHBoxLayout()
        w = MyWidget()
        w.resize(self.parent.size())

        l.addWidget(w)
        self.parent.setLayout(l)

    def OnClose(self, form):
        pass


f = MyCombo()
f.Show("Files Combo box")