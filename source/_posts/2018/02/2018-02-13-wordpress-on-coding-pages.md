---
layout: post
title: 在 Coding.net 上部署 WordPress 和 ThinkPHP
categories: [Coding Pages]
tags: [Coding Pages, WordPress, ThinkPHP]
date: 2018-02-13 00:00:00
updated: 2018-02-13 00:00:00
---

和 Git Pages 一样，Coding.net 也提供了 [Coding Pages](https://coding.net/pages/) 的服务。

## 为什么采用 [Coding Pages](https://coding.net/pages/)

相比 Git Pages，Coding Pages 服务器在香港，国内外访问页面都可以很流畅，并且全新支持动态页面部署

> 基于 Linux 系统的虚拟机环境。
> 率先支持部署 PHP 语言程序。
> 完整的 MySQL 数据库功能。

<!-- more -->

## 部署 [WordPress](https://wordpress.org/)

可以参考 [Coding 帮助文档](https://coding.net/help/doc/pages/dpages.html)

## 部署 [ThinkPHP](http://www.thinkphp.cn/)

步骤和上面部署 WordPress 类似，这里需要注意，ThinkPHP 需要修改 URL 重写的配置，参考 [TP5开发手册-URL重写](https://www.kancloud.cn/manual/thinkphp5/177576)，由于没有修改服务器配置的权限，需要修改 index.php 文件。另外，在 Coding Pages 的设置页面上设置网站入口为 /public。

## 绑定自定义域名

可以参考 [Coding 帮助文档](https://coding.net/help/doc/pages/domain.html)

在这里需要注意，如果安装完 WordPress 之后在绑定自定义域名，可能会导致管理界面进不去，这是因为在 WordPress 数据库中存储了安装时候的 Url，所以在提交登录表单的时候会指向原来的域名，然后自动跳转到自定义域名，导致无法登录。

解决办法：

从 Coding Pages 管理界面进入 phpMyAdmin, 修改存储的 Url 的 wp_options 表的前两项 siteUrl 和 home.

![Modify Url](https://up-img.yonghong.tech/pic/2021/07/29-13-03-modify-url-u3L95Z.png)

修改后再次刷新，就可以进入管理界面了。

