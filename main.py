# Minesweeper1
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import re
from random import randint

numRows = 10
numCols = 12
grid    = []

def initGrid():
    for i in range( numRows ):
        grid.append( [] )
    for row in range(numRows):
        curRow = grid[row]
        initRow(curRow)
    setMines()
    

def initRow(curRow):
    for i in range(numCols):
        curRow.append('.')


def setMines():
    for row in range( numRows ):
        for col in range(numCols):
            if randint(0,8) == 8:
                setGridItem(row, col, '*')
            else:
                setGridItem(row, col, '.')


def setGridItem(row, col, s):
    grid[row][col] = s


def countMinesAbove(curRow, curCol):
    count = 0
    if curRow == 0:
        return 0
    if curCol == 0:
        if grid[curRow - 1][curCol] == '*':
            count += 1
        if grid[curRow - 1][curCol + 1] == '*':
            count += 1
    else:
        if grid[curRow - 1][curCol-1] == '*':
            count += 1
        if grid[curRow - 1][curCol  ] == '*':
            count += 1
        if curCol < numCols -1 and curRow < numRows - 1 and \
           grid[curRow - 1][curCol + 1] == '*':
            count += 1
    return count


def countMinesBelow(curRow, curCol):
    count = 0
    if curRow == numRows - 1:
        return 0
    if curCol == 0:
        if grid[curRow + 1][curCol] == '*':
            count += 1
        if grid[curRow + 1][curCol + 1] == '*':
            count += 1
    else:
        if grid[curRow + 1][curCol-1] == '*':
            count += 1
        if grid[curRow + 1][curCol  ] == '*':
            count += 1
        if curCol < numCols - 1 and \
           curRow < numRows - 1 and \
           grid[curRow + 1][curCol + 1] == '*':
            count += 1
    return count


def countMinesLeft(curRow, curCol):
    if curCol == 0:   # if we are in the leftmost column then no mines to the left
        return 0
    else:
        if grid[curRow][curCol-1] == '*':  # Check to the left
            return 1
        else:
            return 0


def countMinesRight(curRow, curCol):
    if curCol == numCols - 1:   # if we are in the rightmost column then no mines to the right
        return 0
    else:
        if grid[curRow][curCol+1] == '*':  # Check to the right
            return 1
        else:
            return 0


def countNearbyMines(curRow, curCol):
    return countMinesAbove(curRow, curCol) + \
           countMinesBelow(curRow, curCol) + \
           countMinesLeft( curRow, curCol)  + \
           countMinesRight(curRow, curCol)


def populateGridCounts():
    for row in range(numRows):
        for col in range(numCols):
            if grid[row][col] != '*':
                grid[row][col] = countNearbyMines(row, col)
            if col == numCols:
                grid[row][col+1] = countNearbyMines(row, col)


def printGrid():
    for row in grid:
        print(row)


def gameControlLoop():
   while True:
        s = input('Enter grid coordinates. Enter "0 0" to quit:')
        match = re.search(r"(\d+)\s(\d+)", s)
        if match:
            m = int( match.group(1) )
            n = int( match.group(2) )
        if m == 0 and n == 0:
            exit()
        if grid[m][n] == '*':
            print('You hit a mine!')
            exit()
        grid[m][n] = 'F'
        printGrid()
        

if __name__ == "__main__":
    initGrid()
    populateGridCounts()
    gameControlLoop()
    printGrid()