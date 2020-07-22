# Define a class
class DataStatus:
    SUCCEEDED = 1
    ERROR = 2

# Use the members
DataStatus.SUCCEEDED
DataStatus.ERROR

# Introspection
print("Type Checking:", type(DataStatus.SUCCEEDED))
print("Check Instance Type:", isinstance(DataStatus.SUCCEEDED, DataStatus))

from enum import Enum

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    def angle(self):
        right_angle = 90.0
        return right_angle * (self.value - 1)

    @staticmethod
    def angle_interval(direction0, direction1):
        return abs(direction0.angle() - direction1.angle())


east = Direction.EAST
print("South Angle:", east.angle())
west = Direction.WEST
print("Angle Interval:", Direction.angle_interval(east, west))

class DirectionOneLiner(Enum):
    NORTH = 1; EAST = 2; SOUTH = 3; WEST = 4


class DirectionRandomValue(Enum):
    NORTH = 111
    SOUTH = 222
    EAST = 333
    WEST = 444


class DirectionString(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'


print(Direction.NORTH)
print("Type:", type(Direction.SOUTH))
print("Check Instance:", isinstance(Direction.EAST, Direction))

# Create a member
north = Direction.NORTH
# Check the name and the value
print("Name:", north.name)
print("Value:", north.value)

# Create a member from an integer value
fetched_direction_value = 3
fetched_direction = Direction(fetched_direction_value)
print("Fetched Direction:", fetched_direction)
# Condition evaluations
print("Is the fetched direction north?", fetched_direction is Direction.NORTH)
print("Is the fetched direction east?", fetched_direction is Direction.EAST)

unknown_direction = Direction(6)

for direction in Direction:
    print(direction)

print("List of Direction:", list(Direction))

for name, direction in Direction.__members__.items():
    print(f"* Name: {name:<5}; * Direction: {direction}")

# Create an Enum class using the functional API
DirectionFunctional = Enum("DirectionFunctional", "NORTH EAST SOUTH WEST")
# Check what the Enum class is
print(DirectionFunctional)
# Check the items
print(list(DirectionFunctional))
print(DirectionFunctional.__members__.items())


# Create a function and patch it to the DirectionFunctional class
def angle(DirectionFunctional):
    right_angle = 90.0
    return right_angle * (DirectionFunctional.value - 1)


DirectionFunctional.angle = angle

# Create a member and access its angle
south = DirectionFunctional.SOUTH
print("South Angle:", south.angle())