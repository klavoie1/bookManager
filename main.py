import Widget as W
import sys

if __name__ == "__main__":

    app = W.QtWidgets.QApplication([])

    widget = W.Main_Widget()
    widget.setWindowTitle("Python Book Detailer")
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
