from PyQt5 import QtCore, QtWidgets, QtGui
import Book
import random

class Main_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        book1 = Book.Book("Foundation", "Isaac Asimov", "1951", "Science Fiction", "320")

        label = QtWidgets.QLabel(self)
        label.setText(book1.show_title())

