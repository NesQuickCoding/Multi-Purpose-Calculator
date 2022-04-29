import sys

from PyQt5.QtWidgets import QApplication
from view import PrimeGenUi
from controller import PrimeGenControl
import model

def main():
    primegen = QApplication(sys.argv)
    view = PrimeGenUi()
    view.show()
    control = PrimeGenControl(view=view, model=model)
    sys.exit(primegen.exec())

if __name__ == '__main__':
    main()
