---
title: hg clone 与 Mercurial
tags:
- hg
- Mercurial
categories:
- 版本控制
date: 2021-01-06 22:24:00
updated: 2021-01-06 22:24:00
---

Mercurial是跨平台的分布式版本控制软件，主要由Python语言实现，但也包含用C语言实现的二进制比较工具。Mercurial一开始的主要运行平台是Linux，现在Mercurial已经移植到Windows、Mac OS X和大多数的类Unix系统中。Mercurial主要由命令行程序组成，现在也有了图形用户界面。对Mercurial的所有操作都由用不同的关键字作为参数调用程序“hg”来实现，Hg是参考水银的化学符号而取的名字。

Mercurial的主要设计目标包括高性能、可扩展性、分散性、完全分布式合作开发、能同时高效地处理纯文本和二进制文件，以及分支和合并功能，以此同时保持系统的简洁性[1]。Mercurial也包括一个集成的Web界面。

Mercurial的创建者和主要开发人员是Matt Mackal。其源代码采用GNU通用公共许可证第二版为授权，确保了Mercurial是一个自由软件。

<!-- more -->

## 获取 Mercurial

Mercurial 官方网站：https://www.mercurial-scm.org/

我们可以从官方网站上获取到软件安装包：https://www.mercurial-scm.org/downloads

还可以根据系统选择合适安装方式安装命令行工具：

```
# Debian/Ubuntu
$ apt-get install mercurial

# Fedora
$ dnf install mercurial

# Gentoo
$ emerge mercurial

# Mac OS (homebrew)
$ brew install mercurial

# FreeBSD
$ cd /usr/ports/devel/mercurial
$ make install

# Solaris 11 Express
$ pkg install SUNWmercurial
```

## 使用 hg 命令行工具 clone 软件仓库

比如 OpenJDK 的软件仓库：

```
hg clone https://hg.openjdk.java.net/jdk/jdk11
```