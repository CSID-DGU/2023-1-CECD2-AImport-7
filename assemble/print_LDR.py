import json, re, os
from xml.etree.ElementTree import parse

brick = ["0", "3005.dat", "3004.dat", "3622.dat", "3010.dat"]
color = {"black" : 0, 
         "blue" : 1, 
         "green" : 2, 
         "red" : 4,
         "grey" : 7,  
         "white" : 15,
         "purple" : 22,
         "orange" : 25,
         "sky_blue" : 232}

offset = [0, 10, 20, 30, 40]

def jsonToldraw(dir):
    with open(dir, 'r') as json_data:
        data = json.load(json_data)   
    
    ldraw_file_content = ""
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

def xmlToldraw(dir):
    tree = parse(dir)
    root = tree.getroot()
    instructions = root.findall("instruction")
    
    ldraw_file_content = ""
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

def listToldraw(manual):
    ldraw_file_content = ""
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

def convertToldr(input_form, input_dir, name):
    name += '.ldr'
    ldraw_file_content = f"0 Name: {name}\n"
    ldraw_file_content += "0 Author: AImport\n"
    latitude, longitude = 45.0, 20.0
    ldraw_file_content += f"0 !LPUB ASSEM CAMERA_ANGLES {latitude}   {longitude}\n"
    if input_form == 'json' or input_form == 'xml':
        input_dir = str(os.getcwd()) + '/' + input_dir
        
    if input_form == 'json':
        ldraw_file_content += jsonToldraw(input_dir)
    elif input_form == 'xml':
        ldraw_file_content += xmlToldraw(input_dir)
    elif input_form == 'list':
        ldraw_file_content += listToldraw(input_dir)
    return ldraw_file_content
    
def saveLdr(ldraw_file_content, dir, name):
    abs_dir = str(os.getcwd()) + '/' + dir
    os.makedirs(abs_dir, exist_ok=True)
    abs_dir = abs_dir + '/' + name + '.ldr'
    with open(abs_dir, 'wb') as f:
        f.write(ldraw_file_content.encode('utf-8'))        
    return abs_dir
    