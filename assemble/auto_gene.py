import assemble.brick_info as brick_info
import assemble.print_LDR as print_LDR
import assemble.convert as convert

def pixelTomanual(brick, save_ldraw_dir, save_manual_dir, save_manual_form):
    instruction, height, width = brick_info.generate(brick)
    ldraw_content = print_LDR.listToldraw(instruction)
    ldr_dir = print_LDR.saveLdr(ldraw_content, save_ldraw_dir)
    convert.Save_manual(save_manual_form, save_manual_dir, ldr_dir)
    
def jsonTomanual(json_dir, save_ldraw_dir, save_manual_dir, save_manual_form):
    ldraw_content = print_LDR.jsonToldraw(json_dir)
    ldr_dir = print_LDR.saveLdr(ldraw_content, save_ldraw_dir)
    convert.Save_manual(save_manual_form, save_manual_dir, ldr_dir)
    
def xmlTomanual(xml_dir, save_ldraw_dir, save_manual_dir, save_manual_form):
    ldraw_content = print_LDR.xmlToldraw(xml_dir)
    ldr_dir = print_LDR.saveLdr(ldraw_content, save_ldraw_dir)
    convert.Save_manual(save_manual_form, save_manual_dir, ldr_dir)
    
def make_manual(input_form, input_dir, save_ldraw_dir, save_manual_dir, save_manual_form):
    ldr_absdir = print_LDR.saveLdr(print_LDR.convertToldr(input_form, input_dir), save_ldraw_dir)
    convert.Save_manual(save_manual_form, save_manual_dir, ldr_absdir)