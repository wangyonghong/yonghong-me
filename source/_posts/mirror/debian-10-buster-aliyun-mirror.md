---
title: 【国内镜像】Debian 10 buster 阿里云镜像
categories:
- 国内镜像
tags:
- 国内镜像
- 镜像
- 镜像站
- aliyun
- 阿里
- 阿里云
- 阿里云镜像
- mirror
- 国内源
- 阿里源
- 开源
- 开源软件
- 开源软件镜像
- Debian
- buster
- Linux
date: 2020-09-28 08:00:00
updated: 2020-09-28 09:05:00
indexing: false
---

Debian 是一个自由的操作系统（OS），提供您安装在计算机上使用。操作系统就是能让您的计算机工作的一系列基本程序和实用工具。

Debian 不只是提供一个纯粹的操作系统：它还附带了超过 59000 个软件包，这些预先编译好的软件被打包成一种良好的格式以便于在您的机器上进行安装。

## 替换镜像源

```txt /etc/apt/sources.list
deb http://mirrors.aliyun.com/debian/ buster main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster main non-free contrib
deb http://mirrors.aliyun.com/debian-security buster/updates main
deb-src http://mirrors.aliyun.com/debian-security buster/updates main
deb http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib
deb http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib
```

<!-- more -->

## 恢复

```txt /etc/apt/sources.list
deb http://deb.debian.org/debian stretch main
deb http://security.debian.org/debian-security stretch/updates main
deb http://deb.debian.org/debian stretch-updates main
deb http://deb.debian.org/debian buster main
deb http://security.debian.org/debian-security buster/updates main
deb http://deb.debian.org/debian buster-updates main
```

## 相关链接

- https://developer.aliyun.com/mirror/debian
- https://mirrors.tuna.tsinghua.edu.cn/help/debian/
- [【国内镜像】Debian 8 jessie 阿里云镜像](/mirror/debian-8-jessie-aliyun-mirror/)
- [【国内镜像】Debian 9 stretch 阿里云镜像](/mirror/debian-9-stretch-aliyun-mirror/)
- [【国内镜像】Debian 10 buster 阿里云镜像](/mirror/debian-10-buster-aliyun-mirror/)
- [【国内镜像】Debian 8 jessie 清华镜像](/mirror/debian-8-jessie-tuna-mirror/)
- [【国内镜像】Debian 9 stretch 清华镜像](/mirror/debian-9-stretch-tuna-mirror/)
- [【国内镜像】Debian 10 buster 清华镜像](/mirror/debian-10-buster-tuna-mirror/)
