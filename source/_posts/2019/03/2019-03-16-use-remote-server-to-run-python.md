---
layout: post
title:  "使用远程服务器运行 Python"
category: "Linux"
tags: ["Linux", "python", "Python", "linux", "conda", "anaconda"]
date: 2019-03-16 00:00:00
updated: 2018-03-16 00:00:00
---

首先有一台服务器，然后知道服务器的 IP，用户名，密码。本文以我的虚拟机为例子，IP 10.211.55.9，用户名 yh，密码 123456


<!-- more -->

### 登录

```shell
# ssh 用户名@IP
ssh yh@10.211.55.9
# 输入密码，即可登录到远程服务器
```

### Linux 常用命令

```shell
# 退出
exit
# 复制文件
cp file.txt 目录
# 移动文件
mv file.txt 目录
# 重命名
mv file.txt rename.txt
# 解压 zip
unzip file.zip
# 遇到中文乱码的情况加参数 -O GBK
unzip -O GBK file.zip
# 解压 tar tar.gz
tar -zxvf file.tar
# 安装 .deb 安装包
dpkg -i install.deb
```

### 传文件到远程服务器

```shell
# 在本地系统操作
# scp 文件名 远程服务器用户名@IP:目录（确保有这个目录，否则会创建为一个文件）
scp file.zip yh@10.211.55.9:/home/yh
# 上传一个文件夹
scp -r filesdir yh@10.211.55.9:/home/yh
```

### 使用 Python

#### 下载安装 anaconda

清华 [https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)

中科大 [https://mirrors.ustc.edu.cn/anaconda/archive/](https://mirrors.ustc.edu.cn/anaconda/archive/)

以目前最新的 anaconda 版本为例

```shell
# 下载
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.sh
# 添加可执行权限
chmod +x Anaconda3-5.3.1-Linux-x86_64.sh
# 安装
./Anaconda3-5.3.1-Linux-x86_64.sh
# 设置 Conda 国内源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```

#### Conda 的使用

```shell
# conda create -n 环境名称 python=3 包1 包2 包3 ...
conda create -n yhtf python=3 tensorflow numpy keras
# 激活环境
conda activate yhtf
# 取消环境
conda deactivate
# 安装 python 包
# conda install 包
conda install pillow
```

