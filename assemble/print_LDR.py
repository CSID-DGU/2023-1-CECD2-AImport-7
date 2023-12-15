import json, re, os
from xml.etree.ElementTree import parse
from datetime import datetime

brick = ["0", "3005.dat", "3004.dat", "3622.dat", "3010.dat", "0", "3009.dat"]
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
    'Bright Red': 324,
    'Green': 2,
    'Bright Green': 10,
    'Blue': 1,
    'Bright Blue': 212,
    'Yellow': 14,
    'Bright Yellow': 226,
    'Orange': 125,
    'Bright Orange': 191,
    'Brown': 6,
    'Light Brown': 86,
    'Tan': 19,
    'Dark Tan': 28,
    'Dark Grey': 8,
    'Light Grey': 7,
    'Dark Bluish Grey': 72,
    'Light Bluish Grey': 71,
    'Purple': 22,
    'Pink': 13,
    'Lime': 27,
    'Lime Green': 120
}

'''
color = {
    'Black': 0,
    'White': 15,
    'Red': 4,
    'Green': 2,
    'Blue': 1,
    'Yellow': 14,
    'Brown': 6,
    'Purple': 22,
    'Pink': 13,
    'Orange': 125,
}
'''
offset = [0, 10, 20, 30, 40, 50, 60]

def jsonToldraw(dir):
    with open(dir, 'r') as json_data:
        data = json.load(json_data)   
    
    pageSeparator = data["PageSeparator"]
    width = data["Width"]
    ldraw_file_content = ""
    latitude, longitude = 45.0, 0.0
    ldraw_file_content = f"0 !LPUB ASSEM CAMERA_ANGLES {latitude}   {longitude}\n"

    assemble_content = ""
    pl_max = 0
    pl_set = set()
    
    for sequence, entry in enumerate(data["Manual"]):
        if entry.get("Warning") :
            break
        if sequence +  1 in pageSeparator:
            assemble_content += "0 STEP" + "\n"
            pl_max = max(pl_max, len(pl_set))
            pl_set.clear()
            
        part_size = entry["Size"].split(" * ")
        part_size = int(float(part_size[0]))
        position = eval(entry["Position"])
        row, col = position
        part_definition = f"1 0 0 0 0 1 0 -1 0 {brick[part_size]}"
        brick_color = entry["Color"]
        pl_set.add((brick_color, part_size))
        ldraw_command = f"1 {color[brick_color]} {col * 20 + offset[part_size]} 0 {row * 24} {part_definition}"               
        assemble_content += ldraw_command + "\n"
        
    pl_max = max(pl_max, len(pl_set))
    
    if width > 25:
        scale = (20 / width)
        scale = round(scale, 2)
        ldraw_file_content += f"0 !LPUB ASSEM MODEL_SCALE GLOBAL{scale: .4f}" + "\n"
    
    if pl_max > 6:
        ldraw_file_content += f"0 !LPUB PLI MODEL_SCALE GLOBAL{6 / pl_max: .4f}" + "\n"
        ldraw_file_content += f"0 !LPUB PLI INSTANCE_COUNT FONT \"Arial,{(int)(36 * 6 / pl_max)},-1,5,75,0,0,0,0,0,Bold\"\n"
    
    ldraw_file_content += assemble_content
        
    return ldraw_file_content

def xmlToldraw(dir):
    tree = parse(dir)
    root = tree.getroot()
    instructions = root.findall("instruction")

    pageSeparator = root.findtext("pageSeparate")
    pageSeparator = re.sub(r"[^\d\s]", "", pageSeparator)
    pageSeparator = pageSeparator.split(" ")

    ldraw_file_content = ""
    latitude, longitude = 45.0, 0.0
    ldraw_file_content = f"0 !LPUB ASSEM CAMERA_ANGLES {latitude}   {longitude}\n"
    
    width = (int)(root.findtext("width"))
    
    assemble_content = ""
    pl_max = 0
    pl_set = set()
    
    for sequence, inst in enumerate(instructions):
        if (str)(sequence + 1) in pageSeparator:
            assemble_content += "0 STEP" + "\n"
            pl_max = max(pl_max, len(pl_set))
            pl_set.clear()
        
        part_size = inst.findtext("Size").split(" * ")
        part_size = int(float(part_size[0]))
        
        position = inst.findtext("Position")     
        position = re.sub(r"[^\d\s]", "", position)
        position = position.split(" ")
        row, col = int(position[0]), int(position[1])
        part_definition = f"1 0 0 0 0 1 0 -1 0 {brick[part_size]}"
        brick_color = inst.findtext("Color")
        pl_set.add((brick_color, part_size))
        ldraw_command = f"1 {color[brick_color]} {col * 20 + offset[part_size]} 0 {row * 24} {part_definition}"               
        assemble_content += ldraw_command + "\n"
    
    pl_max = max(pl_max, len(pl_set))
    
    if width > 25:
        scale = (20 / width)
        scale = round(scale, 2)
        ldraw_file_content += f"0 !LPUB ASSEM MODEL_SCALE GLOBAL{scale: .4f}" + "\n"
    
    if pl_max > 6:
        ldraw_file_content += f"0 !LPUB PLI MODEL_SCALE GLOBAL{6 / pl_max: .4f}" + "\n"
        ldraw_file_content += f"0 !LPUB PLI INSTANCE_COUNT FONT \"Arial,{(int)(36 * 6 / pl_max)},-1,5,75,0,0,0,0,0,Bold\"\n"
    
    ldraw_file_content += assemble_content    
    
    return ldraw_file_content

def listToldraw(manual, height, width):
    ldraw_file_content = ""
    latitude, longitude = 45.0, 0.0
    ldraw_file_content = f"0 !LPUB ASSEM CAMERA_ANGLES {latitude}   {longitude}\n"
    
    assemble_content = ""
    pl_max = 0
    pl_set = set()
    
    if len(manual) == 0:
        return ldraw_file_content
    
    for entry in manual:
        if entry[-1] == -1:
            assemble_content += "0 STEP" + "\n"
            pl_max = max(pl_max, len(pl_set))
            pl_set.clear()
            continue
        part_size = entry[2]
        row, col = entry[0]
        part_definition = f"1 0 0 0 0 1 0 -1 0 {brick[part_size]}"
        brick_color = entry[1]
        pl_set.add((brick_color, part_size))
        ldraw_command = f"1 {color[brick_color]} {col * 20 + offset[part_size]} 0 {row * 24} {part_definition}"               
        assemble_content += ldraw_command + "\n"
    
    pl_max = max(pl_max, len(pl_set))
    
    if width > 25:
        scale = (20 / width)
        scale = round(scale, 2)
        ldraw_file_content += f"0 !LPUB ASSEM MODEL_SCALE GLOBAL{scale: .4f}" + "\n"
    
    if pl_max > 6:
        ldraw_file_content += f"0 !LPUB PLI MODEL_SCALE GLOBAL{6 / pl_max: .4f}" + "\n"
        ldraw_file_content += f"0 !LPUB PLI INSTANCE_COUNT FONT \"Arial,{(int)(36 * 6 / pl_max)},-1,5,75,0,0,0,0,0,Bold\"\n"
    
    ldraw_file_content += assemble_content
    return ldraw_file_content
    
def saveLdr(ldraw_file_content, dir):
    os.makedirs(dir, exist_ok=True)
    now = datetime.now()
    name = now.strftime('%Y-%m-%d_%H:%M:%S')
    dir = dir + '/' + name + '.ldr'
    with open(dir, 'wb') as f:
        f.write(ldraw_file_content.encode('utf-8'))    
    return dir