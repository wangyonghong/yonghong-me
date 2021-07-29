---
layout: post
title:  "Jekyll 搜索引擎优化之 sitemap"
category: "Jekyll"
tags: ["Jekyll", "sitemap", "搜索"]
date: 2018-10-27 00:00:00
updated: 2018-10-27 00:00:00
---

### 什么是 sitemap

> Sitemap 可方便网站管理员通知搜索引擎他们网站上有哪些可供抓取的网页。最简单的 Sitemap 形式，就是XML 文件，在其中列出网站中的网址以及关于每个网址的其他元数据（上次更新的时间、更改的频率以及相对于网站上其他网址的重要程度为何等），以便搜索引擎可以更加智能地抓取网站。 ——[百度百科](https://baike.baidu.com/item/sitemap)

<!-- more -->

### Jekyll-sitemap 插件

[https://github.com/jekyll/jekyll-sitemap](https://github.com/jekyll/jekyll-sitemap)

> Jekyll plugin to silently generate a sitemaps.org compliant sitemap for your Jekyll site

### 安装方法 

与之前说过的[为 Jekyll 添加分页功能](https://notes.0xl2oot.cn/jekyll/2018/10/27/jekyll-paginate.html)类似，在网站的 `Gemfile`文件中添加下面的语句

```
gem "jekyll-sitemap"
```

修改 `_config.yml` 文件

```yml
url: "http://example.com" # the base hostname & protocol for your site
plugins:
  - jekyll-sitemap
```

更多用法参见 GitHub [https://github.com/jekyll/jekyll-sitemap](https://github.com/jekyll/jekyll-sitemap)

### 在本地运行

如果想在本地运行的话，就要执行下面这条命令来安装依赖包

```shell
gem install jekyll-sitemap
```

或者

```shell
bundle install
```

如果不执行的话就会出现下面的报错


```
Could not find jekyll-sitemap in any of the sources
Run `bundle install` to install missing gems.
```
