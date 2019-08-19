
def solveKTUtil(x, y, moves, soln):
    def printSolution(soln):
        for x in range(len(soln)):
            for y in range(len(soln)):
                print(soln[x][y])

    def isSafe(x, y, soln):
        if (x >= 0 and x < 8) and (y >= 0 and y < 8) and soln[x][y] == -1:
            return True
        else:
            return False

    print(moves)
    if moves == 8 * 8:
        printSolution(soln)
        return True

    dx = [1, 2, -1, -2, -1, -2, 1, 2]
    dy = [2, 1, 2, 1, -2, -1, -2, -1]

    for k in range(len(dx)):
        mx = x + dx[k]
        my = y + dy[k]

        if isSafe(mx, my, soln):
            soln[mx][my] = moves
            if solveKTUtil(mx, my, moves + 1, soln):
                return True

            soln[mx][my] = -1
    return False

def solveKT():
    moves = 1
    x = 0
    y = 0
    soln = [[-1 for _ in range(8)] for _ in range(8)]
    soln[0][0] = 0
    solveKTUtil(x, y, moves, soln)

if __name__ == "__main__":
    solveKT()


