import sys

from PyQt5.QtWidgets import QApplication
from views import PrimeGenUi
from controllers import PrimeGenControl
import models

def main():
    primegen = QApplication(sys.argv)
    view = PrimeGenUi()
    view.show()
    control = PrimeGenControl(view=view, model=models)
    sys.exit(primegen.exec())

if __name__ == '__main__':
    main()
