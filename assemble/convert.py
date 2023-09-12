import subprocess
import os

class Convert:
    def __init__(self):
        self.input_file = ""
        
    def Load_ldr(self, input):
        self.input_file = input
    
    def Save_manual(self, form, dir, name):
        if self.input_file == None:
            return
        
        file_name = name + '.' + form
        os.makedirs("/home/kocan/" + dir, exist_ok=True)
        dir = "/home/kocan/" + dir + '/'
        command = f'lpub3d24 -pe -o {form} -od {dir} -of {file_name} {self.input_file}'
        subprocess.run(command, shell=True)
        
c = Convert()
c.Load_ldr("manual.ldr")
c.Save_manual("pdf", "manual", "manual")

