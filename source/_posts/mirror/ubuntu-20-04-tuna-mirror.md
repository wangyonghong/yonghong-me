---
title: 【国内镜像】Ubuntu 20.04 LTS focal 清华镜像
categories:
- 国内镜像
tags:
- 国内镜像
- 镜像
- 镜像站
- tuna
- 清华
- 清华镜像
- mirror
- 国内源
- 清华源
- 开源
- 开源软件
- 开源软件镜像
- Ubuntu
- trusty
- Linux
date: 2020-09-28 08:00:00
updated: 2020-09-28 10:08:00
indexing: false
---

Ubuntu，是一款基于 Debian Linux 的以桌面应用为主的操作系统，内容涵盖文字处理、电子邮件、软件开发工具和 Web 服务等，可供用户免费下载、使用和分享。

## 替换镜像源


```txt /etc/apt/sources.list
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
```

<!-- more -->

## 恢复


```txt /etc/apt/sources.list
# See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to
# newer versions of the distribution.
deb http://archive.ubuntu.com/ubuntu/ focal main restricted
# deb-src http://archive.ubuntu.com/ubuntu/ focal main restricted

## Major bug fix updates produced after the final release of the
## distribution.
deb http://archive.ubuntu.com/ubuntu/ focal-updates main restricted
# deb-src http://archive.ubuntu.com/ubuntu/ focal-updates main restricted

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
## team. Also, please note that software in universe WILL NOT receive any
## review or updates from the Ubuntu security team.
deb http://archive.ubuntu.com/ubuntu/ focal universe
# deb-src http://archive.ubuntu.com/ubuntu/ focal universe
deb http://archive.ubuntu.com/ubuntu/ focal-updates universe
# deb-src http://archive.ubuntu.com/ubuntu/ focal-updates universe

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
## team, and may not be under a free licence. Please satisfy yourself as to
## your rights to use the software. Also, please note that software in
## multiverse WILL NOT receive any review or updates from the Ubuntu
## security team.
deb http://archive.ubuntu.com/ubuntu/ focal multiverse
# deb-src http://archive.ubuntu.com/ubuntu/ focal multiverse
deb http://archive.ubuntu.com/ubuntu/ focal-updates multiverse
# deb-src http://archive.ubuntu.com/ubuntu/ focal-updates multiverse

## N.B. software from this repository may not have been tested as
## extensively as that contained in the main release, although it includes
## newer versions of some applications which may provide useful features.
## Also, please note that software in backports WILL NOT receive any review
## or updates from the Ubuntu security team.
deb http://archive.ubuntu.com/ubuntu/ focal-backports main restricted universe multiverse
# deb-src http://archive.ubuntu.com/ubuntu/ focal-backports main restricted universe multiverse

## Uncomment the following two lines to add software from Canonical's
## 'partner' repository.
## This software is not part of Ubuntu, but is offered by Canonical and the
## respective vendors as a service to Ubuntu users.
# deb http://archive.canonical.com/ubuntu focal partner
# deb-src http://archive.canonical.com/ubuntu focal partner

deb http://security.ubuntu.com/ubuntu/ focal-security main restricted
# deb-src http://security.ubuntu.com/ubuntu/ focal-security main restricted
deb http://security.ubuntu.com/ubuntu/ focal-security universe
# deb-src http://security.ubuntu.com/ubuntu/ focal-security universe
deb http://security.ubuntu.com/ubuntu/ focal-security multiverse
# deb-src http://security.ubuntu.com/ubuntu/ focal-security multiverse
```

<!-- more -->

## 相关链接

- https://developer.aliyun.com/mirror/ubuntu
- https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/
- [【国内镜像】Ubuntu 14.04 LTS trusty 阿里云镜像](/mirror/ubuntu-14-04-aliyun-mirror/)
- [【国内镜像】Ubuntu 16.04 LTS xenial 阿里云镜像](/mirror/ubuntu-16-04-aliyun-mirror/)
- [【国内镜像】Ubuntu 18.04 LTS bionic 阿里云镜像](/mirror/ubuntu-18-04-aliyun-mirror/)
- [【国内镜像】Ubuntu 20.04 LTS focal 阿里云镜像](/mirror/ubuntu-20-04-aliyun-mirror/)
- [【国内镜像】Ubuntu 14.04 LTS trusty 清华镜像](/mirror/ubuntu-14-04-tuna-mirror/)
- [【国内镜像】Ubuntu 16.04 LTS xenial 清华镜像](/mirror/ubuntu-16-04-tuna-mirror/)
- [【国内镜像】Ubuntu 18.04 LTS bionic 清华镜像](/mirror/ubuntu-18-04-tuna-mirror/)
- [【国内镜像】Ubuntu 20.04 LTS focal 清华镜像](/mirror/ubuntu-20-04-tuna-mirror/)


