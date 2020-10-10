---
title: 软件推荐 | 更好用的图床(文件)上传客户端 uPic
tags:
- 软件推荐
- 推荐
- uPic
- 图床
categories:
- 软件推荐
date: 2020-10-10 17:00:00
updated: 2020-10-10 17:00:00
---

[uPic(upload Picture)](https://github.com/gee1k/uPic) 是一款 macOS 端的图床(文件)上传客户端。

💡 特点：：无论是本地文件、或者屏幕截图都可自动上传，菜单栏显示实时上传进度。上传完成后文件链接自动复制到剪切板，让你无论是在写博客、灌水聊天都能快速插入图片。 连接格式可以是普通 URL、HTML 或者 Markdown，仍由你掌控。

**🔋 支持图床：** [smms](https://sm.ms/)、 [又拍云 USS](https://www.upyun.com/products/file-storage)、[七牛云 KODO](https://www.qiniu.com/products/kodo)、 [阿里云 OSS](https://www.aliyun.com/product/oss/)、 [腾讯云 COS](https://cloud.tencent.com/product/cos)、 [百度云 BOS](https://cloud.baidu.com/product/bos.html)、[微博](https://weibo.com/)、[Github](https://github.com/settings/tokens)、 [Gitee](https://gitee.com/profile/personal_access_tokens)、 [Amazon S3](https://aws.amazon.com/cn/s3/)、[Imgur](https://imgur.com/)、[自定义上传接口](https://blog.svend.cc/upic/tutorials/custom)、...

<!-- more -->

## 🚀 如何安装

### 下载安装

#### 1.Homebrew(推荐):

```
brew cask install upic
```

#### 2.手动

从 [Github release](https://github.com/gee1k/uPic/releases) 下载。

**如果在国内访问 Github 下载困难的，可以从[Gitee release](https://gitee.com/gee1k/uPic/releases)下载。**

### 检查 Finder 扩展权限

- 1.打开 uPic

- 2.打开`系统偏好设置` - `扩展` - `访达扩展` 确保 `uPicFinderExtension`是勾选状态

<img src="https://up-img.yonghong.tech/pic/2020/10/10-17-07-68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f676565316b2f6f7373406d61737465722f73637265656e73686f742f755069632d636e2f66696e6465722d657874656e73696f6e2e706e67-DYYKob.png" width="650px" style="margin: 0 auto;"/>

## 🕹 使用方式

| 功能                     | 描述                                         | 预览                                                         |
| ------------------------ | -------------------------------------------- | ------------------------------------------------------------ |
| **🖥 选择文件上传**       | 从`Finder`选择文件上传。`可设置全局快捷键`   | ![img](https://up-img.yonghong.tech/pic/2020/10/10-17-07-68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f676565316b2f6f7373406d61737465722f73637265656e73686f742f755069632d636e2f73656c65637446696c652e676966-VqFefp.gif) |
| **⌨️ 复制文件上传**       | 上传已拷贝到剪切板的文件。`可设置全局快捷键` | ![img](https://up-img.yonghong.tech/pic/2020/10/10-17-07-68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f676565316b2f6f7373406d61737465722f73637265656e73686f742f755069632d636e2f7061737465626f6172642e676966-hBiI5s.gif) |
| **📸 截图上传**           | 直接拉框截图上传。`可设置全局快捷键`         | ![img](https://up-img.yonghong.tech/pic/2020/10/10-17-07-68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f676565316b2f6f7373406d61737465722f73637265656e73686f742f755069632d636e2f73637265656e73686f742e676966-91Kj7l.gif) |
| **🖱 拖拽本地文件上传**   | 拖拽文件到状态栏上传                         | ![img](https://up-img.yonghong.tech/pic/2020/10/10-17-07-68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f676565316b2f6f7373406d61737465722f73637265656e73686f742f755069632d636e2f6472616746696c652e676966-5Dzzbw.gif) |
| **🖱 拖拽浏览器图片上传** | 从浏览器拖拽图片到状态栏上传                 | ![img](https://up-img.yonghong.tech/pic/2020/10/10-17-07-68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f676565316b2f6f7373406d61737465722f73637265656e73686f742f755069632d636e2f6472616746726f6d42726f777365722e676966-QYEBH7.gif) |
| **📂 Finder 中右键上传**  | 右击文件上传                                 | ![img](https://up-img.yonghong.tech/pic/2020/10/10-17-07-68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f676565316b2f6f7373406d61737465722f73637265656e73686f742f755069632d636e2f636f6e746578746d656e752e676966-7Nmsoo.gif) |
| **⌨️ 命令行上传**         | 通过执行命令调用 uPic 上传文件               | ![img](https://up-img.yonghong.tech/pic/2020/10/10-17-07-68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f676565316b2f6f7373406d61737465722f73637265656e73686f742f755069632d636e2f636c692e676966-uqE7yy.gif) |

## 🧰 更多功能

### 1.全局快捷键

<img src="https://up-img.yonghong.tech/pic/2020/10/10-17-07-68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f676565316b2f6f7373406d61737465722f73637265656e73686f742f755069632d636e2f73686f7274637574732e706e67-eWTput.png" width="450px" style="margin: 0 auto;"/>

### 2. 上传历史

<img src="https://up-img.yonghong.tech/pic/2020/10/10-17-07-68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f676565316b2f6f7373406d61737465722f73637265656e73686f742f755069632d636e2f686973746f72792e706e67-Ad5U62.png" width="650px" style="margin: 0 auto;"/>




