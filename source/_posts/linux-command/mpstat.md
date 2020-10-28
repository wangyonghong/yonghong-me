---
categories:
- Linux 命令
date: '2020-09-25 08:00:00'
tags:
- Linux
- Linux Command
- Linux 命令
- mpstat
title: 【Linux 命令】mpstat
updated: '2020-09-25 10:34:30'
---

显示各个可用CPU的状态

## 补充说明

**mpstat命令** 指令主要用于多CPU环境下，它显示各个可用CPU的状态系你想。这些信息存放在`/proc/stat`文件中。在多CPUs系统里，其不但能查看所有CPU的平均状况信息，而且能够查看特定CPU的信息。

###  语法

```shell
mpstat(选项)(参数)
```

###  选项

```shell
-P：指定CPU编号。
```

###  参数

*   间隔时间：每次报告的间隔时间（秒）；
*   次数：显示报告的次数。

###  实例

当mpstat不带参数时，输出为从系统启动以来的平均值。

```shell
mpstat
Linux 2.6.9-5.31AXsmp (builder.redflag-linux.com) 12/16/2005
09:38:46 AM CPU %user %nice %system %iowait %irq %soft %idle intr/s
09:38:48 AM all 23.28 0.00 1.75     0.50 0.00 0.00 74.47 1018.59
```

 **每2秒产生了2个处理器的统计数据报告：** 

下面的命令可以每2秒产生了2个处理器的统计数据报告，一共产生三个interval 的信息，然后再给出这三个interval的平均信息。默认时，输出是按照CPU 号排序。第一个行给出了从系统引导以来的所有活跃数据。接下来每行对应一个处理器的活跃状态。。

```shell
mpstat -P ALL 2 3
Linux 2.6.18-164.el5 (server.sys.com)    01/04/2010
09:34:20 PM CPU   %user   %nice    %sys %iowait    %irq   %soft %steal   %idle    intr/s
09:34:22 PM all    0.00    0.00    0.00    0.00    0.00    0.00    0.00 100.00   1001.49
09:34:22 PM    0    0.00    0.00    0.50    0.00    0.00    0.00    0.00   99.50   1001.00
09:34:22 PM    1    0.00    0.00    0.00    0.00    0.00    0.00    0.00 100.00      0.00
```

 **比较带参数和不带参数的mpstat的结果：** 

在后台开一个2G的文件

```shell
cat 1.img &
```

然后在另一个终端运行mpstat命令

```shell
mpstat
Linux 2.6.18-164.el5 (server.sys.com)    01/04/2010
10:17:31 PM CPU   %user   %nice    %sys %iowait    %irq   %soft %steal   %idle    intr/s
10:17:31 PM all    0.07    0.02    0.25    0.21    0.01    0.04    0.00   99.40   1004.57
```

```shell
mpstat
Linux 2.6.18-164.el5 (server.sys.com)    01/04/2010
10:17:35 PM CPU   %user   %nice    %sys %iowait    %irq   %soft %steal   %idle    intr/s
10:17:35 PM all    0.07    0.02    0.25    0.21    0.01    0.04    0.00   99.39   1004.73
```

```shell
mpstat 3 10
Linux 2.6.18-164.el5 (server.sys.com)    01/04/2010
10:17:55 PM CPU   %user   %nice    %sys %iowait    %irq   %soft %steal   %idle    intr/s
10:17:58 PM all   13.12    0.00   20.93    0.00    1.83    9.80    0.00   54.32   2488.08
10:18:01 PM all   10.82    0.00   19.30    0.83    1.83    9.32    0.00   57.90   2449.83
10:18:04 PM all   10.95    0.00   20.40    0.17    1.99    8.62    0.00   57.88   2384.05
10:18:07 PM all   10.47    0.00   18.11    0.00    1.50    8.47    0.00   61.46   2416.00
10:18:10 PM all   11.81    0.00   22.63    0.00    1.83   11.98    0.00   51.75   2210.60
10:18:13 PM all    6.31    0.00   10.80    0.00    1.00    5.32    0.00   76.58   1795.33
10:18:19 PM all    1.75    0.00    3.16    0.75    0.25    1.25    0.00   92.85   1245.18
10:18:22 PM all   11.94    0.00   19.07    0.00    1.99    8.29    0.00   58.71   2630.46
10:18:25 PM all   11.65    0.00   19.30    0.50    2.00    9.15    0.00   57.40   2673.91
10:18:28 PM all   11.44    0.00   21.06    0.33    1.99   10.61    0.00   54.56   2369.87
Average:     all    9.27    0.00   16.18    0.30    1.50    7.64    0.00   65.11   2173.54
```

上两表显示出当要正确反映系统的情况，需要正确使用命令的参数。vmstat 和iostat 也需要注意这一问题。


<!-- Linux命令行搜索引擎：https://jaywcjlove.github.io/linux-command/ -->