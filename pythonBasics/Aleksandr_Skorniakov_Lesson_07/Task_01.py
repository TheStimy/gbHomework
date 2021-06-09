import os

f_structure = {
    'my_project': {
        'settings',
        'mainapp',
        'adminapp',
        'authapp'
    }
}

for main_folder, sub_folder in f_structure.items():
    if not os.path.exists(main_folder):
        os.mkdir(main_folder)
    for folder in sub_folder:
        dir_path = os.path.join(main_folder, folder)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
