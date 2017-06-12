import sys
from PyQt5 import QtWidgets, QtGui

class Main(QtWidgets.QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setGeometry(100, 100, 300, 500)
        self.setWindowTitle('HelloW!!')
        self.setWindowIcon(QtGui.QIcon('Image.png'))
        self.show()

app = QtWidgets.QApplication(sys.argv)
gui = Main()
sys.exit(app.exec_())