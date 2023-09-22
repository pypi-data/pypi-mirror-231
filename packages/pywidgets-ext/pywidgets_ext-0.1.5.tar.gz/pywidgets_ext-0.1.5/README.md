# pywidgets-ext

This is a custom widget module for `PySide6` that makes it easy to manage and use during development.

## Installation

Install using pip:

```bash
pip install pywidgets-ext
```

Install using poetry (recommended):

```bash
poetry add pywidgets-ext
```

## Usage

```python
from pywidgets_ext import *
```

## Modules

### PyFigureCanvas

`PyFigureCanvas` is a custom widget inheriting from `FigureCanvasQTAgg`. It's designed to display matplotlib charts. A unique feature is its magnified preview when the mouse hovers over it, which hides when the mouse leaves. The magnified view adjusts according to the screen size and mouse position. Additionally, `PyFigureCanvas` offers methods to get chart dimensions, calculate data ratio, and adjust graphics view size on resize.

To see it in action:

```python
python -m pywidgets_ext.PyFigureCanvas
```

![PyFigureCanvas](https://raw.githubusercontent.com/leoli0605/pywidgets-ext/main/docs/images/py_figure_canvas.webp)

Sample code:

```python
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QMainWindow, QApplication
from pywidgets_ext import PyFigureCanvas


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        fig, ax = self.create_sample_plot()
        self.canvas = PyFigureCanvas(fig)
        self.setup_main_window()

    def create_sample_plot(self):
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16], label="y = x^2")
        ax.set_title("Sample Plot")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend()
        return fig, ax

    def setup_main_window(self):
        self.setCentralWidget(self.canvas)
        self.setWindowTitle("PyFigureCanvas Demo")
        self.resize(600, 600)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
```

### PyGraphicsView

`PyGraphicsView` is a view class inheriting from `QGraphicsView`. It lets users click and drag in the scene to draw and adjust resizable rectangular regions (`ResizableRect`). It offers specific drawing and optimization options for better performance and visuals. Users can select rectangles and delete them using the `Delete` key. Also, it auto-adjusts rectangles when the scene size changes.

To see it in action:

```python
python -m pywidgets_ext.PyGraphicsView
```

![PyGraphicsView](https://raw.githubusercontent.com/leoli0605/pywidgets-ext/main/docs/images/py_graphics_view.webp)

Sample code:

```python
from PySide6.QtCore import Qt, QRectF, QPointF
from PySide6.QtWidgets import QApplication, QMainWindow
from pywidgets_ext import PyGraphicsView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = PyGraphicsView()
        self.view.setSceneRect(0, 0, 500, 500)
        self.setCentralWidget(self.view)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("PyGraphicsView Example")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
```

## Contributions

Contributions of any kind are welcome! Make sure to read the [Contribution Guide](https://github.com/leoli0605/pywidgets-ext/blob/main/CONTRIBUTING.md) first.

## License

This project is under the [MIT License](https://github.com/leoli0605/pywidgets-ext/blob/main/LICENSE).

## Author

- Leo - [Github](https://github.com/leoli0605)
