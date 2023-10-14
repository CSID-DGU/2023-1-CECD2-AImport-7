import numpy as np

def manual_append(position, color, size):
    instruction = list()
    position_list = position[:]
    instruction.append(position_list)
    instruction.append(color)
    instruction.append(size)
    position.clear()
    return instruction

def generate(brick):
    manual = list()
    position = list()
    color = "none"
    size = 0 

    brick = np.flip(brick,axis=0)

    for i in range(brick.shape[0]):
        color = "none"
        size = 0
        for j in range(brick.shape[1]):
            if brick[i, j] != None:                
                if color == "none":
                    color = brick[i, j]
                    size = 1
                    position.append((i, j))

                elif color == brick[i, j]:
                    size = size + 1
                    position.append((i, j))
                        
                    if size >= 4:
                        manual.append(manual_append(position, color, size))
                        if j < brick.shape[1] - 1:
                            color = brick[i][j + 1]
                        size = 0
                    
                elif color != brick[i, j]:
                    manual.append(manual_append(position, color, size))                                        
                    color = brick[i, j]
                    size = 1
                    position.append((i, j))                    
                       
                if j == brick.shape[1] - 1 and size > 0:
                    manual.append(manual_append(position, color, size))
                
            else:
                if size > 0:
                    manual.append(manual_append(position, color, size))
                    color = "none"
                    size = 0

    return manual