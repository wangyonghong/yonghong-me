---
title: 如何安装 Oh My Zsh？
tags:
- 安装
- Install
- Oh My Zsh
- oh-my-zsh
- mirror
- 镜像
categories:
- 安装
date: 2020-09-26 08:00:00
updated: 2020-09-26 10:00:00
---

## Oh My Zsh 是什么？

Oh My Zsh 是一个令人愉快的，开源的，社区驱动的框架，用于管理您的 Zsh 配置。它捆绑了成千上万的有用功能，助手，插件，主题以及一些让您大喊大叫的东西... 

> "Oh My ZSH!"

iTerm2 + Oh My Zsh 这个组合可以创造出无限可能，感受一下网友们配置的主题：

![iTerm2 + Oh My Zsh](https://up-img.yonghong.tech/pic/2020/09/25-14-42-BwYsU5-FbqgAm.jpg)

<!-- more -->

## 安装

### 官方安装方法

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# 或者
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Gitee镜像仓库安装方法

```shell
REMOTE=https://gitee.com/mirrors/oh-my-zsh.git sh -c "$(curl -fsSL https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh)"
# 或者
REMOTE=https://gitee.com/mirrors/oh-my-zsh.git sh -c "$(wget -O- https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh)"
```

## 相关链接

- [如何安装 Homebrew？](/install/install-homebrew/)
- [如何安装 iTerm2？](/install/install-iterm2/)