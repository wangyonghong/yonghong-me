---
layout: post
title:  "macOS Python 的版本管理"
category: "macOS"
tags: ["macOS", "Python"]
date: 2018-11-19 00:00:00
updated: 2018-11-19 00:00:00
---

用上 mac 后，发现装软件都变得简单了许多，要么是 App Store 中直接安装，要么是直接拖进 Application 文件夹。还可以用 brew 这样的工具装一些开发用的软件。

但是问题也是有的，这样装了很多软件之后，自己也不知道装到哪了。

<!-- more -->

比如 Python，打开自己的 /usr/local/bin 之后发现一堆 Python 的软链接。还有 /System/Library/Frameworks/Python.framework/Versions 这个目录下面也有很多。可能还用了 pyenv 这个管理 Python 版本的工具。

我们一个一个开始分析 

```shell
$ ls -l /usr/local/bin | grep python 
lrwxr-xr-x  1 WYH   admin        31 Nov 19 14:23 2to3 -> ../Cellar/python/3.7.1/bin/2to3
lrwxr-xr-x  1 WYH   admin        38 Nov 19 14:22 2to3-2 -> ../Cellar/python@2/2.7.15_1/bin/2to3-2
lrwxr-xr-x  1 WYH   admin        40 Nov 19 14:22 2to3-2.7 -> ../Cellar/python@2/2.7.15_1/bin/2to3-2.7
lrwxr-xr-x  1 WYH   admin        35 Nov 19 14:23 2to3-3.7 -> ../Cellar/python/3.7.1/bin/2to3-3.7
lrwxr-xr-x  1 WYH   admin        44 Nov 19 14:22 easy_install -> ../Cellar/python@2/2.7.15_1/bin/easy_install
lrwxr-xr-x  1 WYH   admin        48 Nov 19 14:22 easy_install-2.7 -> ../Cellar/python@2/2.7.15_1/bin/easy_install-2.7
lrwxr-xr-x  1 WYH   admin        43 Nov 19 14:23 easy_install-3.7 -> ../Cellar/python/3.7.1/bin/easy_install-3.7
lrwxr-xr-x  1 WYH   admin        36 Nov 19 14:22 idle -> ../Cellar/python@2/2.7.15_1/bin/idle
lrwxr-xr-x  1 WYH   admin        37 Nov 19 14:22 idle2 -> ../Cellar/python@2/2.7.15_1/bin/idle2
lrwxr-xr-x  1 WYH   admin        39 Nov 19 14:22 idle2.7 -> ../Cellar/python@2/2.7.15_1/bin/idle2.7
lrwxr-xr-x  1 WYH   admin        32 Nov 19 14:23 idle3 -> ../Cellar/python/3.7.1/bin/idle3
lrwxr-xr-x  1 WYH   admin        34 Nov 19 14:23 idle3.7 -> ../Cellar/python/3.7.1/bin/idle3.7
lrwxr-xr-x  1 WYH   admin        35 Nov 19 14:22 pip -> ../Cellar/python@2/2.7.15_1/bin/pip
lrwxr-xr-x  1 WYH   admin        36 Nov 19 14:22 pip2 -> ../Cellar/python@2/2.7.15_1/bin/pip2
lrwxr-xr-x  1 WYH   admin        38 Nov 19 14:22 pip2.7 -> ../Cellar/python@2/2.7.15_1/bin/pip2.7
lrwxr-xr-x  1 WYH   admin        31 Nov 19 14:23 pip3 -> ../Cellar/python/3.7.1/bin/pip3
lrwxr-xr-x  1 WYH   admin        33 Nov 19 14:23 pip3.7 -> ../Cellar/python/3.7.1/bin/pip3.7
lrwxr-xr-x  1 WYH   admin        37 Nov 19 14:22 pydoc -> ../Cellar/python@2/2.7.15_1/bin/pydoc
lrwxr-xr-x  1 WYH   admin        38 Nov 19 14:22 pydoc2 -> ../Cellar/python@2/2.7.15_1/bin/pydoc2
lrwxr-xr-x  1 WYH   admin        40 Nov 19 14:22 pydoc2.7 -> ../Cellar/python@2/2.7.15_1/bin/pydoc2.7
lrwxr-xr-x  1 WYH   admin        33 Nov 19 14:23 pydoc3 -> ../Cellar/python/3.7.1/bin/pydoc3
lrwxr-xr-x  1 WYH   admin        35 Nov 19 14:23 pydoc3.7 -> ../Cellar/python/3.7.1/bin/pydoc3.7
lrwxr-xr-x  1 WYH   admin        38 Nov 19 14:22 python -> ../Cellar/python@2/2.7.15_1/bin/python
lrwxr-xr-x  1 WYH   admin        38 Nov 19 13:48 python-build -> ../Cellar/pyenv/1.2.8/bin/python-build
lrwxr-xr-x  1 WYH   admin        45 Nov 19 14:22 python-config -> ../Cellar/python@2/2.7.15_1/bin/python-config
lrwxr-xr-x  1 WYH   admin        39 Nov 19 14:22 python2 -> ../Cellar/python@2/2.7.15_1/bin/python2
lrwxr-xr-x  1 WYH   admin        46 Nov 19 14:22 python2-config -> ../Cellar/python@2/2.7.15_1/bin/python2-config
lrwxr-xr-x  1 WYH   admin        41 Nov 19 14:22 python2.7 -> ../Cellar/python@2/2.7.15_1/bin/python2.7
lrwxr-xr-x  1 WYH   admin        48 Nov 19 14:22 python2.7-config -> ../Cellar/python@2/2.7.15_1/bin/python2.7-config
lrwxr-xr-x  1 WYH   admin        34 Nov 19 14:23 python3 -> ../Cellar/python/3.7.1/bin/python3
lrwxr-xr-x  1 WYH   admin        41 Nov 19 14:23 python3-config -> ../Cellar/python/3.7.1/bin/python3-config
lrwxr-xr-x  1 WYH   admin        36 Nov 19 14:23 python3.7 -> ../Cellar/python/3.7.1/bin/python3.7
lrwxr-xr-x  1 WYH   admin        43 Nov 19 14:23 python3.7-config -> ../Cellar/python/3.7.1/bin/python3.7-config
lrwxr-xr-x  1 WYH   admin        37 Nov 19 14:23 python3.7m -> ../Cellar/python/3.7.1/bin/python3.7m
lrwxr-xr-x  1 WYH   admin        44 Nov 19 14:23 python3.7m-config -> ../Cellar/python/3.7.1/bin/python3.7m-config
lrwxr-xr-x  1 WYH   admin        39 Nov 19 14:22 pythonw -> ../Cellar/python@2/2.7.15_1/bin/pythonw
lrwxr-xr-x  1 WYH   admin        40 Nov 19 14:22 pythonw2 -> ../Cellar/python@2/2.7.15_1/bin/pythonw2
lrwxr-xr-x  1 WYH   admin        42 Nov 19 14:22 pythonw2.7 -> ../Cellar/python@2/2.7.15_1/bin/pythonw2.7
lrwxr-xr-x  1 WYH   admin        33 Nov 19 14:23 pyvenv -> ../Cellar/python/3.7.1/bin/pyvenv
lrwxr-xr-x  1 WYH   admin        37 Nov 19 14:23 pyvenv-3.7 -> ../Cellar/python/3.7.1/bin/pyvenv-3.7
lrwxr-xr-x  1 WYH   admin        40 Nov 19 14:22 smtpd.py -> ../Cellar/python@2/2.7.15_1/bin/smtpd.py
lrwxr-xr-x  1 WYH   admin        43 Nov 19 14:22 smtpd2.7.py -> ../Cellar/python@2/2.7.15_1/bin/smtpd2.7.py
lrwxr-xr-x  1 WYH   admin        41 Nov 19 14:22 smtpd2.py -> ../Cellar/python@2/2.7.15_1/bin/smtpd2.py
lrwxr-xr-x  1 WYH   admin        37 Nov 19 14:22 wheel -> ../Cellar/python@2/2.7.15_1/bin/wheel
lrwxr-xr-x  1 WYH   admin        33 Nov 19 14:23 wheel3 -> ../Cellar/python/3.7.1/bin/wheel3
```

可以看到这里安装了 Python3 和 Python2，这里实际上我们不用管，这是 brew 可能在安装别的软件时候所需的依赖，这里如果需要升级的话，只需要

```shell
brew upgrade python # 这里默认是 Python3 
brew upgrade python2
brew upgrade python3
```

使用 pyenv 这部分暂时不分析

### 相关阅读

- [macOS Java 的版本管理](https://notes.0xl2oot.cn/macos/2018/11/19/macOS-java-versions.html)
- [设置 macOS 的系统环境变量](https://notes.0xl2oot.cn/macos/2018/11/07/setting-up-environment-variables-in-macos-sierra.html)