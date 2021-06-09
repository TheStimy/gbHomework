import yaml
import os

with open('config.yaml') as f:
    f_structure = yaml.safe_load(f)


def path_func(data, path=''):
    for main_dir, sub_elements in data.items():
        dir_path = os.path.join(path, main_dir)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        if isinstance(sub_elements, dict):
            path_func(sub_elements, dir_path)
        else:
            for el in sub_elements:
                if isinstance(el, dict):
                    path_func(el, dir_path)
                elif isinstance(el, str):
                    with open(os.path.join(dir_path, f'{el}'), 'w') as _:
                        pass


path_func(f_structure)
