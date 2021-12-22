"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"]=10
    data["cols"]=10
    data["board_size"]=500
    data["cell_size"]= (int)(data["board_size"]/( data["rows"]*data["cols"]))
    data["num_ships"]= 5
    
    temp=emptyGrid(data["rows"],data["cols"])
    data["userboard"]=test.testGrid()
    data["compboard"]=addShips(temp,data["num_ships"])
    return data
  


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    
    showShips = True
    drawGrid(data, compCanvas,data["compboard"] ,showShips)
    drawGrid(data, userCanvas,data["userboard"],showShips)
    return None


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid=[]
    for i in range (rows):
        col=[]
        for j in range(cols):
            col.append(EMPTY_UNCLICKED)
        grid.append(col)    

    return grid



'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    import random
    row = random.randint(1,8)
    col = random.randint(1,8)
    hv = random.randint(0,1)
    if hv==0:
      p=row-1
      randomValue=col
    else:
      p=col-1
      randomValue=row
    d1=[[randomValue for j in range(1)] for i in range(3)]

    for i in range(len(d1)):
      d2=d1[i]
 
      d2.insert(hv,p)
      p=p+1
    return d1


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    count=0
    for i in range(len(ship)):
        row=ship[i][0]
        col=ship[i][1]
        if grid[row][col]==EMPTY_UNCLICKED:
        # print(True)
           count=count+1
    # else: print (False)
    if count==len(ship):
        return True
    
    else:
       return False



'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):

    # for j in range(numShips):
    #     ship = createShip()  
    #     check =checkShip(grid,ship)
    #     if check == True:
    #         for i in range(len(ships)):
    #          row=ships[i][0]
    #          col=ships[i][1]
    #          grid[row][col]=SHIP_UNCLICKED 
    count=0
    while count < numShips:
        ship = createShip()  
        check =checkShip(grid,ship)
        if check :
            for i in ship:
               row=i[0]
               col=i[1]
               grid[row][col]=SHIP_UNCLICKED
            count=count+1
      
            
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
      for i in range(data["rows"]):
        for j in range(data["cols"]):
            if grid[i][j]==SHIP_UNCLICKED:
               canvas.create_rectangle(j*data["cols"]*data["cell_size"], i*data["rows"]*data["cell_size"], (j+1)*data["cols"]*data["cell_size"], (i+1)*data["rows"]*data["cell_size"],fill="yellow")
            else:
               canvas.create_rectangle(j*data["cols"]*data["cell_size"], i*data["rows"]*data["cell_size"], (j+1)*data["cols"]*data["cell_size"], (i+1)*data["rows"]*data["cell_size"],fill="blue")   
      canvas.pack()
      return None
 
    
### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    row=[]
    col=[]
    for i in range(len(ship)):
        row.append(ship[i][0])
        col.append(ship[i][1])
    count=0
    truecount=0
    c=col[0]
    for i in range(1,len(ship)):
        if(c==col[i]):
           count=count+1
    if count==len(ship)-1:
       truecount=truecount+1  
 
    row.sort()
    count=0
    for i in range (len(ship)-1):
        if (row[i]+1==row[i+1]):
          count=count+1
    if (count==len(ship)-1):
        truecount=truecount+1  
    if truecount==2:
        return True
    else:
        return False


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    row=[]
    col=[]
    for i in range(len(ship)):
        row.append(ship[i][0])
        col.append(ship[i][1])
    count=0
    truecount=0
    r=row[0]
    for i in range(1,len(ship)):
        if(r==row[i]):
           count=count+1
    if count==len(ship)-1:
       truecount=truecount+1  
 
    col.sort()
    count=0
    for i in range (len(ship)-1):
        if (col[i]+1==col[i+1]):
          count=count+1
    if (count==len(ship)-1):
        truecount=truecount+1  
    if truecount==2:
        return True
    else:
        return False   


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    l=[]
    i=(int)(event.y/(data["cols"]*data["cell_size"]))
    j=(int)(event.x/(data["rows"]*data["cell_size"]))
    l.append(i)
    l.append(j)
    return l


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    return


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    # test.testEmptyGrid()
    # test.testCheckShip()
    # test.testCreateShip()
    test.testAddShips()
    test.testMakeModel()
    test.testDrawGrid()
    test.testGrid()
   

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
