import sys
from PyQt5 import QtWidgets, QtGui
 
def main(): 
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_())
 
class MyWindow(QtWidgets.QWidget): 
    def __init__(self):
        super(MyWindow, self).__init__()
 
        # create objects
        label = QtWidgets.QLabel(self.tr("Enter command and press Return"))
        self.le = QtWidgets.QLineEdit()
        self.te = QtWidgets.QTextEdit()

        # layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.le)
        layout.addWidget(self.te)
        self.setLayout(layout) 

        # create connection
        #self.connect(self.le, SIGNAL("returnPressed(void)"),
        #             self.run_command)
        self.lineedit.returnPressed.connect(self.updateUi)

    def run_command(self):
        cmd = str(self.le.text())
        stdouterr = os.popen4(cmd)[1].read()
        self.te.setText(stdouterr)
  
if __name__ == "__main__": 
    main()

