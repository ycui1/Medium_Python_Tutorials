from typing import TypeVar

TBox = TypeVar("TBox", bound="Box")

class Box:
    def paint_color(self, color: str) -> TBox:
        self.color = color
        return self


from typing import Literal

def paint_color(color: Literal["red", "green", "blue", "yellow"]):
    pass

paint_color("cyan")