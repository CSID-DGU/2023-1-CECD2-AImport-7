import numpy as np

brick = np.array([['white', 'white', 'white', 'white', 'brown', 'brown', 'white', 'brown'],
                 ['white', 'white', 'white', 'white', 'brown', 'brown', 'white', 'brown'],
                 ['white', 'white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown'],
                 ['white', 'white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown'],
                 ['white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown'],
                 ['white', 'brown', 'brown', 'brown', 'brown', 'white', 'white', 'brown'],
                 ['white', 'brown', 'black', 'brown', 'white', 'white', 'white', 'brown'],
                 ['brown', 'black', 'white', 'white', 'black', 'black', 'brown', 'white']])

def print_manual(manual):
    for i, instruction in enumerate(manual):
        print("intruction " + str(i + 1))
        print("position: " + str(instruction[0]))
        print("color: " + instruction[1])
        print("size: " + str(instruction[2]) + " * 1\n")

def manual_append(position, color, size):
    instruction = list()
    position_list = position[:]
    instruction.append(position_list)
    instruction.append(color)
    instruction.append(size)
    position.clear()
    return instruction

def func(brick):
    #np.flip(brick, axis=0)
    manual = list()
    position = list()
    color = "none"
    size = 0
    
    for i in range(brick.shape[0]):
        for j in range(brick.shape[1]):
            if j == 0:
                color = brick[i, j]
                size = 1
                position.append((i, j))
            else:
                if color == "none":
                    color = brick[i, j]
                    size = 1
                    position.append((i, j))
                    
                elif color == brick[i, j]:
                    size = size + 1
                    position.append((i, j))
                    
                    if size >= 4:
                        manual.append(manual_append(position, color, size))
                        color = "none"
                        size = 0
            
                elif color != brick[i, j]:
                    manual.append(manual_append(position, color, size))
                                        
                    color = brick[i, j]
                    size = 1
                    position.append((i, j))
                    
                
                if j == brick.shape[1] - 1 and size > 0:
                    manual.append(manual_append(position, color, size))
                    
    print_manual(manual)
    return manual

assemble = func(brick)
