import os


head_folder = ('my_project')
inside_folders = ('settings', 'mainapp', 'adminapp', 'authapp')
current_location = (os.path.dirname(os.path.abspath(__file__)))
my_project_location = os.path.join(current_location, 'my_project')
print(inside_folders)
try:
    if not os.path.exists(my_project_location) or \
            not os.path.exists(''.join([os.path.join(my_project_location, item) for item in inside_folders])):
        for inside_folders in inside_folders:
            os.makedirs(os.path.join(head_folder, inside_folders))
except Exception as e:
    print(f'{e.__class__.__name__} Поймали ошибку: {e}')
print('end')