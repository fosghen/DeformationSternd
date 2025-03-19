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
        self.y_vals1 = np.random.rand(len(self.categories))
        self.y_vals2 = np.random.rand(len(self.categories))

        # Кастомная ось X для отображения строк
        self.axis_x = StringAxis(labels={i: label for i, label in enumerate(self.categories)}, orientation="bottom")
        self.plot_widget = pg.PlotWidget(axisItems={"bottom": self.axis_x})

        self.plot_item = self.plot_widget.getPlotItem()
        self.right_vb = pg.ViewBox()
        self.plot_item.scene().addItem(self.right_vb)
        self.plot_item.getAxis('right').linkToView(self.right_vb)
        self.plot_item.vb.sigResized.connect(self.update_views)

        # Добавляем кривые
        self.curve2 = self.plot_item.plot(self.x_vals, self.y_vals2 + 1, pen='red', name="Сила (Н)")
        self.right_vb.addItem(self.curve2)
        self.curve1 = self.plot_item.plot(self.x_vals, self.y_vals1, pen="blue", name="Деформация (με)")

        self.plot_widget.setBackground("white")  # Белый фон
        self.plot_item.showGrid(x=True, y=True, alpha=0.3)  # Полупрозрачная сетка
        self.plot_item.getAxis("bottom").setPen(pg.mkPen("black"))  # Ось X
        self.plot_item.getAxis("left").setPen(pg.mkPen("black"))  # Ось Y
        self.plot_item.getAxis("bottom").setTextPen("black")  # Подписи X
        self.plot_item.getAxis("left").setTextPen("blue")  # Подписи Y
        self.plot_item.getAxis("right").setTextPen("red")  # Подписи Y
        # self.plot_item.getViewBox().setBorder(pg.mkPen("black"))  # Чёрная рамка

        # Настройка подписей осей
        self.plot_item.setLabel('left', 'Деформация (με)')
        self.plot_item.setLabel('right', 'Right Axis')
        self.plot_item.setLabel('bottom', 'Время', pen="black")

        self.plot_item.getAxis('left').setPen('blue')
        self.plot_item.getAxis('right').setPen('red')

        # Синхронизация по оси X
        self.plot_item.vb.sigXRangeChanged.connect(self.sync_x_range)

        # Компоновка
        layout = QVBoxLayout()
        layout.addWidget(self.plot_widget)
        self.setLayout(layout)
        self.plot_item.vb.sigRangeChanged.connect(self.on_range_changed)

    def on_range_changed(self):
        if self.plot_item.vb.autoRangeEnabled()[1]:
            self.plot_item.vb.sigRangeChanged.disconnect(self.on_range_changed)
            self.set_y_range()
            self.plot_item.vb.sigRangeChanged.connect(self.on_range_changed)

    def update_views(self):
        """Обновление геометрии правого ViewBox"""
        self.right_vb.setGeometry(self.plot_item.vb.sceneBoundingRect())
        self.right_vb.linkedViewChanged(self.plot_item.vb, self.right_vb.XAxis)

    def sync_x_range(self):
        """Синхронизация по оси X"""
        self.right_vb.setXRange(*self.plot_item.vb.viewRange()[0], padding=0)

    def set_y_range(self):
        """Устанавливаем диапазон по Y для левого графика"""
        y_min = min(self.y_vals1)  # Минимальное значение по Y
        y_max = max(self.y_vals1)  # Максимальное значение по Y
        padding = (y_max - y_min) * 0.1  # Добавляем 10% от диапазона для отступов
        self.plot_item.vb.setYRange(y_min - padding, y_max + padding)

    def update(self, new_categories, new_y1, new_y2):
        """Обновление данных графика"""
        self.y_vals1 = new_y1
        self.y_vals2 = new_y2

        self.axis_x.labels = {i: label for i, label in enumerate(new_categories)}
        self.axis_x.update()

        self.curve1.setData(np.arange(len(new_categories)), new_y1)
        self.curve2.setData(np.arange(len(new_categories)), new_y2)

        # Обновляем диапазон по Y для левого графика
        # self.set_y_range()
