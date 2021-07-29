---
layout: post
title:  "设置 macOS 的系统环境变量"
category: "macOS"
tags: ["macOS"]
date: 2018-11-07 00:00:00
updated: 2018-11-07 00:00:00
---

macOS 的环境变量一般有这几个地方

```
/etc/profile
/etc/bashrc
~/.bash_profile
```

<!-- more -->

前两个配置属于系统级别的，所有用户均可使用；第三个配置属于用户级别的，仅供当前用户读写。建议将个人用户所需要的环境变量配置于第三个当中。但是第三个文件默认是不存在的，需要自己创建。

如果你使用 zsh，还会在这里

```
~/.zshrc
```

所以我建议，个人的配置只在 `~/.bash_profile` 中写。别的文件尽量不要动

如果你用 zsh，那么只在 `.zshrc` 中只添加

```
source .bash_profile
# !!! Please put user configuration in ~/.bash_profile
```

提示自己把配置都放在 `~/.bash_profile` 中，这样能管理起来也方便。

还有一个叫 nvm 软件，是管理 node 版本的工具，我建议如果不常用还是不要了，这个东西让我的命令行启动多了 1.2 秒

