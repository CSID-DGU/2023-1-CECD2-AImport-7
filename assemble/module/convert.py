import subprocess
import os
   
def Save_manual(form, dir, name, ldr_file):
    abs_dir = str(os.getcwd()) + '/' + dir + '/'
    os.makedirs(abs_dir, exist_ok=True)
    file_name = abs_dir + name + '.' + form        
    command = f'lpub3d24 --viewpoint top -o {form} -od {abs_dir} -of {file_name} -pe {ldr_file}'
    subprocess.run(command, shell=True)

