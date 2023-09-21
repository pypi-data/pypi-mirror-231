from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class ResizableRect(QGraphicsRectItem):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

        self.handleSize = 10
        self.created = False

        self.defaultPen = QPen(Qt.red, 2)
        self.selectedPen = QPen(Qt.blue, 2, Qt.DashLine)
        self.setPen(self.defaultPen)

        self.brush = QBrush(Qt.transparent)
        self.setBrush(self.brush)

        self.handles = [
            QGraphicsRectItem(
                -self.handleSize / 2, -self.handleSize / 2, self.handleSize, self.handleSize, self
            )
            for _ in range(4)
        ]
        self.updateHandles()
        self.setHandlesVisible(False)

        self.setFlag(QGraphicsRectItem.ItemIsMovable)
        self.setFlag(QGraphicsRectItem.ItemIsSelectable)
        self.setFlag(QGraphicsRectItem.ItemSendsGeometryChanges)
        self.setAcceptHoverEvents(True)

    def setRect(self, rect):
        super().setRect(rect)
        self.updateHandles()

    def updateHandles(self):
        rect = self.rect()
        self.handles[0].setPos(rect.topLeft())
        self.handles[1].setPos(rect.topRight())
        self.handles[2].setPos(rect.bottomLeft())
        self.handles[3].setPos(rect.bottomRight())
        for handle in self.handles:
            handle.setBrush(QBrush(Qt.blue))

    def setHandlesVisible(self, visible):
        for handle in self.handles:
            handle.setVisible(visible)

    def hoverMoveEvent(self, event):
        # Check if the mouse is over any of the handles and change the cursor shape accordingly
        for i, handle in enumerate(self.handles):
            if handle.isUnderMouse():
                if i == 0 or i == 3:
                    self.setCursor(Qt.SizeFDiagCursor)
                else:
                    self.setCursor(Qt.SizeBDiagCursor)
                break
        else:
            self.setCursor(Qt.ArrowCursor)
        super().hoverMoveEvent(event)

    def mousePressEvent(self, event):
        self.clickedHandle = None
        for handle in self.handles:
            if handle.isUnderMouse():
                self.clickedHandle = handle
                break
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        view = self.scene().views()[0]  # Get the associated GraphicsView
        sceneRect = view.sceneRect()  # Get the sceneRect of the GraphicsView
        mappedPos = self.mapToScene(event.pos())  # Map the position to scene coordinates
        if self.clickedHandle:
            index = self.handles.index(self.clickedHandle)
            rect = self.rect()

            # Calculate the new rectangle based on the handle being dragged
            if index == 0:
                newRect = QRectF(mappedPos, rect.bottomRight() + self.pos())
            elif index == 1:
                newRect = QRectF(
                    QPointF(rect.left() + self.pos().x(), mappedPos.y()),
                    QPointF(mappedPos.x(), rect.bottom() + self.pos().y()),
                )
            elif index == 2:
                newRect = QRectF(
                    QPointF(mappedPos.x(), rect.top() + self.pos().y()),
                    QPointF(rect.right() + self.pos().x(), mappedPos.y()),
                )
            elif index == 3:
                newRect = QRectF(rect.topLeft() + self.pos(), mappedPos)

            # Adjust the new rectangle to ensure it's within the sceneRect
            if not sceneRect.contains(newRect):
                newRect = newRect.intersected(sceneRect)

            self.setPos(newRect.topLeft())
            self.setRect(QRectF(0, 0, newRect.width(), newRect.height()))
            self.updateHandles()
        else:
            # Calculate the new position of the ResizableRect
            newPos = self.pos() + event.pos() - self.boundingRect().center()

            # Create a hypothetical new rectangle to check if it's within the sceneRect
            hypotheticalRect = self.rect().translated(newPos)

            # Adjust the position to ensure the entire ResizableRect remains within the sceneRect
            if hypotheticalRect.left() < sceneRect.left():
                newPos.setX(sceneRect.left() - self.rect().left())
            if hypotheticalRect.right() > sceneRect.right():
                newPos.setX(sceneRect.right() - self.rect().right())
            if hypotheticalRect.top() < sceneRect.top():
                newPos.setY(sceneRect.top() - self.rect().top())
            if hypotheticalRect.bottom() > sceneRect.bottom():
                newPos.setY(sceneRect.bottom() - self.rect().bottom())

            self.setPos(newPos)

    def mouseReleaseEvent(self, event):
        self.clickedHandle = None
        super().mouseReleaseEvent(event)

    def itemChange(self, change, value):
        if change == QGraphicsRectItem.ItemSelectedChange:
            if value:
                self.setPen(self.selectedPen)
                self.setHandlesVisible(True)
            else:
                self.setPen(self.defaultPen)
                self.setHandlesVisible(False)
        return super().itemChange(change, value)


class PyGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setScene(QGraphicsScene())
        self.setRenderHints()
        self.setOptimizations()
        self.setAdditionalProperties()
        self.rect = None
        self.startPos = None
        self.referenceSceneRect = QRectF(0, 0, 1, 1)

    def setRenderHints(self):
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setRenderHint(QPainter.TextAntialiasing)

    def setOptimizations(self):
        self.setOptimizationFlag(QGraphicsView.DontAdjustForAntialiasing, True)
        self.setOptimizationFlag(QGraphicsView.DontSavePainterState, True)

    def setAdditionalProperties(self):
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setInteractive(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.startPos = self.mapToScene(event.position().toPoint())
            if not self.itemAt(event.pos()) and self.sceneRect().contains(self.startPos):
                self.rect = ResizableRect(self.startPos.x(), self.startPos.y(), 0, 0)
                self.scene().addItem(self.rect)
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.startPos and self.rect:
            endPos = self.mapToScene(event.position().toPoint())
            if (endPos - self.startPos).manhattanLength() > 5 and self.sceneRect().contains(
                endPos
            ):  # Check if endPos is within sceneRect
                self.rect.setRect(QRectF(self.startPos, endPos).normalized())
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.rect and self.rect.rect().width() > 0 and self.rect.rect().height() > 0:
            self.rect.created = True
        self.rect = None
        self.startPos = None
        super().mouseReleaseEvent(event)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            selected_items = self.scene().selectedItems()
            for item in selected_items:
                self.scene().removeItem(item)
                del item
        super().keyPressEvent(event)

    def setSceneRect(self, x, y, w, h):
        super().setSceneRect(x, y, w, h)
        self.adjustResizableRects()

    def adjustResizableRects(self):
        scaleX = self.sceneRect().width() / self.referenceSceneRect.width()
        scaleY = self.sceneRect().height() / self.referenceSceneRect.height()
        for item in self.scene().items():
            if isinstance(item, ResizableRect):
                # Adjust the size of the ResizableRect
                rect = item.rect()
                newTopLeft = QPointF(rect.left() * scaleX, rect.top() * scaleY)
                newBottomRight = QPointF(rect.right() * scaleX, rect.bottom() * scaleY)
                item.setRect(QRectF(newTopLeft, newBottomRight))

                # Adjust the position of the ResizableRect
                newPos = item.pos()
                newPos.setX(newPos.x() * scaleX)
                newPos.setY(newPos.y() * scaleY)
                item.setPos(newPos)

        self.referenceSceneRect = self.sceneRect()

    def getResizableRectsCoordinates(self):
        coordinates = []
        for item in self.scene().items():
            if isinstance(item, ResizableRect) and item.created:
                topLeft = item.mapToScene(item.rect().topLeft())
                bottomRight = item.mapToScene(item.rect().bottomRight())
                coordinates.append((topLeft, bottomRight))
        return coordinates


# This file can be run directly from Python to test the widget.
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = PyGraphicsView()
        self.view.setSceneRect(0, 0, 500, 500)
        # border = QGraphicsRectItem(self.view.sceneRect())
        # self.view.scene().addItem(border)
        self.setCentralWidget(self.view)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("PySide6 QGraphicsView Example")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
