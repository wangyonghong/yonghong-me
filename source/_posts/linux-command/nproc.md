---
categories:
- Linux 命令
date: '2020-09-25 08:00:00'
tags:
- Linux
- Linux Command
- Linux 命令
- nproc
title: 【Linux 命令】nproc
updated: '2020-09-25 10:48:00'
---

打印可用的处理器单元数量。

## 概要

```shell
nproc [OPTION]...
```

## 主要用途

- 打印可用的处理器单元数量。

## 选项

```shell
--all         打印已安装处理器的数量。
--ignore=N    如果可以的情况下，排除 N 个处理单元。
--help        显示帮助信息并退出。
--version     显示版本信息并退出。
```

## 例子

```shell
[root@localhost ~]# nproc
8
```

### 注意

1. 该命令是`GNU coreutils`包中的命令，相关的帮助信息请查看`man -s 1 nproc`，`info coreutils 'nproc invocation'`。


