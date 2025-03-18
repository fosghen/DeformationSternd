# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QVBoxLayout, QWidget
import pyqtgraph as pg
import numpy as np

class StringAxis(pg.AxisItem):
    """Кастомная ось X для отображения строк"""
    def __init__(self, labels=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.labels = labels or {}

    def tickStrings(self, values, scale, spacing):
        return [self.labels.get(int(v), "") for v in values]

class PyQtGraphWidget(QWidget):
    def __init__(self, ylabel="", ylabel_units="", parent=None):
        super().__init__(parent)

        self.categories = ["A", "B", "C", "D", "E", "F", "G"]
        self.x_vals = np.arange(len(self.categories))  # Числовые индексы
        self.y_vals = np.random.rand(len(self.categories))

        self.axis_x = StringAxis(labels={i: label for i, label in enumerate(self.categories)}, orientation="bottom")
        self.plot_widget = pg.PlotWidget(axisItems={"bottom": self.axis_x})

        layout = QVBoxLayout()
        layout.addWidget(self.plot_widget)
        self.setLayout(layout)

        self.curve = self.plot_widget.plot(self.x_vals, self.y_vals, pen=pg.mkPen("black"))

        self.plot_widget.setBackground("white")
        self.plot_widget.setLabel("left", ylabel, units=ylabel_units)
        self.plot_widget.getPlotItem().getAxis("bottom").setPen(pg.mkPen("black"))
        self.plot_widget.getPlotItem().getAxis("left").setTextPen("black")
        self.plot_widget.getPlotItem().getViewBox().setBorder(pg.mkPen("black"))
        self.plot_widget.getPlotItem().showGrid(x=True, y=True, alpha=0.3)

    def update(self, new_categories, new_y):
            """Обновление данных графика"""

            self.axis_x.labels = {i: label for i, label in enumerate(new_categories)}
            self.axis_x.update()

            self.curve.setData(np.arange(len(new_categories)), new_y)
