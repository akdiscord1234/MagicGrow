#import statements
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'MagicGrow'
        self.setWindowIcon(QIcon('/New/Images/MagicGrow_Icon.png'))
        self.left = 0
        self.top = 0
        self.width = 700
        self.height = 500
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        QApplication.setStyle(QStyleFactory.create('modif')) #Sets style, can use the following- [Windows, motif, cde, plastique, CleanLooks, ]

        self.tab_widget = TabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.show()

class TabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        #Initialize Tab Screen
        self.tabs = QTabWidget()
        self.HomeTab = QWidget()
        self.GraphTab = QWidget()
        self.tabs.resize(500, 500)

        #Add Tabs
        self.tabs.addTab(self.HomeTab, "Home")
        self.tabs.addTab(self.GraphTab, "Graphs/Charts")

        # Create Home Tab
        self.HomeTab.layout = QVBoxLayout(self)

        #EXAMPLE LABEL CODE-
        #self.l = QLabel()
        #self.l.setText("aa")
        #self.HomeTab.layout.addWidget(self.l)

        self.HomeTab.setLayout(self.HomeTab.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        # Home Temperature Frame

        #Init Setup
        TempFrame = QFrame(self.HomeTab)
        TempFrame.setFrameShape(QFrame.StyledPanel)
        TempFrame.setGeometry(20, 20, 360, 260)
        TempFrame.setStyleSheet("background-color: #f0f0f0;")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
