---
title: Java 进阶 05 —— JVM 相关工具
tags:
- Java进阶
- JVM
categories:
- Java进阶
date: 2021-06-11 21:00:00
updated: 2021-06-11 21:00:00
---

## JVM 命令行工具

| 工具 | 简介 |
| :--: | -- |
| java    | Java 应用的启动程序 |
| javac   | JDK 内置的编译工具 |
| javap   | 反编译 class 文件的工具 |
| javadoc | 根据 Java 代码和标准注释,自动生成相关的API说明文档 |
| javah   | JNI 开发时, 根据 java 代码生成需要的 .h文件。 |
| extcheck| 检查某个 jar 文件和运行时扩展 jar 有没有版本冲突，很少使用 |
| jdb     | Java Debugger ; 可以调试本地和远端程序, 属于 JPDA 中的一个 demo 实现, 供其他调试器参考。开发时很使用 |
| jdeps   | 探测 class 或 jar 包需要的依赖 |
| jar     | 打包工具，可以将文件和目录打包成为 .jar 文件；.jar 文件本质上就是 zip 文件, 只是后缀不同。使用时按顺序对应好选项和参数即可。 |
| keytool | 安全证书和密钥的管理工具; （支持生成、导入、导出等操作） |
| jarsigner   | JAR 文件签名和验证工具 |
| policytool  | 实际上这是一款图形界面工具, 管理本机的 Java 安全策略 |
| jps/jinfo | 查看 java 进程 |
| **jstat** | 查看 JVM 内部 gc 相关信息 |
| **jmap** | 查看 heap 或类占用空间统计 |
| **jstack** | 查看线程信息 |
| jcmd | 执行 JVM 相关分析命令（整合命令） |
| jrunscript/jjs | 执行 js 命令 |

<!-- more -->

### 常用命令实例

```shell
jps -l
jps -mlv 
# -l 列出 Java 进程
# -m 列出传递给 main 方法的参数
# -v 列出传递给 JVM 的参数

jinfo pid

# 参考：https://blog.csdn.net/maosijunzi/article/details/46049117
# jstat   内存信息
jstat -gc pid 1000 1000 # 每1000ms打印1次，打印1000次
S0C    S1C    S0U    S1U      EC       EU        OC         OU       MC     MU    CCSC   CCSU   YGC     YGCT    FGC    FGCT     GCT
4352.0 4352.0 4352.0  0.0   34944.0  10175.9   198132.0   152461.3  142132.0 134139.5 19624.0 16988.2     26    0.201   0      0.000    0.201
4352.0 4352.0 4352.0  0.0   34944.0  10175.9   198132.0   152461.3  142132.0 134139.5 19624.0 16988.2     26    0.201   0      0.000    0.201
4352.0 4352.0 4352.0  0.0   34944.0  10175.9   198132.0   152461.3  142132.0 134139.5 19624.0 16988.2     26    0.201   0      0.000    0.201
# S0C：第一个幸存区的大小
# S1C：第二个幸存区的大小
# S0U：第一个幸存区的使用大小
# S1U：第二个幸存区的使用大小
# EC：伊甸园区的大小
# EU：伊甸园区的使用大小
# OC：老年代大小
# OU：老年代使用大小
# MC：方法区大小
# MU：方法区使用大小
# CCSC：压缩类空间大小
# CCSU：压缩类空间使用大小
# YGC：年轻代垃圾回收次数
# YGCT：年轻代垃圾回收消耗时间
# FGC：老年代垃圾回收次数
# FGCT：老年代垃圾回收消耗时间
# GCT：垃圾回收消耗总时间

jstat -gcutil pid 1000 1000
  S0     S1     E      O      M     CCS    YGC     YGCT    FGC    FGCT     GCT
  0.00  79.37  72.86  78.50  94.45  86.65     27    0.207     0    0.000    0.207
  0.00  79.37  72.86  78.50  94.45  86.65     27    0.207     0    0.000    0.207
  0.00  79.37  72.86  78.50  94.45  86.65     27    0.207     0    0.000    0.207
# S0：幸存1区当前使用比例
# S1：幸存2区当前使用比例
# E：伊甸园区使用比例
# O：老年代使用比例
# M：元数据区使用比例
# CCS：压缩使用比例
# YGC：年轻代垃圾回收次数
# FGC：老年代垃圾回收次数
# FGCT：老年代垃圾回收消耗时间
# GCT：垃圾回收消耗总时间

# 只看 Young 或 Old 区
jstat -gcnew pid
jstat -gcold pid

# jmap    对象信息
jmap -heap pid      # 堆内存
jmap -histo pid     # 直方图

# jstack  线程信息
jstack -l pid       # 将线程相关的 locks 信息一起输 出，比如持有的锁，等待的锁。

# jcmd 综合了前面的几个命令
jcmd pid VM.version
jcmd pid VM.flags
jcmd pid VM.command_line
jcmd pid VM.system_properties
jcmd pid Thread.print
jcmd pid GC.class_histogram
jcmd pid GC.heap_info

# 当curl命令用
jrunscript -e "cat('http://www.baidu.com')" 
# 执行js脚本片段
jrunscript -e "print('hello,kk.jvm'+1)" 
# 执行js文件 
jrunscript -l js -f /XXX/XXX/test.js

```

## JVM 图形化工具

### jconsole

JDK 自带工具

![jconsole-内存](https://up-img.yonghong.tech/pic/2021/04/03-17-11-jconsole-mem-MJI7ul.png)
![jconsole-线程](https://up-img.yonghong.tech/pic/2021/04/03-17-12-jconsole-thread-b0RSWW.png)
![jconsole-概览](https://up-img.yonghong.tech/pic/2021/04/03-17-12-jconsole-guide-KgMCzE.png)

### jvisualvm

![jvisualvm](https://up-img.yonghong.tech/pic/2021/04/03-17-15-jvisualvm-guide-JU8yC7.png)

### VisualGC

![VisualGC](https://up-img.yonghong.tech/pic/2021/04/03-17-16-VisualGC-poZ5Sm.png)

### jmc

需要安装 Oracle JDK。

![jmc](https://up-img.yonghong.tech/pic/2021/04/03-17-16-jmc-yNni2V.png)
![jmc-1](https://up-img.yonghong.tech/pic/2021/04/03-17-16-jmc-1-5ultLq.png)
![jmc-2](https://up-img.yonghong.tech/pic/2021/04/03-17-16-jmc-2-gKxxpd.png)
![jmc-3](https://up-img.yonghong.tech/pic/2021/04/03-17-16-jmc-3-GleUio.png)
