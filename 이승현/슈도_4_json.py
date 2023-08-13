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
            for j in range(self.brick.shape[1]):
                if j == 0:
                    color = self.brick[i, j]
                    size = 1
                    position.append((i, j))
                else:                    
                    if color == self.brick[i, j]:
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
                        
        return manual

    def manualTodict(self, manual):
        instruction__list = list()
        for i, instruction in enumerate(manual):
            instruction_tuple = list()
            instruction_tuple.append(("number", i + 1))
            instruction_tuple.append(("position", str(instruction[0])))
            instruction_tuple.append(("color", instruction[1]))
            instruction_tuple.append(("size", str(instruction[2]) + " * 1"))
            instruction_dict = dict(instruction_tuple)
            instruction__list.append(instruction_dict)
        manual_dict = {"manual": instruction__list}
        return manual_dict

    def saveTojson(self, manual):
        manual_dict = self.manualTodict(manual)
        with open(r'C:\Users\kocan\OneDrive - dongguk.edu\컴공\컴퓨터공학종합설계1\manual.json', 'w', encoding='utf-8') as f:
            json.dump(manual_dict, f, indent="\t")

m = Manual(brick)
m.saveTojson(m.generate())

