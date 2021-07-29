---
layout: post
title: .gitignore文件的配置
tags: [git]
date: 2018-01-27 00:00:00
updated: 2018-01-27 00:00:00
---

> 对于本 Blog 来说，在上传到 GitHub 中时，并不需要上传 `_site` 和 `_drafts` 目录中的内容，此时便可以设置 `.gitignore` 文件。

有些时候，你必须把某些文件放到Git工作目录中，但又不能提交它们，比如保存了数据库密码的配置文件啦，等等。

好在 Git 考虑到了大家的感受，这个问题解决起来也很简单，在 Git 工作区的根目录下创建一个特殊的 `.gitignore` 文件，然后把要忽略的文件名填进去，Git 就会自动忽略这些文件。

<!-- more -->

不需要从头写 `.gitignore` 文件，GitHub 已经为我们准备了各种配置文件，只需要组合一下就可以使用了。所有配置文件可以直接在线浏览：

[https://github.com/github/gitignore](https://github.com/github/gitignore)

## 忽略文件的原则

忽略文件的原则是：

1. 忽略操作系统自动生成的文件，比如缩略图等；
2. 忽略编译生成的中间文件、可执行文件等，也就是如果一个文件是通过另一个文件自动生成的，那自动生成的文件就没必要放进版本库，比如 Java 编译产生的 `.class` 文件；
3. 忽略你自己的带有敏感信息的配置文件，比如存放口令的配置文件。


## 例子

假设你在 Windows 下进行 Python 开发， Windows 会自动在有图片的目录下生成隐藏的缩略图文件，如果有自定义目录，目录下就会有 `Desktop.ini` 文件，因此你需要忽略 Windows 自动生成的垃圾文件：

```
# Windows:
Thumbs.db
ehthumbs.db
Desktop.ini
```

然后，继续忽略Python编译产生的 `.pyc` 、 `.pyo` 、 `dist` 等文件或目录：

```
# Python:
*.py[cod]
*.so
*.egg
*.egg-info
dist
build
```

加上你自己定义的文件，最终得到一个完整的 `.gitignore` 文件，内容如下：

```
# Windows:
Thumbs.db
ehthumbs.db
Desktop.ini

# Python:
*.py[cod]
*.so
*.egg
*.egg-info
dist
build

# My configurations:
db.ini
deploy_key_rsa
```

最后一步就是把 `.gitignore` 也提交到 Git，就完成了！当然检验 `.gitignore` 的标准是 `git status` 命令是不是说 `working directory clean` 。

## Windows 下创建 `.gitignore` 文件

方法一（最直接）：
在资源管理创建文件时，文件命名 `.gitignore.`，注意结尾有个 `.` 号，回车确认时系统会自动存成 `.gitignore`。

方法二：
打开文本编辑器，保存时文件名输入 `.gitignore`，保存类型选 `所有文件`。

方法三：
进入 cmd 命令行，执行 `echo > .gitignore` 输入空内容并创建文件，或执行 `rename somefile .gitignore、copy somefile .gitignore` 从已有文件复制、重命名。

## 强制添加到 Git

有些时候，你想添加一个文件到 Git，但发现添加不了，原因是这个文件被 `.gitignore` 忽略了：

```shell
$ git add App.class
The following paths are ignored by one of your .gitignore files:
App.class
Use -f if you really want to add them.
```

如果你确实想添加该文件，可以用 `-f` 强制添加到 Git：

```shell
$ git add -f App.class
```

或者你发现，可能是 	`.gitignore` 写得有问题，需要找出来到底哪个规则写错了，可以用 `git check-ignore` 命令检查：

```shell
$ git check-ignore -v App.class
.gitignore:3:*.class    App.class
```

Git 会告诉我们，`.gitignore` 的第3行规则忽略了该文件，于是我们就可以知道应该修订哪个规则。

## 小结
忽略某些文件时，需要编写 `.gitignore` 。

`.gitignore` 文件本身要放到版本库里，并且可以对 `.gitignore` 做版本管理！


## 参考

[廖雪峰的官方网站-忽略特殊文件](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013758404317281e54b6f5375640abbb11e67be4cd49e0000)



