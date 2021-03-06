#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import yaml
import os
import requests
import zipfile
import shutil

linux_command_zip = 'linux-command-master.zip'
linux_command_unzip = 'linux-command-master/'
linux_command_dir = 'linux-command-master/command/'
try:
    os.remove(linux_command_zip)
except:
    pass

try:
    shutil.rmtree(linux_command_unzip)
except:
    pass

# download
url = 'https://github.com/jaywcjlove/linux-command/archive/master.zip'
r = requests.get(url)
with open(linux_command_zip, 'wb') as f:
    f.write(r.content)
# unzip
fz = zipfile.ZipFile(linux_command_zip, 'r')
for file in fz.namelist():
    fz.extract(file, './')

create_time = "2020-09-25 08:00:00"
update_time = time.mktime(time.strptime(create_time, '%Y-%m-%d %H:%M:%S'))
file_list = os.listdir(linux_command_dir)
file_list.sort()
for file in file_list:
    print('处理文件: ' + linux_command_dir + file)

    fin = open(linux_command_dir + file, 'r')
    content = fin.readlines()
    content = ''.join(content[2:])

    metadata = {}
    metadata['title'] = '【Linux 命令】'+os.path.splitext(file)[0]
    metadata['tags'] = ['Linux', 'Linux Command',
                        'Linux 命令', os.path.splitext(file)[0]]
    metadata['categories'] = ['Linux 命令']
    metadata['date'] = create_time
    update_time = update_time + 30
    metadata['updated'] = time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime(update_time))
    metadata_text = yaml.dump(data=metadata, allow_unicode=True)
    # print(metadata_text)

    content = '---\n' + metadata_text + '---\n' + content
    # print(content)
    fout = open('../source/_posts/linux-command/' + file, 'w')
    fout.write(content)

try:
    os.remove(linux_command_zip)
except:
    pass

try:
    shutil.rmtree(linux_command_unzip)
except:
    pass
