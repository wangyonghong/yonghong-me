---
title: 如何安装 Homebrew？
tags:
- 安装
- Install
- Homebrew
- brew
- mirror
- 镜像
categories:
- 安装
date: 2020-09-26 08:00:00
updated: 2020-09-26 08:00:00
---

## Homebrew 是什么？

Homebrew是一款自由及开放源代码的软件包管理系统，用以简化macOS系统上的软件安装过程，最初由马克斯·霍威尔（Max Howell）写成。因其可扩展性得到了一致好评，而在Ruby on Rails社区广为人知。

Homebrew使用GitHub，通过用户的贡献扩大对软件包的支持。2012年，Homebrew是GitHub上拥有最多新贡献者的项目。2013年，Homebrew同时成为GitHub上最多贡献者及最多已关闭问题的项目。

## 相关网站

官网：https://brew.sh/

官方GitHub仓库：https://github.com/Homebrew/brew

官方GitHub安装脚本：https://github.com/Homebrew/install

国内定制安装脚本：https://gitee.com/cunkai/HomebrewCN

<!-- more -->

## 安装

官方的安装方法：

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

国内定制的安装脚本：

```
/bin/bash -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
```

## 可能遇到的问题

如果是新手可能会遇到git没有安装的问题，一般情况只需要按照提示安装就可以了，但是也有例外，当出现

> 不能安装该软件，因为当前无法从软件更新服务器获得。

![25-12-19-截屏2020-09-25下午12.15.04-yOZ7xD](https://up-img.yonghong.tech/pic/2020/09/25-12-19-%E6%88%AA%E5%B1%8F2020-09-25%20%E4%B8%8B%E5%8D%8812.15.04-yOZ7xD.png)

这种情况时，也不用慌，打开 https://developer.apple.com/ 网站，下载 Command Line Tools 安装就可以了。

![25-12-19-截屏2020-09-25下午12.16.21-OZrMBN](https://up-img.yonghong.tech/pic/2020/09/25-12-19-%E6%88%AA%E5%B1%8F2020-09-25%20%E4%B8%8B%E5%8D%8812.16.21-OZrMBN.png)

## 相关链接

- [如何安装 iTerm2？](/install/install-iterm2/)
- [如何安装 Oh My Zsh？](/install/install-oh-my-zsh/)