---
layout: post
title: 【已解决】GitHub Metadata:No GitHub API authentication
categories: [Jekyll]
tags : [Jekyll, GitHub]
date: 2018-01-26 00:00:00
updated: 2018-01-26 00:00:00
---

## 问题

Jekyll 配置过程中报错  `GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data.`

<!-- more -->
## 解决方法

在 `~/.bash_profile` 文件中加上

```
export JEKYLL_GITHUB_TOKEN='你的TOKEN'
```

即可。

TOKEN 需要在 GitHub 上申请，Settings->Developer settings->Personal access tokens，然后 Generate new token，在 public-repo 前面打上对勾，复制下来 token，写入 `~/.bash_profile` 文件中，执行 `source ~/.bash_profile` 即可。

![生成 TOKEN](/images/post/jekyll/token.png)

测试是否添加成功，命令行中输入 `echo $JEKYLL_GITHUB_TOKEN`，如果打印出你申请的 TOKEN 那么说明已经添加成功了。

## 番外

本人在完成这一些配置之后，再次打开 terminal 运行之后，发现还是报错，仔细查看之后发现 macOS 不会自动加载 `~/.bash_profile` 文件，解决方法也很简单，本人用的 terminal 是 zsh，只需要在 `~/.zshrc` 文件末尾加上 

```
source .bash_profile
```

即可。


