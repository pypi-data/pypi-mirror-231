import matplotlib
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtSvgWidgets import *
from PySide6.QtWidgets import *

matplotlib.use("Qt5Agg")
from copy import deepcopy

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class PyFigureCanvas(FigureCanvas):
    def __init__(self, *args, **kwargs):
        super(PyFigureCanvas, self).__init__(*args, **kwargs)
        self.current_border = None
        self.magnified_view = None  # Placeholder for magnified figure preview
        self.setMouseTracking(True)  # Enable mouse tracking for hover events

    def enterEvent(self, event):
        """Handle mouse hover event to show magnified view."""
        # Check if there's an existing magnified view and hide it
        if self.magnified_view:
            self.magnified_view.hide()
            self.magnified_view = None

        mouse_pos = event.globalPos()  # Get the global mouse position
        self.create_magnified_view(mouse_pos)
        QTimer.singleShot(5, self.magnified_view.show)

    def leaveEvent(self, event):
        """Hide magnified view when mouse leaves the canvas."""
        if self.magnified_view:
            QTimer.singleShot(10, self.magnified_view.hide)
            self.magnified_view = None

    def create_magnified_view(self, mouse_pos=None):
        """Create and style magnified preview."""
        self.magnified_view = QDialog(self)
        self.magnified_view.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.magnified_view.setStyleSheet(
            "background-color: rgba(0, 0, 0, 128);"
        )  # Semi-transparent black

        # Create a new FigureCanvas with the same figure and add to the QDialog
        copied_figure = deepcopy(self.figure)
        new_canvas = FigureCanvas(copied_figure)
        layout = QVBoxLayout(self.magnified_view)
        layout.addWidget(new_canvas)
        self.magnified_view.setLayout(layout)

        # Get screen geometry
        screen_geometry = QGuiApplication.primaryScreen().geometry()

        # Determine the maximum possible size for the preview based on mouse position
        max_width = screen_geometry.width() - mouse_pos.x()

        # Set the size of the magnified view
        size_factor = 0.3  # You can adjust this for desired size
        width = min(int(screen_geometry.width() * size_factor), max_width)
        height = int(screen_geometry.height() * size_factor)

        # Position the magnified view based on mouse position
        if mouse_pos:
            if mouse_pos.y() < screen_geometry.height() // 2:
                # Position at right-top corner
                self.magnified_view.setGeometry(
                    mouse_pos.x(), mouse_pos.y() - height, width, height
                )
            else:
                # Position at right-bottom corner
                self.magnified_view.setGeometry(mouse_pos.x(), mouse_pos.y(), width, height)
        else:
            # Default to center of the screen if mouse position is not provided
            self.magnified_view.setGeometry(
                (screen_geometry.width() - width) // 2,
                (screen_geometry.height() - height) // 2,
                width,
                height,
            )

    def setGraphicsView(self, graphicsView):
        self.graphicsView = graphicsView

    def get_figure_dimensions(self):
        """
        Get the size of the figure in pixels.
        """
        ax = self.figure.axes[0]
        pos = ax.get_position()

        dpi = self.figure.dpi
        width = pos.width * self.figure.get_figwidth() * dpi
        height = (
            pos.height * self.figure.get_figheight() * dpi - ax.title.get_window_extent().height
        )
        return int(width), int(height)

    def get_ratio(self):
        fig_width, fig_height = self.get_figure_dimensions()
        data_width, data_height = (
            self.figure.axes[0].get_xlim()[1] - self.figure.axes[0].get_xlim()[0],
            self.figure.axes[0].get_ylim()[1] - self.figure.axes[0].get_ylim()[0],
        )
        width_ratio, height_ratio = data_width / fig_width, data_height / fig_height
        width_ratio, height_ratio = abs(width_ratio), abs(height_ratio)
        return width_ratio, height_ratio

    def showEvent(self, event):
        super(PyFigureCanvas, self).showEvent(event)

    def resizeEvent(self, event):
        super(PyFigureCanvas, self).resizeEvent(event)

        fig_width, fig_height = self.get_figure_dimensions()
        # print(f"Figure size: {fig_width} x {fig_height}")

        if hasattr(self, "graphicsView"):
            self.graphicsView.setSceneRect(0, 0, fig_width, fig_height)

            # if self.current_border:
            #     self.graphicsView.scene().removeItem(self.current_border)
            #     self.current_border = None
            # self.current_border = QGraphicsRectItem(self.graphicsView.sceneRect())
            # self.current_border.setPen(QPen(QColor(255, 0, 0), 1))
            # self.graphicsView.scene().addItem(self.current_border)


# This file can be run directly from Python to test the widget.
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create a simple figure
        fig, ax = self.create_sample_plot()

        # Use PyFigureCanvas class to display the figure
        self.canvas = PyFigureCanvas(fig)

        # Set up the main window
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
