---
layout: post
title:  "Vuepress踩坑小结"
category: "vuepress"
tags: ["vuepress", "Vuepress", "nginx", "Nginx"]
date: 2019-07-12 00:00:00
updated: 2019-07-12 00:00:00
---

## 介绍

VuePress 由两部分组成：第一部分是一个[极简静态网站生成器](https://github.com/vuejs/vuepress/tree/master/packages/%40vuepress/core)，它包含由 Vue 驱动的主题系统和插件 API，另一个部分是为书写技术文档而优化的默认主题，它的诞生初衷是为了支持 Vue 及其子项目的文档需求。

<!-- more -->

每一个由 VuePress 生成的页面都带有预渲染好的 HTML，也因此具有非常好的加载性能和搜索引擎优化（SEO）。同时，一旦页面被加载，Vue 将接管这些静态内容，并将其转换成一个完整的单页应用（SPA），其他的页面则会只在用户浏览到的时候才按需加载。

## 为什么不是...?

### [Nuxt](https://nuxtjs.org/)

VuePress 能做的事情，Nuxt 理论上确实能够胜任，但 Nuxt 是为构建应用程序而生的，而 VuePress 则专注在以内容为中心的静态网站上，同时提供了一些为技术文档定制的开箱即用的特性。

### [Docsify](https://docsify.js.org/) / [Docute](https://docute.org/)

这两个项目同样都是基于 Vue，然而它们都是完全的运行时驱动，因此对 SEO 不够友好。如果你并不关注 SEO，同时也不想安装大量依赖，它们仍然是非常好的选择！

### [Hexo](https://hexo.io/)

Hexo 一直驱动着 Vue 的文档 —— 事实上，在把我们的主站从 Hexo 迁移到 VuePress 之前，我们可能还有很长的路要走。Hexo 最大的问题在于他的主题系统太过于静态以及过度地依赖纯字符串，而我们十分希望能够好好地利用 Vue 来处理我们的布局和交互，同时，Hexo 的 Markdown 渲染的配置也不是最灵活的。

### [GitBook](https://www.gitbook.com/)

我们的子项目文档一直都在使用 GitBook。GitBook 最大的问题在于当文件很多时，每次编辑后的重新加载时间长得令人无法忍受。它的默认主题导航结构也比较有限制性，并且，主题系统也不是 Vue 驱动的。GitBook 背后的团队如今也更专注于将其打造为一个商业产品而不是开源工具。

## 更多介绍

[https://vuepress.vuejs.org/](https://vuepress.vuejs.org/)

[https://vuepress.vuejs.org/zh/](https://vuepress.vuejs.org/zh/)

[https://vuepressbook.com/](https://vuepressbook.com/)

## 开始

### 环境

本地运行文档需要安装 Node.js、Yarn。

macOS 安装 

```sh
brew install node yarn
yarn global add vuepress
```

### 运行

运行的命令是在package.json中定义的

```json
{
  "scripts": {
    "dev": "vuepress dev .",
    "build": "vuepress build ."
  }
}
```

执行

```sh
yarn dev
```

就等于执行

```
vuepress dev .
```

### 打包

```sh
yarn build
```

## 配置

配置在.vuepress中config.js中，可参考[https://vuepress.vuejs.org/zh/config/](https://vuepress.vuejs.org/zh/config/)进行配置

可以将导航配置单独拿出来

config.js

```js
const navConfig = require('./nav.js');

module.exports = {
  title: '产品文档',
  description: 'lalalala',
  head: [
    ['link', { rel: 'icon', href: '/logo.png' }]
  ],
  dest: 'dist',
  markdown: {
    lineNumbers: false
  },
  themeConfig: {
    nav: navConfig,
    search: true,
    searchMaxSuggestions: 10,
    lastUpdated: 'Last Updated',
    activeHeaderLinks: true,
    displayAllHeaders: true,
    sidebar: 'auto'
  }
}
```

nav.js

```js
module.exports = [
    {
      text: '首页', link: '/'
    },
    {
      text: 'Android', 
      items: [
        {
          text: 'v1.0.0',
          link: '/android/v1.0.0/'
        }
      ]
    },
    {
      text: 'iOS', 
      items: [
        {
          text: 'v1.0.0',
          link: '/ios/v1.0.0/'
        }
      ]
    }
  ]
```

## 部署

### Nginx部署

```conf
server {
  listen 80;
  server_name 127.0.0.1;

  location / {
    root /vuepress;
    index index.html index.htm;
    try_files $uri $uri/ /index.html;
  }
}
; $uri 是请求文件的路径
; $uri/ 事请求目录的路径
; 二者缺一不可
```

## 亮点

### 自定义容器

```md
::: tip
This is a tip
:::

::: warning
This is a warning
:::

::: danger
This is a dangerous warning
:::
```

![29-18-18-屏幕快照2019-07-12上午9.43.41-gR4ink](https://up-img.yonghong.tech/pic/2021/07/29-18-18-%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-07-12%20%E4%B8%8A%E5%8D%889.43.41-gR4ink.png)