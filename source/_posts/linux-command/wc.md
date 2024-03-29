---
categories:
- Linux 命令
date: '2020-09-25 08:00:00'
tags:
- Linux
- Linux Command
- Linux 命令
- wc
title: 【Linux 命令】wc
updated: '2020-09-25 12:34:30'
---

统计文件的字节数、字数、行数

## 补充说明

**wc命令** 统计指定文件中的字节数、字数、行数，并将统计结果显示输出。利用wc指令我们可以计算文件的Byte数、字数或是列数，若不指定文件名称，或是所给予的文件名为“-”，则wc指令会从标准输入设备读取数据。wc同时也给出所指定文件的总统计数。

###  语法 

```shell
wc(选项)(参数)
wc [选项]... [文件]...
wc [选项]... --files0-from=F
```

###  选项 

```shell
-c # 统计字节数，或--bytes或——chars：只显示Bytes数；。
-l # 统计行数，或——lines：只显示列数；。
-m # 统计字符数。这个标志不能与 -c 标志一起使用。
-w # 统计字数，或——words：只显示字数。一个字被定义为由空白、跳格或换行字符分隔的字符串。
-L # 打印最长行的长度。
-help     # 显示帮助信息
--version # 显示版本信息
```

###  参数 

文件：需要统计的文件列表。

## 例子

```shell
wc -l *       # 统计当前目录下的所有文件行数及总计行数。
wc -l *.js    # 统计当前目录下的所有 .js 后缀的文件行数及总计行数。
find  . * | xargs wc -l # 当前目录以及子目录的所有文件行数及总计行数。
```

查看文件的字节数、字数、行数

```shell
wc test.txt
# 输出结果
7     8     70     test.txt
# 行数 单词数 字节数 文件名
```

用wc命令怎么做到只打印统计数字不打印文件名

```shell
wc -l < test.txt
# 输出结果
7
```

用来统计当前目录下的文件数(不包含隐藏文件)

```shell
# 要去除TOTAL行
expr $(ls -l | wc -l) - 1
# 输出结果
8
```

统计当前目录下的所有文件行数及总计行数

```shell
[root@centos7 ~]# wc -l *
      21 LICENSE
     270 README.md
wc: example: read: Is a directory
     785 lerna-debug.log
      25 lerna.json
wc: node_modules: read: Is a directory
   23603 package-lock.json
      79 package.json
       3 renovate.json
   24786 total
```


