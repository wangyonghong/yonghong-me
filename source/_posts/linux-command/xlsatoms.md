---
categories:
- Linux 命令
date: '2020-09-25 08:00:00'
tags:
- Linux
- Linux Command
- Linux 命令
- xlsatoms
title: 【Linux 命令】xlsatoms
updated: '2020-09-25 12:39:00'
indexing: false
---

列出X服务器内部所有定义的原子成分

## 补充说明

**xlsatoms命令** 用于列出X服务器内部所有定义的原子成分，每个原子成分都有自身的编号。可利用参数设置列表范围，或直接指定欲查询的成分名称。

###  语法

```shell
xlsatoms(选项)
```

###  选项

* -display<显示器编号>：指定X Server连接的显示器编号，该编号由"0"开始计算，依序递增；
* -format<输出格式>：设置成分清单的列表格式，您可使用控制字符改变显示样式；
* -name<成分名称>：列出指定的成分；
* -range<列表范围>：设置成分清单的列表范围。


<!-- Linux命令行搜索引擎：https://jaywcjlove.github.io/linux-command/ -->