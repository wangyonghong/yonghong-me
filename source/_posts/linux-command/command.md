---
categories:
- Linux 命令
date: '2020-09-25 08:00:00'
tags:
- Linux
- Linux Command
- Linux 命令
- command
title: 【Linux 命令】command
updated: '2020-09-25 08:36:30'
---

调用并执行指定的命令

## 补充说明

**command命令** 调用指定的指令并执行，命令执行时不查询shell函数。command命令只能够执行shell内部的命令。

###  语法

```shell
command(参数)
```

###  参数

指令：需要调用的指令及参数。

###  实例

使用command命令调用执行`echo Linux`，输入如下命令：

```shell
command echo Linux            #调用执行shell内部指令
```

上面的命令执行后，将调用执行命令`echo Linux`，其执行结果如下：

```shell
Linux
```


