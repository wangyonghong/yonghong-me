---
categories:
- Linux 命令
date: '2020-09-25 08:00:00'
tags:
- Linux
- Linux Command
- Linux 命令
- rpm2cpio
title: 【Linux 命令】rpm2cpio
updated: '2020-09-25 11:23:00'
---

将RPM软件包转换为cpio格式的文件

## 补充说明

**rpm2cpio命令** 用于将rpm软件包转换为cpio格式的文件。

###  语法

```shell
rpm2cpio(参数)
```

###  参数

文件：指定要转换的rpm包的文件名。

###  实例

```shell
rpm2cpio ../libstdc++-4.3.0-8.i386.rpm | cpio -idv
```


<!-- Linux命令行搜索引擎：https://jaywcjlove.github.io/linux-command/ -->