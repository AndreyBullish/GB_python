import os
import shutil
import sys
from shutil import copy2


current_location = (__file__)
parent_dir = os.path.dirname(current_location)
my_project_location = os.path.join(parent_dir, 'my_project')
templates_folder = os.path.join(my_project_location, 'templates')  # задаем путь до папки 'templates'
try:
    if not os.path.exists(templates_folder):
        os.makedirs(templates_folder)
except Exception as e:
    print(f'{e.__class__.__name__} Поймали ошибку: {e}')
if not os.path.exists(my_project_location):
    print(f'Директория {my_project_location} не сущетсвует')
    sys.exit(1)
else:
    try:
        for root, dirs, files in os.walk(my_project_location):
            if files:
                for f_name in files:
                    if f_name.endswith('.html'):
                        file_path = os.path.join(root, f_name) #текущий путь до html файлов
                        new_path = os.path.join(templates_folder, os.path.basename(root), f_name) #новый путь до html файлов
                        os.makedirs(os.path.dirname(new_path), exist_ok=True) #поднимаемся на дир. выше и создаем папки по новому пути
                        copy2(file_path, new_path)
    except (shutil.SameFileError, FileExistsError):
        if new_path == file_path:
            pass





# html_files = [os.path.join(current_folder, item) for item in os.listdir(current_folder) if item.endswith('txt')]