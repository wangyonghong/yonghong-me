---
categories:
- Linux 命令
date: '2020-09-25 08:00:00'
tags:
- Linux
- Linux Command
- Linux 命令
- uuto
title: 【Linux 命令】uuto
updated: '2020-09-25 12:25:30'
---

将文件传送到远端的UUCP主机

## 补充说明

**uuto命令** 为script文件，它实际上会执行uucp，用来将文件传送到远端UUCP主机，并在完成工作后，以邮件通知远端主机上的用户。

###  语法

```shell
uuto [文件][目的]
```


### 例子

将文件传送到远程 UUCP 主机 localhost 的 tmp 目录，在命令提示符中直接输入如下命令：

```shell
uuto./testfile localhost/tmp # 将文件传送到远程UUCP 主机localhost的tmp目录 
```

该命令通常没有输出。

