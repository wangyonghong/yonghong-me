---
categories:
- Linux 命令
date: '2020-09-25 08:00:00'
tags:
- Linux
- Linux Command
- Linux 命令
- nm
title: 【Linux 命令】nm
updated: '2020-09-25 10:44:30'
---

显示二进制目标文件的符号表

## 补充说明

**nm命令** 被用于显示二进制目标文件的符号表。

###  语法

```shell
nm(选项)(参数)
```

###  选项

```shell
-A：每个符号前显示文件名；
-D：显示动态符号；
-g：仅显示外部符号；
-r：反序显示符号表。
```

###  参数

目标文件：二进制目标文件，通常是库文件和可执行文件。


<!-- Linux命令行搜索引擎：https://jaywcjlove.github.io/linux-command/ -->