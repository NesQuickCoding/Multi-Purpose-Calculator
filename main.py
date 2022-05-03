import sys
from PyQt5.QtWidgets import QApplication
from main_calc.views import MultiCalcUi
from main_calc.models import evaluateExpression
from main_calc.controllers import MultiCalcCtrl

__version__ = "0.1"
__author__ = "Python Calcuator"


def main():
    multicalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = MultiCalcUi()
    view.show()
    # Create instances of the model and the controller
    model = evaluateExpression
    controller = MultiCalcCtrl(model=model, view=view)
    # Execute calculator's main loop
    sys.exit(multicalc.exec_())

if __name__ == "__main__":
    main()
