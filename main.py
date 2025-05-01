import sys
from importlib.metadata import version

from PySide6.QtWidgets import QApplication

from gui_settings import GuiSettings
from image_window import ImageWindow
from program_settings import ProgramSettings


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_package_version(package_name: str) -> str:
    return version(package_name)


def main():
    app = QApplication(sys.argv)

    pct_scaling = float(ProgramSettings().get_setting('WINDOW_SCALE_PCT'))/100.0
    gui_settings = GuiSettings(pct_scaling)

    image_path = ProgramSettings.get_setting('IMAGE_FILE_PATH')
    title = f'Image Display Example using Python {get_python_version()}, PySide6 {get_package_version("pyside6")}, PyAutoGUI {get_package_version("pyautogui")}'
    window = ImageWindow(image_path, title, gui_settings.scaled_width, gui_settings.scaled_height)

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'PySide6 version: {get_package_version("pyside6")}')
    print(f'PyAutoGUI version: {get_package_version("pyautogui")}')
    print(f'python-dotenv version: {get_package_version("python-dotenv")}')

    main()
