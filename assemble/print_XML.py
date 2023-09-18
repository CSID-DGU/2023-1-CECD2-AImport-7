from xml.etree.ElementTree import Element, SubElement, ElementTree
from datetime import datetime
import os

def manualTotree(manual):
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

def saveTomxl(manual, dir):
        manual_tree = manualTotree(manual)
        os.makedirs(dir, exist_ok=True)
        now = datetime.now()
        name = now.strftime('%Y-%m-%d %H:%M:%S')
        dir = dir + '/' + name + '.xml'
        with open(dir, "wb") as file:
            manual_tree.write(file, encoding='utf-8', xml_declaration=True)
        return dir