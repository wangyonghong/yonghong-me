---
categories:
- macOS 命令
date: '2021-03-29 20:00:00'
tags:
- macOS 命令
title: 【macOS 命令】scutil
updated: '2021-03-29 20:00:00'
---

管理系统配置参数。

## 用法

对系统的用户名和主机名进行修改

- ComputerName 就是电脑名称，给人看的（在下图中，电脑名称）
- HostName 主机名，但通常不会设置这个值
- LocalHostName 主机名，和 Linux 系统的 hostname 一样（在下图中，本地网络中电脑名称）

<!-- more -->

![电脑名称、主机名设置](https://up-img.yonghong.tech/pic/2021/03/29-20-27-%E6%88%AA%E5%B1%8F2021-03-29%20%E4%B8%8B%E5%8D%888.27.22-EnugWj.png)

hostname 命令取值的顺序：

- hostname 命令设置的值
- HostName 属性值
- LocalHostName 属性值（通常系统都会设置此属性）

```shell
# 查看系统主机名
$ scutil --get ComputerName
$ scutil --get HostName
$ scutil --get LocalHostName
# 修改系统主机名
$ scutil --set ComputerName xxx
$ scutil --set HostName xxx
$ scutil --set LocalHostName xxx
```

查看 DNS 配置信息

```shell
$ scutil --dns
```

查看代理信息

```shell
$ scutil --proxy
```

查看网络信息（ipv4/ipv6）

```shell
$ scutil --nwi
```





