from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout


class ImageWindow(QWidget):
    def __init__(self, image_file_path: str, title: str = '', width=640, height=480) -> None:
        super().__init__()
        self.setWindowTitle(title)

        # Load the image
        pixmap = QPixmap(image_file_path)

        scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Create a QLabel and set the pixmap
        label = QLabel(self)
        label.setPixmap(scaled_pixmap)
        label.setScaledContents(True)  # Optional: scale image to fit label size

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        # Resize window to fit the image
        self.resize(width, height)
