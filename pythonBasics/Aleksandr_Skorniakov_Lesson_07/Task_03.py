import os
import shutil

src_dir, template = 'my_project', 'templates'
for root, dirs, files in os.walk(src_dir):
    if root != src_dir and template in dirs:
        for pre_dir in os.scandir(os.path.join(root, template)):
            shutil.copytree(os.path.join(root, template, pre_dir.name),
                            os.path.join(src_dir, template, pre_dir.name))
