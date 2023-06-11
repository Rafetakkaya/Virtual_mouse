import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from UI import Ui_MainWindow
import main
import head
class myApp(QtWidgets.QMainWindow):
    
    def __init__(self):

        super(myApp, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
      
        self.setWindowTitle("Virtual Mause")
        self.ui.pushButton.clicked.connect(self.headSet) 
        self.ui.pushButton_2.clicked.connect(self.mainSet)
        
        
      
    def mainSet(self):
        main.mouse()  
    def headSet(self):
        head.mouse()
   
    
def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())
app()


