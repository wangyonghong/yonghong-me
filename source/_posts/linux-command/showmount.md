---
categories:
- Linux 命令
date: '2020-09-25 08:00:00'
tags:
- Linux
- Linux Command
- Linux 命令
- showmount
title: 【Linux 命令】showmount
updated: '2020-09-25 11:37:30'
indexing: false
---

显示NFS服务器加载的信息

## 补充说明

**showmount命令** 查询“mountd”守护进程，以显示NFS服务器加载的信息。

###  语法

```shell
showmount(选项)(参数)
```

###  选项

```shell
-d：仅显示已被NFS客户端加载的目录；
-e：显示NFS服务器上所有的共享目录。
```

###  参数

NFS服务器：指定NFS服务器的ip地址或者主机名。


<!-- Linux命令行搜索引擎：https://jaywcjlove.github.io/linux-command/ -->