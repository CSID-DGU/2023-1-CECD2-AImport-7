import brick_info, print_LDR, convert

def pixelTomanual(brick, save_ldraw_dir, save_ldraw_name, save_manual_dir, save_manual_form, save_manual_name):
    instruction = brick_info.generate(brick)
    ldraw_content = print_LDR.listToldraw(instruction, save_ldraw_name)
    ldr_dir = print_LDR.saveLdr(ldraw_content, save_ldraw_dir, save_ldraw_name)
    convert.Save_manual(save_manual_form, save_manual_dir, save_manual_name, ldr_dir)
    
def jsonTomanual(json_dir, save_ldraw_dir, save_ldraw_name, save_manual_dir, save_manual_form, save_manual_name):
    ldraw_content = print_LDR.jsonToldraw(json_dir, save_ldraw_name)
    ldr_dir = print_LDR.saveLdr(ldraw_content, save_ldraw_dir, save_ldraw_name)
    convert.Save_manual(save_manual_form, save_manual_dir, save_manual_name, ldr_dir)
    
def xmlTomanual(xml_dir, save_ldraw_dir, save_ldraw_name, save_manual_dir, save_manual_form, save_manual_name):
    ldraw_content = print_LDR.xmlToldraw(xml_dir, save_ldraw_name)
    ldr_dir = print_LDR.saveLdr(ldraw_content, save_ldraw_dir, save_ldraw_name)
    convert.Save_manual(save_manual_form, save_manual_dir, save_manual_name, ldr_dir)