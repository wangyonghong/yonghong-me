---
categories:
- Linux 命令
date: '2020-09-25 08:00:00'
tags:
- Linux
- Linux Command
- Linux 命令
- xlsfonts
title: 【Linux 命令】xlsfonts
updated: '2020-09-25 12:42:00'
---

列出X Server使用的字体

## 补充说明

**xlsfonts命令** 列出X Server使用的字体，也能使用范本样式仅列出的符合条件的字体。

###  语法

```shell
xlsfonts(选项)
```

###  选项

```shell
-l：除字体名称外，同时列出字体的属性；
-ll：此参数的效果和指定"l"参数类似，但显示更详细的信息；
-lll：此参数的效果和指定"ll"参数类似，但显示更详细的信息；
-m：配合参数"-l"使用时，一并列出字体大小的上下限；
-n<显示栏位数>：设置每列显示的栏位数；
-o：以OpenFont的形式列出字体清单；
-u：列出字体清单时不依照其名称排序；
-w<每列字符数>：设置每列的最大字符数。
```


