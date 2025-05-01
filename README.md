# Python Image Display Example
Example of how to display a .jpg image in Python using PySide6 for the GUI scaled
to a user-defined percentage of available device width and height.

## Usage Notes:

1.  Make sure you have installed all the packages mentioned in the _*requirements.txt*_ file.
    If you are using a virtual environment and run into permission errors, one solution after setting up the python virtual environment
    that worked for me is as follows:
    ```text
    pip install --no-cache-dir -r requirements.txt
    ```
1.  Create a `.env` file with the following entries, modified for your specific situation:
    1. IMAGE_FILE_PATH='c:\sample pictures\Penguins.jpg'
    1. WINDOW_SCALE_PCT=40.0
 
## Tools Used

| Tool          |  Version |
|:--------------|---------:|
| Python        |   3.13.3 |
| pillow        |   11.2.1 | 
| PyAutoGUI     |   0.9.54 |
| PySide6       |    6.9.0 |
| Python-dotenv |    1.1.0 |
| PyCharm       | 2025.1.0 |
| VSCode        |   1.99.0 |

## Change History

| Date       | Description                                          |
|:-----------|:-----------------------------------------------------|
| 2025-04-30 | Initial creation                                     |
| 2025-05-01 | Make fetch of screen scaling percentage more robust. |

## References

* [PySide6 official documentation](https://doc.qt.io/qtforpython-6/)
* [PySide6 tutorials](https://doc.qt.io/qtforpython-6/tutorials/index.html)
* [PySide6 examples](https://doc.qt.io/qtforpython-6/examples/index.html)
* [PySide6 examples on PyPL](https://pypi.org/project/PySide6-Examples/)
* [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
* [PyAutoGUI Tutorial](https://www.pythoncentral.io/pyautogui-tutorial-how-to-automate-gui-tasks-with-python/0)
