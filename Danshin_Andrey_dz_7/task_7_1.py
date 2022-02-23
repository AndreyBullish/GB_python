import os
#ИЗМЕНИЛ НАЗВАНИЕ ПАПКИ MY_PROJECT ЧТОБЫ ВСЕ РАБОТАЛО И НЕ ПЕРЕСИКАЛОСЬ С TASK_3

head_folder = ('my_project_first')
list_inside_folders = ('settings', 'mainapp', 'adminapp', 'authapp')

def func_creat_my_project(location):
    current_location = location
    my_project_location = os.path.join(current_location, head_folder)
    try:
        if not os.path.exists(my_project_location) or \
                not os.path.exists(''.join([os.path.join(my_project_location, item) for item in list_inside_folders])):
            for inside_folders in list_inside_folders:
                os.makedirs(os.path.join(head_folder, inside_folders))
    except Exception as e:
        print(f'{e.__class__.__name__} Поймали ошибку: {e}')

func_creat_my_project(__file__)

print('end')