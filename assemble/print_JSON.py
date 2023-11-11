import json, os
from datetime import datetime
from brick_info import generate

def manualTodict(manual, height, width):
    instruction__list = list()
    discount = 0
    if len(manual) == 0:
        info_list = list()
        info_list.append(("Warning", "Manual is empty!"))
        info_dict = dict(info_list)
        instruction__list.append(info_dict)
    else:
        pageSeparate = list()

        for i, instruction in enumerate(manual):
            if instruction[2] == -1:
                pageSeparate.append(i + 1 - discount)
                discount = discount + 1
                continue

            instruction_tuple = list()
            instruction_tuple.append(("Sequence", i + 1 - discount))
            instruction_tuple.append(("Position", str(instruction[0])))
            instruction_tuple.append(("Color", instruction[1]))
            instruction_tuple.append(("Size", str(instruction[2]) + " * 1"))
            instruction_dict = dict(instruction_tuple)
            instruction__list.append(instruction_dict)
    manual_dict = {"Height" : height, "Width" : width, "Manual": instruction__list, "PageSeparator" : pageSeparate}
    return manual_dict

def saveTojson(brick, dir):
    manual, height, width = generate(brick)
    manual_dict = manualTodict(manual, height, width)
    os.makedirs(dir, exist_ok=True)
    now = datetime.now()
    name = now.strftime('%Y-%m-%d')
    dir = dir + '/' + name + '.json'
    with open(dir, 'w', encoding='utf-8') as f:
        json.dump(manual_dict, f, indent="\t")
        
    return dir