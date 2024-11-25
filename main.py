import Widget as W
import sys
import PyQt5 as Qt

if __name__ == "__main__":

    app = W.QtWidgets.QApplication([])

    widget = W.Main_Widget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())

