from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout
from PIL import Image


class ImageWindow(QWidget):
    def __init__(self, image_file_path: str, title: str = '', width=640, height=480) -> None:
        super().__init__()
        self.setWindowTitle(title)

        scaled_image = self.get_image(image_file_path, width, height)

        # Create a QLabel and set the pixmap inside it.
        label = QLabel(self)
        label.setPixmap(scaled_image)
        label.setScaledContents(True)  # Optional: scale image to fit label size

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        # Resize window to fit the image
        self.resize(width, height)

    @staticmethod
    def get_image(image_file_path: str, width: int, height: int) -> QPixmap:
        """
        load and scale an image
        :param image_file_path: The path to the image file in the local file system.
        :type image_file_path: string
        :param width: width to scale the image to.
        :type width: integer
        :param height: height to scale the image to.
        :type height: integer
        :return: The scaled image.
        :rtype: QPixmap
        """
        # Load and resize image using Pillow
        image = Image.open(image_file_path).resize((width, height))  # Scale image
        # Convert Pillow Image to a QByteArray
        image_data = image.convert("RGBA").tobytes("raw", "RGBA")
        # Create QImage from raw data
        qimage = QImage(image_data, image.width, image.height, QImage.Format_RGBA8888)

        # Convert QImage to QPixmap
        pixmap = QPixmap.fromImage(qimage)
        return pixmap