import json, re, os
from xml.etree.ElementTree import parse
from datetime import datetime

brick = ["0", "3005.dat", "3004.dat", "3622.dat", "3010.dat"]
# color = {"black" : 0, 
#          "blue" : 1, 
#          "green" : 2, 
#          "red" : 4,
#          "brown" : 6,
#          "grey" : 7,  
#          "white" : 15,
#          "purple" : 22,
#          "orange" : 25,
#          "sky_blue" : 232}

color = {
    'Black': 0,
    'White': 15,
    'Red': 4,
    'Bright_Red': 324,
    'Green': 2,
    'Bright_Green': 10,
    'Blue': 1,
    'Bright_Blue': 212,
    'Yellow': 14,
    'Bright_Yellow': 226,
    'Orange': 125,
    'Bright_Orange': 191,
    'Brown': 6,
    'Light_Brown': 86,
    'Tan': 19,
    'Dark_Tan': 28,
    'Dark_Grey': 8,
    'Light_Grey': 7,
    'Dark_Bluish_Grey': 72,
    'Light_Bluish_Grey': 71,
    'Purple': 22,
    'Pink': 13,
    'Lime': 27,
    'Lime_Green': 120
}


offset = [0, 10, 20, 30, 40]

def jsonToldraw(dir):
    with open(dir, 'r') as json_data:
        data = json.load(json_data)   
    
    pageSeparator = data["PageSeparator"]

    ldraw_file_content = ""
    latitude, longitude = 45.0, 20.0
    ldraw_file_content = f"0 !LPUB ASSEM CAMERA_ANGLES {latitude}   {longitude}\n"
    ldraw_file_content += "0 STEP" + "\n"
    for sequence, entry in enumerate(data["Manual"]):
        if entry.get("Warning") :
            break
        if sequence +  1 in pageSeparator:
            ldraw_file_content += "0 STEP" + "\n"
        part_size = entry["Size"].split(" * ")
        part_size = int(float(part_size[0]))
        positions = eval(entry["Position"])
        row, col = positions[0]
        part_definition = f"1 0 0 0 0 1 0 -1 0 {brick[part_size]}"
        brick_color = entry["Color"]
        ldraw_command = f"1 {color[brick_color]} {col * 20 + offset[part_size]} 0 {row * 20} {part_definition}"               
        ldraw_file_content += ldraw_command + "\n"
    return ldraw_file_content

def xmlToldraw(dir):
    tree = parse(dir)
    root = tree.getroot()
    instructions = root.findall("instruction")

    pageSeparator = root.findtext("pageSeparate")
    pageSeparator = re.sub(r"[^\d\s]", "", pageSeparator)
    pageSeparator = pageSeparator.split(" ")
    print(pageSeparator)

    ldraw_file_content = ""
    latitude, longitude = 45.0, 20.0
    ldraw_file_content = f"0 !LPUB ASSEM CAMERA_ANGLES {latitude}   {longitude}\n"
    ldraw_file_content += "0 STEP" + "\n"
    for sequence, inst in enumerate(instructions):
        if (str)(sequence + 1) in pageSeparator:
            ldraw_file_content += "0 STEP" + "\n"
        part_size = inst.findtext("Size").split(" * ")
        part_size = int(float(part_size[0]))
        
        positions = inst.findtext("Position")            
        positions = re.sub(r"[^\d\s]", "", positions)
        positions = positions.split(" ")
        row, col = int(positions[0]), int(positions[1])
        part_definition = f"1 0 0 0 0 1 0 -1 0 {brick[part_size]}"
        brick_color = inst.findtext("Color")
        ldraw_command = f"1 {color[brick_color]} {col * 20 + offset[part_size]} 0 {row * 20} {part_definition}"               
        ldraw_file_content += ldraw_command + "\n"
    return ldraw_file_content

def saveLdr(ldraw_file_content, dir):
    os.makedirs(dir, exist_ok=True)
    now = datetime.now()
    name = now.strftime('%Y-%m-%d')
    dir = dir + '/' + name + '.ldr'
    with open(dir, 'wb') as f:
        f.write(ldraw_file_content.encode('utf-8'))    
    return dir

'''
def listToldraw(manual):
    ldraw_file_content = ""
    latitude, longitude = 45.0, 20.0
    ldraw_file_content = f"0 !LPUB ASSEM CAMERA_ANGLES {latitude}   {longitude}\n"
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

def convertToldr(input_form, input_dir):
    latitude, longitude = 45.0, 20.0
    ldraw_file_content = f"0 !LPUB ASSEM CAMERA_ANGLES {latitude}   {longitude}\n"        
    if input_form == 'json':
        ldraw_file_content += jsonToldraw(input_dir)
    elif input_form == 'xml':
        ldraw_file_content += xmlToldraw(input_dir)
    elif input_form == 'list':
        ldraw_file_content += listToldraw(input_dir)
    return ldraw_file_content
''' 
    