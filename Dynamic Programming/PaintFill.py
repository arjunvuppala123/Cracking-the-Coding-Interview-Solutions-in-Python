'''
paint fill
'''

def paintFill(screen, x, y, newColor):
    '''
    paint fill
    '''
    oldColor = screen[x][y]
    if oldColor == newColor:
        return
    paintFillHelper(screen, x, y, oldColor, newColor)

def paintFillHelper(screen, x, y,oldColor,newColor):
    '''
    paint fill helper
    '''
    if x < 0 or x >= len(screen) or y < 0 or y >= len(screen[0]):
        return
    if screen[x][y] != oldColor:
        return
    screen[x][y] = newColor
    paintFillHelper(screen, x+1, y, oldColor, newColor)
    paintFillHelper(screen, x-1, y, oldColor, newColor)
    paintFillHelper(screen, x, y+1, oldColor, newColor)
    paintFillHelper(screen, x, y-1, oldColor, newColor)

if __name__ == '__main__':
    screen = [
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1]
    ]
    paintFill(screen, 3, 3, 2)
    print(screen)