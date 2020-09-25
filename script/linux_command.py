import yaml
import os

# 下载
# wget https://github.com/jaywcjlove/linux-command/archive/master.zip -O linux-command-master.zip
# unzip linux-command-master.zip
linux_command_dir = 'linux-command-master/command/'
for file in os.listdir(linux_command_dir):
    print('处理文件: ' + linux_command_dir + file)

    fin = open(linux_command_dir + file, 'r')
    content = fin.readlines()
    content = ''.join(content[2:])

    metadata = {}
    metadata['title'] = '【Linux 命令】'+os.path.splitext(file)[0]
    metadata['tags'] = ['Linux', 'Linux Command',
                        'Linux 命令', os.path.splitext(file)[0]]
    metadata['categories'] = ['Linux 命令']
    metadata_text = yaml.dump(data=metadata, allow_unicode=True)
    # print(metadata_text)

    content = '---\n' + metadata_text + '---\n' + content
    # print(content)
    fout = open('../source/_posts/linux-command/' + file, 'w')
    fout.write(content)
