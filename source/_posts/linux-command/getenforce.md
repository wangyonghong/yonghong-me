---
categories:
- Linux 命令
date: '2020-09-25 08:00:00'
tags:
- Linux
- Linux Command
- Linux 命令
- getenforce
title: 【Linux 命令】getenforce
updated: '2020-09-25 09:24:00'
indexing: false
---

显示当前SELinux的应用模式，是强制、执行还是停用

## 补充说明

**grename命令** 可以重命名卷组的名称。

###  语法

```shell
getenforce
```

### 例子

查看当前SELinux的应用模式。

```shell
[root@localhost ~]# getenforce
Enforcing
```

<!-- Linux命令行搜索引擎：https://jaywcjlove.github.io/linux-command/ -->
