---
title: 【国内镜像】Alpine 3.11 清华镜像
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
- Alpine
- Linux
date: 2020-09-28 08:00:00
updated: 2020-09-28 08:04:00
indexing: false
---

Alpine Linux是一个由社区开发的Linux操作系统，该操作系统以安全为理念，面向x86路由器、防火墙、虚拟专用网、IP电话盒及服务器而设计。

Alpine Linux is a security-oriented, lightweight Linux distribution based on musl libc and busybox.

## 替换镜像源

使用sed命令替换

```shell
sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories
```

<!-- more -->

或者使用下面文本替换

```txt /etc/apk/repositories
http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.11/main
http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.11/community
```

## 恢复

```txt /etc/apk/repositories
http://dl-cdn.alpinelinux.org/alpine/v3.11/main
http://dl-cdn.alpinelinux.org/alpine/v3.11/community
```

## 相关链接

- https://developer.aliyun.com/mirror/alpine
- https://mirrors.tuna.tsinghua.edu.cn/help/alpine/
- [【国内镜像】Alpine 3.10 阿里云镜像](/mirror/alpine-3-10-aliyun-mirror/)
- [【国内镜像】Alpine 3.11 阿里云镜像](/mirror/alpine-3-11-aliyun-mirror/)
- [【国内镜像】Alpine 3.12 阿里云镜像](/mirror/alpine-3-12-aliyun-mirror/)
- [【国内镜像】Alpine 3.10 清华镜像](/mirror/alpine-3-10-tuna-mirror/)
- [【国内镜像】Alpine 3.11 清华镜像](/mirror/alpine-3-11-tuna-mirror/)
- [【国内镜像】Alpine 3.12 清华镜像](/mirror/alpine-3-12-tuna-mirror/)