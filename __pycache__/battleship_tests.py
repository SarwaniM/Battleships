from battleship import *

### SUPPLEMENTAL TEST FUNCTIONS ###

def testGrid(): # Used in Week 1
    grid = [ [1] * 10 for row in range(10) ]
    grid[0][2] = 2
    grid[0][3] = 2
    grid[0][4] = 2
    grid[2][7] = 2
    grid[3][7] = 2
    grid[4][7] = 2
    return grid
    print("... done!")

def testShip(): # Used in Week 2
    return [ [5, 4], [5, 5], [5, 6] ]


### WEEK 1 TESTS ###

def testEmptyGrid():
    print("Testing emptyGrid()...", end="")
    assert(emptyGrid(5, 5) == [ [1,1,1,1,1],
                                [1,1,1,1,1],
                                [1,1,1,1,1],
                                [1,1,1,1,1],
                                [1,1,1,1,1] ])
    assert(emptyGrid(4, 6) == [ [1,1,1,1,1,1],
                                [1,1,1,1,1,1],
                                [1,1,1,1,1,1],
                                [1,1,1,1,1,1] ])
    assert(emptyGrid(0, 0) == [ ])

    # Make sure that the grid doesn't have any aliasing problems
    g = emptyGrid(3, 3)
    g[0][1] = "foo"
    assert(g[1][1] != "foo")
    print("... done!")

def testCreateShip():
    print("Testing createShip()...", end="")
    ship = createShip()
    assert(type(ship) == list)
    assert(len(ship) == 3)
    ship.sort()
    # All in same row/col
    assert((ship[0][0] == ship[1][0] == ship[2][0]) or \
        (ship[0][1] == ship[1][1] == ship[2][1]))
    # All connected
    assert((ship[0][0] + 1 == ship[1][0] == ship[2][0] - 1) or \
        (ship[0][1] + 1 == ship[1][1] == ship[2][1] - 1))
    print("... done!")

def testCheckShip():
    print("Testing checkShip()...", end="")
    grid = [ [1, 1, 2, 1], [1, 1, 2, 1], [1, 1, 2, 1], [2, 2, 2, 1] ]
    assert(checkShip(grid, [[0, 0], [1, 0], [2, 0]]) == True)
    assert(checkShip(grid, [[0, 2], [1, 2], [2, 2]]) == False)
    assert(checkShip(grid, [[1, 1], [2, 1], [3, 1]]) == False)
    print("... done!")

def testAddShips():
    print("Testing addShips()...", end="")
    grid = [ [1] * 10 for row in range(10) ]
    grid2 = addShips(grid, 2)
    count = 0
    for row in grid2:
        for cell in row:
            if cell == 2:
                count += 1
    assert(count == 6) # Two ships should take up 6 cells total

    grid = [ [1] * 10 for row in range(10) ]
    grid5 = addShips(grid, 5)
    count = 0
    for row in grid5:
        for cell in row:
            if cell == 2:
                count += 1
    assert(count == 15) # Five ships should take up 15 cells total
    print("... done!")

def testMakeModel():
    print("Testing makeModel()...", end="")
    data = { }
    makeModel(data)
    values = data.values()
    assert(10 in values) # have you stored the number of rows and cols?
    assert(500 in values) # have you stored the board size?
    assert(5 in values) # have you stored the number of ships?
    listCount = 0
    for value in values:
        if type(value) == list:
            listCount += 1
    assert(listCount >= 2) # have you set up grids for both the user and the enemy?
    print("... done!")

def testDrawGrid():
    print("Testing drawGrid()...")
    print("TEMPORARILY SET YOUR USER GRID TO test.testGrid()")
    print("THEN CHECK WHETHER THE CANVAS SHOWS THE PICTURE IN THE WRITEUP")
    print("... done!")

def week1Tests():
    testEmptyGrid()
    testCreateShip()
    testCheckShip()
    testAddShips()
    testMakeModel()
    testDrawGrid()

### WEEK 2 TESTS ###

def testIsVertical():
    print("Testing isVertical()...", end="")
    assert(isVertical([ [0, 1], [1, 1], [2, 1] ]) == True)
    assert(isVertical([ [2, 1], [0, 1], [1, 1] ]) == True) # order doesn't matter
    assert(isVertical([ [1, 0], [1, 1], [1, 2] ]) == False)
    assert(isVertical([ [0, 0], [1, 0], [3, 0] ]) == False) # must be sequential
    assert(isVertical([ [1, 0], [3, 2], [0, 1] ]) == False)
    assert(isVertical([ [4, 5], [5, 5], [6, 5] ]) == True)
    print("... done!")

