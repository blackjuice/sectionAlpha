# PyQt
import pickle
from PyQt5.QtCore import (Qt, pyqtSlot)
from PyQt5.QtWidgets import (QDialog, QFileDialog, QGridLayout, 
                            QHBoxLayout, QLabel, QLineEdit, 
                            QMessageBox, QPushButton, QTextEdit,
                            QVBoxLayout, QWidget, QApplication, 
                            QMainWindow)
from PyQt5.QtGui import QIcon
# Custom
from lib.script001 import *

# Empty window
class OverwatchStats(QWidget):
    NavigationMode, AddingMode, EditingMode = range(3)

    def __init__(self):
        super().__init__()

        self.oldName = ''
        self.oldAddress = ''
        self.currentMode = self.NavigationMode

    # Status bar example
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, 
                        self.width, self.height)
        self.show()

class ImportOutside(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'show message on statusbar'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(10, 10, 200, 300)
    
        statusDate(self)
        self.show()

def create_button(self,i):
    button = QPushButton('PyQt5 button', self)
    button.setToolTip('This is an example button')
    button.move(100,i*50)
    button.clicked.connect(self.on_click)

class AddButton(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'add button'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(10, 10, 200, 300)

        for i in range(1,4):
            create_button(self,i)
    
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')


# Calling main when executed
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app             = QApplication(sys.argv)
    #overwatchStats = OverwatchStats() # empty window
    overwatchStats = ImportOutside() # show msg on statusbar
    #overwatchStats = AddButton()
    sys.exit(app.exec_())