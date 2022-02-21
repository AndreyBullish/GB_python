import os


if __name__ == "__main__":
    head_folder = ('my_project')
    inside_folders = ('settings', 'mainapp', 'adminapp', 'authapp')
    current_location = (os.path.dirname(os.path.abspath(__file__)))
    dir_name = 'my_project'
    if not os.path.exists(dir_name):
        for dir1 in inside_folders:
                os.makedirs(os.path.join(head_folder, dir1))

print('end')