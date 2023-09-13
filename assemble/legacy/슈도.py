import numpy as np

brick = np.array([['white', 'white', 'white', 'white', 'brown', 'brown', 'white', 'brown'],
                 ['white', 'white', 'white', 'white', 'brown', 'brown', 'white', 'brown'],
                 ['white', 'white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown'],
                 ['white', 'white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown'],
                 ['white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown'],
                 ['white', 'brown', 'brown', 'brown', 'brown', 'white', 'white', 'brown'],
                 ['white', 'brown', 'black', 'brown', 'white', 'white', 'white', 'brown'],
                 ['brown', 'black', 'white', 'white', 'black', 'black', 'brown', 'white']])


def func(brick):
    manual = list()
    position = tuple()
    count = 0
    
    for i in range(brick.shape[0]):
        color = brick[i, 0]
        position = (i, 0)
        count = 0
        for j in range(brick.shape[1]):
            if color == brick[i, j]:
                count = count + 1
            else:
                select = list()
                select.append(position)
                select.append(color)
                select.append(count)
                manual.append(select)

                position = (i, j)
                color = brick[i, j]
                count = 1
            
            if count == 4:
                select = list()
                select.append(position)
                select.append(color)
                select.append(count)
                manual.append(select)
                if j + 1 < brick.shape[1]:
                    color = brick[i, j+1]
                count = 0
                position = (i, j + 1)
                
            if j == brick.shape[1] - 1 and count > 0:
                select = list()
                select.append(position)
                select.append(color)
                select.append(count)
                manual.append(select)
    return manual

assemble = func(brick)
print(assemble)
