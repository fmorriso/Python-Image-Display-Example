from typing import ClassVar

import pyautogui


class GuiSettings:
    """ A central location to store settings needed throughout this program."""

    __DEFAULT_SCALE_PERCENT: ClassVar[float] = 0.3333


    def __init__(self, pct: float = __DEFAULT_SCALE_PERCENT):
        # calculate game size as a percentage of device screen size
        self.__device_width, self.__device_height = pyautogui.size()
        self.screenPct: float = pct

        # calculate scaled screen width & height rounded to a  multiple of 10
        self.__scaled_width: int = int((self.__device_width * self.screenPct // 10) * 10)
        self.__scaled_height: int = int((self.__device_height * self.screenPct // 10) * 10)


    @classmethod
    def get_default_scale_percent(cls) -> float:
        """Getter method to return the default scale percent."""
        return cls.__DEFAULT_SCALE_PERCENT


    @property
    def device_width(self) -> int:
        """Device width in pixels."""
        return self.__device_width


    @property
    def device_height(self) -> int:
        """Device height in pixels."""
        return self.__device_height


    @property
    def scaled_height(self) -> int:
        """Scaled height in pixels."""
        return self.__scaled_height


    @property
    def scaled_width(self) -> int:
        """Scaled width in pixels."""
        return self.__scaled_width


    def __str__(self) -> str:
        return (f'device width: {self.__device_width}, device height: {self.__device_height}'
                f'\n\tscaled width: {self.__scaled_width}, '
                f'scaled height{self.__scaled_height}')


    def __repr__(self) -> str:
        return (f'device width: {self.__device_width}, device height: {self.__device_height}'
                f'\n\tscaled width: {self.__scaled_width}, '
                f'scaled height{self.__scaled_height}')
