---
title: 如何在 macOS 上安装 OpenJDK/AdoptOpenJDK？
tags:
- 安装
- Install
- OpenJDK
- AdoptOpenJDK
- Homebrew
categories:
- 安装
date: 2020-09-23 09:00:00
updated: 2020-09-26 14:00:00
---

[OpenJDK](https://openjdk.java.net/) 是一个标准，[AdoptOpenJDK](https://adoptopenjdk.net/) 是其中的一个比较常用的实现版本，它由 Java User Group (JUG) 成员、Java 开发者以及一些公司（包含亚马逊、GoDaddy、IBM、微软、Pivotal、红帽等）共同维护，AdoptOpenJDK 提供了同时提供了基于 Hotspot 和 OpenJ9 的版本，IBM 是 OpenJ9 的核心贡献者。本文将会讲解几种在 macOS 上安装 OpenJDK/AdoptOpenJDK 的方法。

<!-- more -->

## 查看自己电脑上安装了哪些Java版本

使用 `/usr/libexec/java_home -V` 命令查看自己电脑上安装的Java版本。

比如说我的电脑，我安装了好几个版本，有三个 AdoptOpenJDK 和两个 Oracle JDK。默认情况下会使用 adoptopenjdk-14.jdk。

```shell
/usr/libexec/java_home -V
Matching Java Virtual Machines (5):
    14.0.2, x86_64:	"AdoptOpenJDK 14"	/Library/Java/JavaVirtualMachines/adoptopenjdk-14.jdk/Contents/Home
    11.0.8, x86_64:	"AdoptOpenJDK 11"	/Library/Java/JavaVirtualMachines/adoptopenjdk-11.jdk/Contents/Home
    11.0.7, x86_64:	"Java SE 11.0.7"	/Library/Java/JavaVirtualMachines/jdk-11.0.7.jdk/Contents/Home
    1.8.0_252, x86_64:	"AdoptOpenJDK 8"	/Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home
    1.8.0_221, x86_64:	"Java SE 8"	/Library/Java/JavaVirtualMachines/jdk1.8.0_221.jdk/Contents/Home

/Library/Java/JavaVirtualMachines/adoptopenjdk-14.jdk/Contents/Home
```

## 使用 jenv 管理 JDK 版本

jenv 是一个管理java版本的命令行工具，可以轻松的帮你配置 JAVA_HOME。

官网 https://www.jenv.be/

GitHub 代码仓库 https://github.com/jenv/jenv

安装也十分简单，官网上有，不多介绍。

```shell
brew install jenv

# 如果使用bash
echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(jenv init -)"' >> ~/.bash_profile

# 如果使用zsh
echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(jenv init -)"' >> ~/.zshrc

# 把Java各个版本添加到jenv
jenv add /Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home
jenv add /Library/Java/JavaVirtualMachines/adoptopenjdk-11.jdk/Contents/Home

# 查看版本
jenv versions

# 切换Java版本
jenv local 11.0
jenv global 11.0
```


## 下载安装包手动安装

鉴于官方的安装包在GitHub上托管，下载起来非常不便，因此这里使用清华的镜像 TUNA。

下载地址：

{% tabs OpenJDK 下载地址, 3 %}
<!-- tab 全部 -->
https://mirrors.tuna.tsinghua.edu.cn/AdoptOpenJDK/
<!-- endtab -->

<!-- tab Java 8 -->
jdk https://mirrors.tuna.tsinghua.edu.cn/AdoptOpenJDK/8/jdk/x64/mac/

jre https://mirrors.tuna.tsinghua.edu.cn/AdoptOpenJDK/8/jre/x64/mac/
<!-- endtab -->

<!-- tab Java11 -->
jdk https://mirrors.tuna.tsinghua.edu.cn/AdoptOpenJDK/11/jdk/x64/mac/

jre https://mirrors.tuna.tsinghua.edu.cn/AdoptOpenJDK/11/jre/x64/mac/
<!-- endtab -->
{% endtabs %}

打开之后下载哪个呢？如果你不知道要下载哪个，你就下载 Hotspot 的 pkg 文件。

下载之后，双击就可以安装了。

## 使用 Homebrew 安装

Homebrew 是一个非常好用的工具，官网 https://brew.sh/

可以参考 [如何安装 Homebrew？](/install/install-homebrew/)

### 官方的 Homebrew Tap

https://github.com/AdoptOpenJDK/homebrew-openjdk

官方维护了一个 Homebrew Tap，已经很方便了，美中不足是他提供的下载链接是托管在GitHub上的，下载非常慢，所以我建议使用下面笔者维护的 Tap wangyonghong/openjdk-mirror。

如果你的网速还可以，那么使用官方的就足够了。

```shell
brew tap AdoptOpenJDK/openjdk

brew search openjdk

brew cask install adoptopenjdk11
brew cask uninstall adoptopenjdk11
```

### wangyonghong/openjdk-mirror

https://github.com/wangyonghong/homebrew-openjdk-mirror

笔者维护的这个 Tap，JDK 的下载链接是来自清华的镜像 TUNA，和上面的手动下载安装的地址是一样的。

用法相同

```shell
brew tap wangyonghong/openjdk-mirror

brew search openjdk

brew cask install tuna-adoptopenjdk8
brew cask uninstall tuna-adoptopenjdk8
```

如果这个工具用着有什么问题，欢迎来GitHub上提[issue](https://github.com/wangyonghong/homebrew-openjdk-mirror/issues)。

## 参考链接

- [如何安装 Homebrew？](/install/install-homebrew/)
- [如何安装 iTerm2？](/install/install-iterm2/)
- [如何安装 Oh My Zsh？](/install/install-oh-my-zsh/)