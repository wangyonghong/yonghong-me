---
categories:
- Linux 命令
date: '2020-09-25 08:00:00'
tags:
- Linux
- Linux Command
- Linux 命令
- quotaoff
title: 【Linux 命令】quotaoff
updated: '2020-09-25 11:12:00'
---

关闭Linux内核中指定文件系统的磁盘配额功能

## 补充说明

**quotaoff命令** 用于关闭Linux内核中指定文件系统的磁盘配额功能。

###  语法

```shell
quotaoff(选项)(参数)
```

###  选项

```shell
-a：关闭在/etc/fstab文件里，有加入quota设置的分区的空间限制；
-g：关闭群组的磁盘空间限制；
-u：关闭用户的磁盘空间限制；
-v：显示指令执行过程。
```

###  参数

文件系统：指定要关闭磁盘配额功能的文件系统。


