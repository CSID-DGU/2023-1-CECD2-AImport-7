import subprocess, os
from datetime import datetime
   
def Save_manual(form, dir, ldr_file):
    os.makedirs(dir, exist_ok=True)
    now = datetime.now()
    name = now.strftime('%Y-%m-%d_%H:%M:%S')
    file_name = name + '.' + form
         
    command = f'lpub3d --line-width 3 -o {form} -od {dir} -of {file_name} -pe {ldr_file}'
    subprocess.run(command, shell=True)