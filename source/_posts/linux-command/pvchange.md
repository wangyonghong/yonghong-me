---
categories:
- Linux 命令
date: '2020-09-25 08:00:00'
tags:
- Linux
- Linux Command
- Linux 命令
- pvchange
title: 【Linux 命令】pvchange
updated: '2020-09-25 11:05:30'
---

修改物理卷属性

## 补充说明

**pvchange命令** 允许管理员改变物理卷的分配许可。如果物理卷出现故障，可以使用pvchange命令禁止分配物理卷上的PE。

### 语法

```shell
pvchange(选项)(参数)
```

### 选项

```shell
-u：生成新的UUID；
-x：是否允许分配PE。
```

### 参数

物理卷：指定要修改属性的物理卷所对应的设备文件。

### 实例

使用pvchange命令禁止分配指定物理卷上的PE。在命令行中输入下面的命令：

```shell
pvchange -x n /dev/sdb1     #禁止分配"/dev/sdb1"上的PE
```

输出信息如下：

```shell
Physical volume "/dev/sdb1" changed  
1 physical volume changed / 0 physical volumes not changed
```


