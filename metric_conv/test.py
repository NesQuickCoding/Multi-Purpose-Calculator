import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow

from views import MetricConvUI
import models
from controllers import MetricConvCtrl

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Metric Conversion")
        self.setFixedSize(400, 400)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        
        self.metricConvUI = MetricConvUI()
        self.generalLayout.addWidget(self.metricConvUI)

def main():
    baseconv = QApplication(sys.argv)
    view = TestWindow()
    view.show()
    MetricConvCtrl(view=view.metricConvUI.lengthView, model=models.length_conversion)
    MetricConvCtrl(view=view.metricConvUI.weightView, model=models.weight_conversion)
    MetricConvCtrl(view=view.metricConvUI.timeView, model=models.time_conversion)
    MetricConvCtrl(view=view.metricConvUI.digitalStorageView, model=models.digital_space_conversion)
    sys.exit(baseconv.exec())

if __name__ == '__main__':
    main()
