import numpy as np
from itertools import combinations_with_replacement as combi
from random import *
from math import *

flag1, flag2 = True, True
brick_boundary = dict()
brick_list = dict()
'''
def initBrickList():
    colors = ['Black', 'White', 'Red', 'Green', 'Blue', 'Yellow', 'Brown', 'Purple', 'Pink', 'Orange']
    for c in colors:
        sizes = [0, 16, 20, 20, 8, 32, 4]
        brick_list[c] = sizes
'''      
def initBrickList():
    colors = ['Black', 'White', 'Red', 'Green', 'Blue', 'Yellow', 'Brown', 'Purple', 'Pink', 'Orange']
    for c in colors:
        sizes = [0, 16, 40, 0, 40, 0, 4]
        brick_list[c] = sizes

def manual_append(manual, position, color, size):    
    if position != (-1, -1):
        if (size == 1) or (size == 2) or (size == 4) or (size == 6):
            #checkBrickAmount(color, size)
            calcBoundary(position[1], position[0], size)
            instruction = list()
            instruction.append(position)
            instruction.append(color)
            instruction.append(size)
            manual.append(instruction)
     
        else:            
            position_list = splitBlock(assembleBlock(color, size), position)
            for position in position_list:
                #checkBrickAmount(color, position[2])
                calcBoundary(position[1], position[0], position[2])
                instruction = list()
                instruction.append((position[0], position[1]))
                instruction.append(color)
                instruction.append(position[2])
                manual.append(instruction)

    else:
        if not manual or manual[-1][2] != -1:
            instruction = list()
            instruction.append(position)
            instruction.append(color)
            instruction.append(size)
            manual.append(instruction)          

def assembleBlock(color, size):
    arr = list()
    start = (int)(ceil(size / 6))
    end = (int)(ceil(size / 2))
    for split in range(start, end + 1):
        arr = arr + [list(x) for x in combi([1, 2, 4, 6], split) if sum(x) == size]
    
    if size % 2 == 0:
        for i in range(len(arr) - 1, -1, -1):
            if 1 in arr[i]:
                arr.pop(i)
                
    return arr

def splitBlock(arr, position):
    select_combi = randint(0, len(arr) - 1)
    position_list = list()
    now_col = position[1]
    shuffle(arr[select_combi])
    for i in arr[select_combi]:
        position_list.append((position[0], now_col, i))
        now_col = now_col + i
    return position_list

def checkBrickAmount(brick_color, size):
    if brick_list[brick_color][size] <= 0:
        global flag1 
        flag1 = False
        return
    brick_list[brick_color][size] = brick_list[brick_color][size] - 1

def initBoundary(brick):
    for colmun in range(brick.shape[1]):
        row_list = "0" * brick.shape[0]
        brick_boundary[colmun] = row_list

def calcBoundary(col, row, size):
    for i in range(0, size):
        temp = list(brick_boundary[col + i])
        temp[row] = str(size)
        brick_boundary[col + i] = ''.join(temp)

def deleteEdge(manual):
    for key, val in brick_boundary.items():
        lines = val.split('0')
        for l in lines:
            if l != '':
                sizes = [int(num) for num in l]
                maxSize = max(sizes)
                if maxSize == 1:
                    if val.find(l) > 0:
                        if val[val.find(l) - 1] != 0:
                            start = val.find('0' + l) + 1
                        else:
                            start = val.find(l)
                    else:
                        if val[val.find(l) + len(l)] == '0':
                            start = val.find(l + '0')
                        else:
                            start = val.find(l)
                    for row in range(start, start + len(l)):
                        manual_Delete(manual, row, key)
                        temp = list(brick_boundary[key])
                        temp[row] = '0'
                        brick_boundary[key] = ''.join(temp)
                            

def manual_Delete(manual, row, col):
    for index in range(0, len(manual)):
        if manual[index][0] == (row, col):
            manual.pop(index)
            break

def print_brickBoundary():
    for key, val in brick_boundary.items():
        print(key, val)

def validJoin(brick, manual):
    for key, val in brick_boundary.items():
        if (key == 0) or (key > 0 and brick_boundary[key - 1] == ('0' * len(val))):
            continue

        for row in range(0, len(val)):
            if val[row] == "0":
                continue
            if not findPosition(row, key, manual):
                break
            if row == len(val) - 1:
                global flag2
                flag2 = False
                return
        
def findPosition(row, col, manual):
    for m in manual:
        if m[0] == (row, col):
            return True
    return False

def generate(brick):
    global flag1, flag2, brick_boundary, brick_list
    height, width = brick.shape
    brick = np.flip(brick, axis=0)
    count = 0
    while count <= 100:
        flag1, flag2 = True, True
        brick_boundary.clear()
        brick_list.clear()
        initBrickList()
        initBoundary(brick)
        manual = list()
        position = tuple()
        color = "none"
        size = 0
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
               
        manual.pop()
        deleteEdge(manual)
        validJoin(brick, manual)
        
        if flag1 and flag2:
            break
        count = count + 1
    if count >= 100:
        print("Don't create manual!!")
        exit()
        
    return manual, height, width