def testIsHorizontal():
    print("Testing isHorizontal()...", end="")
    assert(isHorizontal([ [1, 0], [1, 1], [1, 2] ]) == True)
    assert(isHorizontal([ [1, 2], [1, 0], [1, 1] ]) == True) # order doesn't matter
    assert(isHorizontal([ [0, 1], [1, 1], [2, 1] ]) == False)
    assert(isHorizontal([ [0, 0], [0, 1], [0, 3] ]) == False) # must be sequential
    assert(isHorizontal([ [0, 1], [2, 3], [1, 0] ]) == False)
    assert(isHorizontal([ [5, 4], [5, 5], [5, 6] ]) == True)
    print("... done!")

def testGetClickedCell():
    print("Testing getClickedCell()...", end="")
    data = { }
    makeModel(data)
    class Struct():
        pass
    event = Struct()
    event.x = 140
    event.y = 321
    # Note that y corresponds to row, and x corresponds to col
    assert(getClickedCell(data, event) == [6, 2])
    event.x = 499
    event.y = 1
    assert(getClickedCell(data, event) == [0, 9])
    # Make sure to get edges right! 200 could go either way
    event.x = 201
    event.y = 199
    assert(getClickedCell(data, event) == [3, 4])
    print("... done!")

def testDrawShip():
    print("Testing drawShip()...")
    print("TEMPORARILY SET YOUR USER GRID TO test.testShip()")
    print("THEN CHECK WHETHER THE CANVAS SHOWS THE PICTURE IN THE WRITEUP")
    print("... done!")

def testShipIsValid():
    print("Testing shipIsValid()...", end="")
    grid = [ [1] * 10 for row in range(10) ]
    grid[0][1] = 2

    # can't place a ship that overlaps the board
    ship = [ [0, 1], [1, 1], [2, 1] ]
    assert(shipIsValid(grid, ship) == False)
    grid[0][1] = 1
    grid[1][1] = 2
    assert(shipIsValid(grid, ship) == False)
    grid[1][1] = 1
    grid[2][1] = 2
    assert(shipIsValid(grid, ship) == False)
    grid[2][1] = 1
    grid[9][9] = 2
    assert(shipIsValid(grid, ship) == True) # no overlap!

    # can't place a ship that isn't horizontal or vertical
    ship = [ [0, 1], [2, 3], [5, 6] ]
    assert(shipIsValid(grid, ship) == False)
    print("... done!")

def week2Tests():
    testIsVertical()
    testIsHorizontal()
    testGetClickedCell()
    testDrawShip()
    testShipIsValid()

### WEEK 3 TESTS ###

def testUpdateBoard():
    print("Testing updateBoard()...", end="")
    data = { }
    makeModel(data)
    class Struct():
        pass

    board = [ [1] * 10 for row in range(10) ]
    board[4][3] = 2
    board[8][5] = 2
    updateBoard(data, board, 2, 1, "user")
    assert(board[2][1] == 3)
    updateBoard(data, board, 7, 4, "comp")
    assert(board[7][4] == 3)
    updateBoard(data, board, 4, 3, "user")
    assert(board[4][3] == 4)
    updateBoard(data, board, 8, 5, "comp")
    assert(board[8][5] == 4)
    print("... done!")

def testGetComputerGuess():
    print("Testing getComputerGuess()...", end="")
    # You can guess anywhere on an empty board
    board = [ [1] * 10 for row in range(10) ]
    guess = getComputerGuess(board)
    assert(len(guess) == 2 and 0 <= guess[0] < 10 and 0 <= guess[1] < 10)

    # If the board is full except for one spot, you need to guess that one
    board = [ [3] * 10 for row in range(10) ]
    board[3][6] = 1
    assert(getComputerGuess(board) == [3, 6])
    print("... done!")

def testIsGameOver():
    print("Testing isGameOver()...", end="")
    board = [ [3] * 10 for row in range(10) ]
    board[4][3] = 4
    board[5][3] = 4
    board[6][3] = 4
    assert(isGameOver(board) == True)
    board[3][5] = 1
    assert(isGameOver(board) == True) # cells can be unclicked if they aren't ships
    board[7][9] = 2
    assert(isGameOver(board) == False) # even one ship left means the game isn't over!
    print("... done!")

def testDrawGameOver():
    print("Testing drawGameOver()...")
    print("TEMPORARILY SET YOUR WINNER VARIABLE TO 'user'")
    print("THEN CHECK WHETHER THE CANVAS DISPLAYS THE APPROPRIATE MESSAGE")
    print("REPEAT BY SETTING THE WINNER VARIABLE TO 'comp'")
    print("... done!")

def week3Tests():
    testUpdateBoard()
    testGetComputerGuess()
    testIsGameOver()
    testDrawGameOver()
