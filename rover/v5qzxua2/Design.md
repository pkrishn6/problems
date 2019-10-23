# Design:
The application defines a class Rover which should be "dropped" in a grid by init'ing the class.
So the class expects the driver to provide
  * the starting location and orientation of the rover and
  * the boundaries of the grid

The init function verifies the validity of the provided input and sets up the rover.

The move function processes one instruction at a time and if the instruction is to
   * move: proceeds one step in the current direction
   * L,R : sets the cur_direction to the new orientation by simply adding or subtracting 1
     to the cur_direction and getting the new_direction from the hash table. The hash_table is
     set up such that, the next direction while turning left, would be the next integer value
     For e.g: North is 0 and West is 1

creation of the Rover object expects the grid, location and orientation to be specified. 
A created Rover object can be reset using the reset api that expects the same arguments.

# Assumptions:
  * Not many beyong what is specified in the question
  * Directions NE, NW, SW, SE is not supported but the code can easily be extended
    by adding these directions to the directions and turns hash-table. + 1 (L) or N would put
    the rover on NW instead of W
  * An invalid instruction, one that would move the rover out of the grid is simply ignored
    instead of raising a ValueError as that felt more natural to how the code should behave
  * Please check the section on input for assumptions about the input format

# Execution instructions:
  Pre-req: The code required python3 to run as typing is used to define types of variables
           for better code readability
  Execute: python rover.py </path/to/input.txt>

# Input file and format:
 *  Input file can exist in any location on the filesystem.
 *  Some error handling is done on the reading the input but the code
    expects the user to provide the input in the correct format. 
    Line 1 is grid, Line 2 is initial position and Line 3 is instructions
 * The code expects multiple inputs to be separated by "#####". No restriction on the number of "#" 
 * The code expects the grid to be specified for each input even the user does not intend to change the grid.

# Future improvements:
 * More error handling around the input file parsing
 * Support cases where if the user does not specify the grid, use the grid from the previous input section.
