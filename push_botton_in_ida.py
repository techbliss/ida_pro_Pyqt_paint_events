#starting easy
import idaapi

from PyQt4 import QtGui

class MyWidget(QtGui.QDialog):
    def __init__(self):
        super(MyWidget, self).__init__()

    def paintEvent(self, event):
        # Create layout
		self.button = QtGui.QPushButton('Test', self)
        self.button.clicked.connect(self.handleButton)
        layout2 = QtGui.QVBoxLayout(self)
        layout2.addWidget(self.button)

    def handleButton(self):
        print ('Hello World')
        layout2 = QtGui.QVBoxLayout()


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
f.Show("Pushbotton")