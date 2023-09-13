import json, os

def manualTodict(manual):
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

def saveTojson(manual, dir, name):
    manual_dict = manualTodict(manual)
    abs_dir = str(os.getcwd()) + '/' + dir + '/'
    os.makedirs(abs_dir, exist_ok=True)
    abs_dir = abs_dir + '/' + name + '.json'
    with open(abs_dir, 'w', encoding='utf-8') as f:
        json.dump(manual_dict, f, indent="\t")
        
    return abs_dir