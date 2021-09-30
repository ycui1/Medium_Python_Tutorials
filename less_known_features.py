from pprint import pprint
http_responses = [
    {"status": 200, "result": [1, 2, 3]},
    {"status": 404, "result": "Endpoint not found"},
    {"status": 400, "result": "API error"}
]
print(http_responses)
pprint(http_responses)

pprint(http_responses, indent=4)


from collections import namedtuple

# Create the Coordinate class
Coordinate = namedtuple("Coordinate", "latitude longitude")
# Create an instance
north_pole = Coordinate(90, 0)
north_pole
# Access attribute with dot notation
north_pole.latitude, north_pole.longitude

# Unpacking
latitude, longitude = north_pole
print(latitude, longitude)
# Indexing
print(north_pole[0])
# Iteration
for point in north_pole:
    print(point)

# Create a new instance by replacing a field value
north_pole1 = north_pole._replace(longitude=135)
print(north_pole, north_pole1)
# See the dictionary of the instance
north_pole._asdict()

for letter in 'ab':
    print(letter)
else:
    print('Letters have been printed.')

for letter in 'ab':
    print(letter)
    if letter == 'b':
        break
else:
    print('Letters have been printed.')

from enum import Enum

class Direction(Enum):
    EAST = 1
    SOUTH = 2
    WEST = 3
    NORTH = 4

Direction.EAST.name
Direction.EAST.value


class DirectionOneLine(Enum):
    EAST = 1; SOUTH = 2; WEST = 3; NORTH = 4;

DirectionFunctional = Enum('Direction', 'EAST SOUTH WEST NORTH')

class DirectionLetter(Enum):
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'
    NORTH = 'N'
DirectionLetter.SOUTH.value

for direction in DirectionLetter:
    print(direction.name, direction.value)

DirectionLetter.EAST in DirectionLetter

# Create an item using a proper value
Direction(2)
# Create an item using an improper value
Direction(5)
