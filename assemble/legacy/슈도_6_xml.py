import numpy as np
from xml.etree.ElementTree import Element, SubElement, ElementTree, parse
import re

brick = np.array([['white', 'white', 'white', 'white', 'brown', 'brown', 'white', 'brown'],
                 ['white', 'white', 'white', 'white', 'brown', 'brown', 'white', 'brown'],
                 ['white', 'white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown'],
                 ['white', 'white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown'],
                 ['white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown'],
                 ['white', 'brown', 'brown', 'brown', 'brown', 'white', 'white', 'brown'],
                 ['white', 'brown', 'black', 'brown', 'white', 'white', 'white', 'brown'],
                 ['brown', 'black', 'white', 'white', 'black', 'black', 'brown', 'white'],
                 ['white', 'white', None, 'white', 'brown', 'brown', 'white', 'brown'],
                 ['white', 'white', 'white', 'white', 'brown', 'brown', 'white', None],
                 ['white', 'white', 'brown', 'brown', 'brown', 'brown', 'brown', 'brown'],
                 ['white', 'white', None, 'brown', 'brown', 'brown', None, 'brown'],
                 ['white', 'brown', 'brown', 'brown', None, 'brown', 'brown', 'brown'],
                 [None, 'brown', 'brown', 'brown', 'brown', 'white', 'white', 'brown'],
                 ['white', 'brown', 'black', 'brown', 'white', 'white', 'white', 'brown'],
                 ['brown', 'black', None, None, 'black', 'black', 'brown', 'white']])

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

    def manualTotree(self, manual):
        root = Element("manual")
        if len(manual) == 0:
            info = Element("information")
            info.set("Warning", "Manual is empty!")
            root.append(info)
        else:
            for i, instruction in enumerate(manual):
                inst = Element("instruction")
                inst.set("Sequence", str(i + 1))
                root.append(inst)

                instruction_position = SubElement(inst, "Position")
                instruction_position.text = str(instruction[0])

                instruction_color = SubElement(inst, "Color")
                instruction_color.text = str(instruction[1])

                instruction_size = SubElement(inst, "Size")
                instruction_size.text = str(instruction[2]) + " * 1"

        tree = ElementTree(root)
        return tree
    def xmlToldraw(self):
        tree = parse(r"C:\Users\kocan\Desktop\2023-1-CECD2-AImport-7\이승현\manual.xml")
        root = tree.getroot()
        instructions = root.findall("instruction")
        ldraw_file_content = "0 Name: manual.ldr" + "\n"
        ldraw_file_content += "0 Author: AImport" + "\n"
        brick = ["0", "3005.dat", "3004.dat", "3622.dat", "3010.dat"]
        color = {"black" : 0, "brown" : 6, "white" : 15}
        offset = [0, 10, 20, 30, 40]
        for inst in instructions:
            ldraw_file_content += "0 STEP" + "\n"
            part_size = inst.findtext("Size").split(" * ")
            part_size = int(float(part_size[0]))
            positions = inst.findtext("Position")            
            positions = re.sub(r"[^\d\s]", "", positions)
            positions = positions.split(" ")
            row, col = int(positions[0]), int(positions[1])
            part_definition = f"1 0 0 0 1 0 0 0 1 {brick[part_size]}"
            brick_color = inst.findtext("Color")
            ldraw_command = f"1 {color[brick_color]} {col * 20 + offset[part_size]} 0 {row * 20} {part_definition}"               
            ldraw_file_content += ldraw_command + "\n"
        return ldraw_file_content
    
    def saveTomxl(self, manual):
        manual_tree = self.manualTotree(manual)
        with open(r"C:\Users\kocan\Desktop\2023-1-CECD2-AImport-7\이승현\manual.xml", "wb") as file:
            manual_tree.write(file, encoding='utf-8', xml_declaration=True)

    def saveLdr(self, ldraw_file_content):
        with open(r'C:\Users\kocan\Desktop\2023-1-CECD2-AImport-7\이승현\manual.ldr', 'wb') as f:
            f.write(ldraw_file_content.encode('utf-8'))
m = Manual(brick)
m.saveTomxl(m.generate())
m.saveLdr(m.xmlToldraw())