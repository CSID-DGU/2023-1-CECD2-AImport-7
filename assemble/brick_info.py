import numpy as np
from itertools import combinations_with_replacement as combi
from random import *
from math import *

brick_boundary = dict()

def initBoundary(brick):
    for colmun in range(brick.shape[1]):
        row_list = "0" * brick.shape[0]
        brick_boundary[colmun] = row_list

def calcBoundary(col, row, size):
    for i in range(0, size):
        temp = list(brick_boundary[col + i])
        temp[row] = str(size)
        brick_boundary[col + i] = ''.join(temp)

def manual_append(manual, position, color, size):
    
    if position != (-1, -1):
        if(size > 4):
            position_list = splitBlock(assembleBlock(size), position)
            for position in position_list:
                calcBoundary(position[1], position[0], position[2])
                instruction = list()
                instruction.append((position[0], position[1]))
                instruction.append(color)
                instruction.append(position[2])
                manual.append(instruction)
        else:
            calcBoundary(position[1], position[0], size)
            instruction = list()
            instruction.append(position)
            instruction.append(color)
            instruction.append(size)
            manual.append(instruction)
    else:
        instruction = list()
        instruction.append(position)
        instruction.append(color)
        instruction.append(size)
        manual.append(instruction)

    return instruction            

def checkNotJoin(manual):
    for key, val in brick_boundary.items():
        lines = val.split('0')
        #print(lines)
        for l in lines:
            if l != '':
                sizes = [int(num) for num in l]
                maxSize = max(sizes)
                if maxSize == 1:
                    if val[val.find(l) - 1] != 0:
                        start = val.find('0' + l)
                    else:
                        start = val.find(l)
                    for row in range(start, start + len(l)):
                        #print(row, key)
                        manual_Delete(manual, row, key)
                    #print(val[start:start+len(l)])

def manual_Delete(manual, row, col):
    for index in range(0, len(manual)):
        if manual[index][0] == (row, col):
            manual.pop(index)
            break


def print_brickBoundary():
    
    for key, val in brick_boundary.items():
        print(key, val)
    
    #print(brick_boundary)
        

def assembleBlock(size):
    arr = list()
    start = (int)(ceil(size / 4))
    end = (int)(ceil(size / 2))
    divide = randint(start, end)
    while len(arr) == 0:
        arr = [list(x) for x in combi(range(1, 4), divide) if sum(x)== size]
        divide = randint(start, end)
    return arr

def splitBlock(arr, position):
    select_combi = randint(0, len(arr) - 1)
    position_list = list()
    now_col = position[1]
    for i in arr[select_combi]:
        position_list.append((position[0], now_col, i))
        now_col = now_col + i
    return position_list

def generate(brick):
    initBoundary(brick)
    manual = list()
    position = tuple()
    color = "none"
    size = 0
    height, width = brick.shape
    
    brick = np.flip(brick, axis=0)

    for i in range(brick.shape[0]):
        color = "none"
        size = 0
        for j in range(brick.shape[1]):
            if brick[i, j] != None:                
                if color == "none":
                    color = brick[i, j]
                    size = 1
                    position = (i, j)

                elif color == brick[i, j]:
                    size = size + 1

                    '''   
                    if size >= 4:
                        manual.append(manual_append(position, color, size))
                        if j < brick.shape[1] - 1:
                            color = brick[i][j + 1]
                            position = (i, j + 1)
                        size = 0
                    '''
                elif color != brick[i, j]:
                    manual_append(manual, position, color, size)                                       
                    color = brick[i, j]
                    size = 1
                    position = (i, j)                    
                       
                if j == brick.shape[1] - 1 and size > 0:
                    manual_append(manual, position, color, size)
                
            else:
                if size > 0:
                    manual_append(manual, position, color, size)
                    color = "none"
                    size = 0
                    
            if j == brick.shape[1] - 1:
                separator = tuple()
                separator = (-1, -1)
                manual_append(manual, separator, "-1", -1)
             
    #print_brickBoundary()
    #checkNotJoin(manual)
    return manual, height, width