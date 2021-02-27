---
title: 如何在macOS根目录创建文件夹
tags:
- macOS
categories:
- macOS
date: 2021-02-27 10:24:00
updated: 2021-02-27 10:24:00
---

在短短的两个月里，已经遇到了 2 次这个问题，第 1 次是 macOS@Catalina 版本，第 2 次是升级后的 macOS@Big Sur 版本，在这里记录一下解决办法。

## macOS@Catalina 版本

重启系统进入恢复模式，关闭 SIP，重启后命令行执行下面这行代码，再创建文件夹就能成功了。

```shell
sudo mount -uw /
```

## macOS@Big Sur 版本

重启系统进入恢复模式，关闭 SIP（不确定有没有这个步骤，如果有人尝试可以评论一下），接下来稍稍麻烦一点，修改 /etc/synthetic.conf 文件

<!-- more -->

```shell
sudo vi /etc/synthetic.conf
```

输入如下内容，data 换成你要创建的文件夹，后面是映射目录，注意，中间是 Tab，不是空格

```shell
data    /private/data
```

重启系统后，系统根目录出现了对应的文件夹，这个文件夹是一个软链接，链接到了前面写的映射目录中。

如图，我在我电脑根目录下创建了一个 home 文件夹的软链接，实际存储在 /private/home 这个文件夹中。

![根目录下的home文件夹](https://up-img.yonghong.tech/pic/2021/02/27-12-28-%E6%88%AA%E5%B1%8F2021-02-26%20%E4%B8%8B%E5%8D%888.41.34-ovojux.png)

这是我的 /etc/synthetic.conf 文件内容：

```shell
➜  ~ cat /etc/synthetic.conf
home	/private/home
```

## 相关文档

- [Mac升级到big sur之后，根目录无法写入文件如何解决？](https://newsn.net/say/mac-big-sur-root-readonly.html)
- [macOS 开启或关闭 SIP](https://sspai.com/post/55066)
- [关于基于 Intel 的 Mac 电脑上的 macOS 恢复功能](https://support.apple.com/zh-cn/HT201314)
