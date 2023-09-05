import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGridLayout, QLabel, QScrollArea, QDialog, QGraphicsBlurEffect, QPushButton, QMessageBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QScreen, QImage, QFont
from PyQt5.QtCore import Qt

from glob import glob
import numpy as np
from natsort import natsorted
import os
import random

MAIN_WIDTH = 1500
MAIN_HEIGHT = 800

# Class for input image and edit
class LEGOGeneratorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # [MAIN WINDOW]
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # [OPEN IMAGE LABEL]
        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 300, 200)

        self.initUI(central_widget)

        # [OPEN IMAGE BUTTON]
        self.openImgbutton = QPushButton('Open Image', self)
        self.openImgbutton.setGeometry(MAIN_WIDTH - 200, 50, 120, 30)
        self.openImgbutton.clicked.connect(self.showDialog)

        # Font adjusted
        font = QFont('Helvetica', 10) # Font type
        # font.setBold(True) # Font bold
        self.openImgbutton.setFont(font)

        # Maximize window
        # self.showMaximized()
    
    def initUI(self, central_widget):

        # Backgound color (dark blue)
        style = """
            QWidget {
                background-color: #2a2a2a;
            }
        """
        central_widget.setStyleSheet(style)

        self.setWindowTitle('LEGO Manual Generator by AImport')
        self.setGeometry(100, 100, MAIN_WIDTH, MAIN_HEIGHT) # x, y, width, height

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        print(fname)

        if fname[0]:
            pixmap = QPixmap(fname[0])
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(True)
            self.label.move(500, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Open LEGO generator window
    window = LEGOGeneratorWindow()
    window.show()
    sys.exit(app.exec_())