#from Hexray forum
import idaapi
import sip
from PyQt4 import QtGui

class MyWidget(QtGui.QDialog):
    def __init__(self):
        super(MyWidget, self).__init__()

    def paintEvent(self, event):
        p = QtGui.QPainter()
        p.begin(self)
        p.fillRect(0, 0, self.width(), self.height(), QtGui.QColor(0, 0, 255))
        p.setPen(QtGui.QColor(255, 0, 0))
        p.setFont(QtGui.QFont("Monospace", 36))
        p.drawText(50, 50, "Can I haz paint?")
        p.end()


class MyForm(idaapi.PluginForm):
    def OnCreate(self, form):
        self.parent = self.FormToPyQtWidget(form)
        l = QtGui.QVBoxLayout()
        w = MyWidget()
        w.resize(self.parent.size())
        print w.size()
        l.addWidget(w)
        self.parent.setLayout(l)

    def OnClose(self, form):
        pass


f = MyForm()
f.Show("Hazpaint")