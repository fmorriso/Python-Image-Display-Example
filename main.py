import sys
from importlib.metadata import version

from PySide6.QtWidgets import QApplication

from image_window import ImageWindow
from program_settings import ProgramSettings


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_package_version(package_name: str) -> str:
    return version(package_name)


def main():
    app = QApplication(sys.argv)

    image_path = ProgramSettings.get_setting('IMAGE_FILE_PATH')
    title = f'Image Display Example using Python {get_python_version()} and PySide6 {get_package_version("pyside6")}'
    window = ImageWindow(image_path, title)

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'PySide6 version: {get_package_version("pyside6")}')

    main()
