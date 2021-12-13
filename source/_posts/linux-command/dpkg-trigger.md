---
categories:
- Linux 命令
date: '2020-09-25 08:00:00'
tags:
- Linux
- Linux Command
- Linux 命令
- dpkg-trigger
title: 【Linux 命令】dpkg-trigger
updated: '2020-09-25 08:58:00'
---

Debian Linux下的软件包触发器

## 补充说明

**dpkg-trigger命令** 是Debian Linux下的软件包触发器。

###  语法

```shell
dpkg-trigger(选项)(参数)
```

###  选项

```shell
--check-supported：检查运行的dpkg是否支持触发器，返回值为0，则支持触发器。
--help：显示帮助信息；
--admindir=<目录>：设置dpkg数据库所在的目录；
--no-act：仅用于测试，不执行任何操作；
--by-package=<软件包>：覆盖触发器等待者。
```

###  参数

触发器名：指定触发器名称。


