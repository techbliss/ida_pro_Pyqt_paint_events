#starting easy
import idaapi
import sip
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import QDir, QSize
from PyQt4.QtGui import QDockWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class MyWidget(QtGui.QDialog):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setupUi()


    def setupUi(self):
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(1203, 1200)
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 711, 491))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.tabWidget = QtGui.QTabWidget(self.widget)
        self.tabWidget.setGeometry(QtCore.QRect(0, -1, 711, 501))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2", None))


class MyForm(idaapi.PluginForm):
    def OnCreate(self, form):
        self.parent = self.FormToPyQtWidget(form)
        l = QtGui.QHBoxLayout()
        w = MyWidget()
        w.resize(self.parent.size())
        print w.size()
        l.addWidget(w)
        self.parent.setLayout(l)

    def OnClose(self, form):
        pass


f = MyForm()
f.Show("Tabwindow")