---
layout: post
title:  "macOS Java 的版本管理"
category: "macOS"
tags: ["macOS", "Java"]
date: 2018-11-19 00:00:00
updated: 2018-11-19 00:00:00
---

上回书说道，[macOS Python 的版本管理](https://notes.0xl2oot.cn/macos/2018/11/19/macos-python-versions.html)，这次我来说一说 macOS Java 的版本管理。

Java 的版本管理相对来说方便的多，一般我们只需要从官网上下载 Java JDK 的安装程序进行安装就可以很方便的管理了。

<!-- more -->

我们可以用 jenv 这个工具来管理

```
brew install jenv
```

在 `~/.bash_profile` 文件中 添加下面两句(参考 [设置 macOS 的系统环境变量](https://notes.0xl2oot.cn/macos/2018/11/07/setting-up-environment-variables-in-macos-sierra.html))

```
export PATH="$HOME/.jenv/bin:$PATH"
eval "$(jenv init -)"
```

打开命令行

```
source ~/.bash_profile
```


安装之后看

```
$ jenv --version
jenv 0.4.4
```

这样就安装好了

我们看 Java 虚拟机下面这个目录，可以看到我们装了3个 JDK 分别是 1.8，10，11，如果有不需要的 JDK 我们可以直接删掉


```
/Library/Java/JavaVirtualMachines   
$ ls
jdk-10.0.2.jdk   jdk-11.jdk       jdk1.8.0_181.jdk
```

jenv 用法也很简单。 jenv add 加上 JDK 的 Home 目录就可以了


```
/Library/Java/JavaVirtualMachines/jdk-10.0.2.jdk/Contents/Home   
$ jenv add `pwd`
oracle64-10.0.2 added
10.0.2 added
10.0 added
/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home   
$ jenv add `pwd`
oracle64-1.8.0.181 added
1.8.0.181 added
1.8 added
```

查看所有已安装的版本

```
jenv versions
```

查看当前Java版本


```
jenv version
```

设置全局 Java 版本

```
jenv global 1.8.0.181
```