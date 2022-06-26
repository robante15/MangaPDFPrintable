import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsView


class GFXHelper():
    def loadPreview(image_path: str, gfx_viewer: QGraphicsView):
        """Carga la vista previa de una imágen dentro de un visor

        Args:
            image_path (str): Ruta de la imagen a mostrar
            gfx_viewer (QGraphicsView): Visor donde se va a mostrar la imagen
        """
        if os.path.isfile(image_path):
            scene = QtWidgets.QGraphicsScene()
            pixmap = QPixmap(image_path)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            gfx_viewer.setScene(scene)
            gfx_viewer.fitInView(
                scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
