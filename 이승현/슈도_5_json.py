import numpy as np
import json

brick = np.array([['white', 'white', 'white', 'white', 'brown', 'brown', 'white', 'brown'],
                 ['white', 'white', 'white', 'white', 'brown', 'brown', 'white', 'brown'],
                 ['white', 'white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown'],
                 ['white', 'white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown'],
                 ['white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown'],
                 ['white', 'brown', 'brown', 'brown', 'brown', 'white', 'white', 'brown'],
                 ['white', 'brown', 'black', 'brown', 'white', 'white', 'white', 'brown'],
                 ['brown', 'black', 'white', 'white', 'black', 'black', 'brown', 'white']])

brick2 = np.array([['white', 'white', None, 'white', 'brown', 'brown', 'white', 'brown'],
                 ['white', 'white', 'white', 'white', 'brown', 'brown', 'white', None],
                 ['white', 'white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown'],
                 ['white', 'white', None, 'brown', 'brown', 'brown', None, 'brown'],
                 ['white', 'brown', 'brown', 'brown', None, 'brown', 'brown', 'brown'],
                 [None, 'brown', 'brown', 'brown', 'brown', 'white', 'white', 'brown'],
                 ['white', 'brown', 'black', 'brown', 'white', 'white', 'white', 'brown'],
                 ['brown', 'black', None, None, 'black', 'black', 'brown', 'white']])

brick3 = np.array([[None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None]])

class Manual:
    def __init__(self, brick):
        #self.brick = np.flip(brick, axis=0)
        self.brick = brick

    def print_manual(self, manual):
        for i, instruction in enumerate(manual):
            print("intruction " + str(i + 1))
            print("position: " + str(instruction[0]))
            print("color: " + instruction[1])
            print("size: " + str(instruction[2]) + " * 1\n")

    def manual_append(self, position, color, size):
        instruction = list()
        position_list = position[:]
        instruction.append(position_list)
        instruction.append(color)
        instruction.append(size)
        position.clear()
        return instruction

    def generate(self):
        manual = list()
        position = list()
        color = "none"
        size = 0        
        for i in range(self.brick.shape[0]):
            color = "none"
            size = 0
            for j in range(self.brick.shape[1]):
                if self.brick[i, j] != None:                
                    if color == "none":
                        color = self.brick[i, j]
                        size = 1
                        position.append((i, j))

                    elif color == self.brick[i, j]:
                        size = size + 1
                        position.append((i, j))
                        
                        if size >= 4:
                            manual.append(self.manual_append(position, color, size))
                            if j < self.brick.shape[1] - 1:
                                color = self.brick[i][j + 1]
                            size = 0
                    
                    elif color != self.brick[i, j]:
                        manual.append(self.manual_append(position, color, size))                                        
                        color = self.brick[i, j]
                        size = 1
                        position.append((i, j))                    
                        
                    if j == self.brick.shape[1] - 1 and size > 0:
                        manual.append(self.manual_append(position, color, size))
                
                else:
                    if size > 0:
                       manual.append(self.manual_append(position, color, size))
                       color = "none"
                       size = 0

        return manual

    def manualTodict(self, manual):
        instruction__list = list()
        if len(manual) == 0:
            info_list = list()
            info_list.append(("Warning", "Manual is empty!"))
            info_dict = dict(info_list)
            instruction__list.append(info_dict)
        else:
            for i, instruction in enumerate(manual):
                instruction_tuple = list()
                instruction_tuple.append(("Sequence", i + 1))
                instruction_tuple.append(("Position", str(instruction[0])))
                instruction_tuple.append(("Color", instruction[1]))
                instruction_tuple.append(("Size", str(instruction[2]) + " * 1"))
                instruction_dict = dict(instruction_tuple)
                instruction__list.append(instruction_dict)
        manual_dict = {"Manual": instruction__list}
        return manual_dict

    def saveTojson(self, manual):
        manual_dict = self.manualTodict(manual)
        with open(r'C:\Users\kocan\OneDrive\바탕 화면\종설\2023-1-CECD2-AImport-7\이승현\manual.json', 'w', encoding='utf-8') as f:
            json.dump(manual_dict, f, indent="\t")

m = Manual(brick2)
m.saveTojson(m.generate())

