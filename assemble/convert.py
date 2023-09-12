import subprocess
import os

class Convert:
    def __init__(self):
        self.input_file = ""
        
    def Load_ldr(self, input):
        self.input_file = str(os.getcwd()) + '/' + input
    
    def Save_manual(self, form, dir, name):
        if self.input_file == None:
            return
        
        abs_dir = str(os.getcwd()) + '/' + dir + '/'
        os.makedirs(abs_dir, exist_ok=True)
        file_name = abs_dir + name + '.' + form        
        command = f'lpub3d24 -pe -o {form} -od {abs_dir} -of {file_name} --viewpoint top {self.input_file}'
        subprocess.run(command, shell=True)
        
c = Convert()
c.Load_ldr("manual.ldr")
c.Save_manual("pdf", "manual", "manual")

