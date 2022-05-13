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


data = {
    "one": 1,
    "two": 2,
    "three": {
        "four": 4,
        "five": 5,
        "six": {
            "6": 6,
            "seven": 7
        }
    }
}
data["three"]["6"]["6"]

from typing import Generic, TypeVar

Dim1 = TypeVar('Dim1')
Dim2 = TypeVar('Dim2')
Dim3 = TypeVar('Dim3')

class Shape1(Generic[Dim1]):
    pass

class Shape2(Generic[Dim1, Dim2]):
    pass

class Shape3(Generic[Dim1, Dim2, Dim3]):
    pass


from typing import TypedDict

class Name(TypedDict):
    first_name: str
    last_name: str


from typing import TypedDict

class _Name(TypedDict):
    first_name: str
    last_name: str

class Name(_Name, total=False):
    middle_name: str