import os
import shutil

from_dir = "\Descargas"
to_dir = '\Users\danny\OneDrive\Documentos\programacion\Documentos_Archivos'

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

# Profe no se que mas haceer, estoy confundida con este proyecto