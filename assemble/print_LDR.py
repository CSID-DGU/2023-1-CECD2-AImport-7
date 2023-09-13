import json, re, os
from xml.etree.ElementTree import parse

def jsonToldraw(dir, name):
    abs_dir = str(os.getcwd()) + '/' + dir
    with open(abs_dir, 'r') as json_data:
        data = json.load(json_data)
    
    name += '.ldr'
    ldraw_file_content = "0 Name: {name}" + "\n"
    ldraw_file_content += "0 Author: AImport" + "\n"
    brick = ["0", "3005.dat", "3004.dat", "3622.dat", "3010.dat"]
    color = {"black" : 0, "brown" : 6, "white" : 15}
    offset = [0, 10, 20, 30, 40]
    for entry in data["Manual"]:
        if entry.get("Warning") :
            break
        ldraw_file_content += "0 STEP" + "\n"
        part_size = entry["Size"].split(" * ")
        part_size = int(float(part_size[0]))
        positions = eval(entry["Position"])
        row, col = positions[0]
        part_definition = f"1 0 0 0 1 0 0 0 1 {brick[part_size]}"
        brick_color = entry["Color"]
        ldraw_command = f"1 {color[brick_color]} {col * 20 + offset[part_size]} 0 {row * 20} {part_definition}"               
        ldraw_file_content += ldraw_command + "\n"
    return ldraw_file_content

def xmlToldraw(dir, name):
    abs_dir = str(os.getcwd()) + '/' + dir
    tree = parse(abs_dir)
    root = tree.getroot()
    instructions = root.findall("instruction")
    name += '.ldr'
    ldraw_file_content = "0 Name: {name}" + "\n"
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

def listToldraw(manual, name):
    name += '.ldr'
    ldraw_file_content = "0 Name: {name}" + "\n"
    ldraw_file_content += "0 Author: AImport" + "\n"
    brick = ["0", "3005.dat", "3004.dat", "3622.dat", "3010.dat"]
    color = {"black" : 0, "brown" : 6, "white" : 15}
    offset = [0, 10, 20, 30, 40]
    if len(manual) == 0:
        return ldraw_file_content
    for entry in manual:
        ldraw_file_content += "0 STEP" + "\n"
        part_size = entry[2]
        row, col = entry[0][0]
        part_definition = f"1 0 0 0 1 0 0 0 1 {brick[part_size]}"
        brick_color = entry[1]
        ldraw_command = f"1 {color[brick_color]} {col * 20 + offset[part_size]} 0 {row * 20} {part_definition}"               
        ldraw_file_content += ldraw_command + "\n"
    return ldraw_file_content
    
def saveLdr(ldraw_file_content, dir, name):
    abs_dir = str(os.getcwd()) + '/' + dir
    os.makedirs(abs_dir, exist_ok=True)
    abs_dir = abs_dir + '/' + name + '.ldr'
    with open(abs_dir, 'wb') as f:
        f.write(ldraw_file_content.encode('utf-8'))
        
    return abs_dir