import os
import sys

from typing import Tuple
from typing import List

directions = {
    'N': (0, (0, 1)),
    'W': (1, (-1, 0)),
    'S': (2, (0, -1)),
    'E': (3, (1, 0))
}

turns = {
    0: 'N',
    1: 'W',
    2: 'S',
    3: 'E'
}


class Rover:
    def __init__(self, grid: Tuple, location: Tuple, direction: str) -> None:
        self.grid: Tuple = None
        self._curDirection: str = None
        self.location: Tuple = None
        self.instructions: List = ['L', 'R', 'M']

        self.reset(grid, location, direction)

    def reset(self, grid: Tuple , location: Tuple, direction) -> None:
        # Drop the rover on a grid by init'ing the class
        if direction not in directions:
            raise ValueError(f"Invalid direction:{direction}")
        self._curDirection: str = direction

        self.grid = grid

        if not self.isSafe(location[0] , location[1]):
            raise ValueError("Location out of grid", location)
        self.location = location

    @property
    def curDirection(self):
        return self._curDirection

    @curDirection.setter
    def curDirection(self, value):
        if value not in directions:
            raise ValueError(f"Setting invalid direction:{value} on rover. Abort")
        self._curDirection = value

    def isSafe(self, x, y):
        if x < 0 or x > self.grid[0]:
            return False
        if y < 0 or y > self.grid[1]:
            return False

        return True

    def getPosition(self) -> (int, int, str):
        return self.location[0] , self.location[1], self.curDirection

    def move(self, instruction):
        if instruction not in self.instructions:
            # Deliberately not raising an exception but ignoring an invalid
            # instruction.
            print(f"Invalid instruction:{instruction}. Ignoring")
            return

        if instruction == 'M':
            # Move one step in current direction
            dx, dy = directions[self.curDirection][1]
            mx = self.location[0] + dx
            my = self.location[1] + dy

            if not self.isSafe(mx, my):
                print("Rover will move out of grid. Please turn or backup")
                return

            self.location = (mx, my)
        elif instruction == 'L':
            # turns is initialized such that adding one to cur_direction switches
            # rover to its direction on the left. For e.g when rover is facing north(0)
            # 0 + 1 = 1 which is WEST. 1 + 1 is SOUTH.
            # Adding one to curDirection turns the rover left and subtracting 1 turns it right

            cur_direction = directions[self.curDirection][0]
            new_direction = turns[(cur_direction + 1) % len(turns)]
            self.curDirection = new_direction
        elif instruction == 'R':
            cur_direction = directions[self.curDirection][0]
            new_direction = turns[(cur_direction - 1) % len(turns)]
            self.curDirection = new_direction

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify the input file to control the rover")
        sys.exit()

    filePath = sys.argv[1]

    if not os.path.isfile(filePath):
        print(f"File path:{filePath} does not exist. Exiting...")
        sys.exit()

    lineList = [[]]
    cnt = 0
    with open(filePath) as fp:
        for line in fp:
            if all(i == '#' for i in line.strip()):
                cnt += 1
                lineList.append([])
                continue

            lineList[cnt].append(line.rstrip('\n').replace(" ", ""))

    rover = None
    for cnt, inp in enumerate(lineList):
        if len(inp) < 3:
            print("Input should list grid, initial location and instructions "
                  "in 3 separate lines")
            sys.exit()

        #Calling int can raise exception if grid is not a numeric value expressed as string.
        grid = (int(inp[0][0]), int(inp[0][1]))
        # This section can use some error handling. Assumes user to specify the input in the right
        # format. e.g '1 2 N'
        position = (int(inp[1][0]), int(inp[1][1]))
        orientation = inp[1][2]
        instructions = inp[2]

        if cnt == 0:
            rover = Rover(grid, position, orientation)
        else:
            rover.reset(grid, position, orientation)

        for i in instructions:
            rover.move(i)
        print(rover.getPosition())
