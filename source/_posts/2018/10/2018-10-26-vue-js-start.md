---
layout: post
title:  "Vue.js 初学者可能会遇到的问题"
category: "Vue.js"
tags: ["vue.js", "vue", "beginner", "npm", "yarn", "vue-cli"]
date: 2018-10-26 00:00:00
updated: 2018-10-26 00:00:00
---

### 1. npm 和 Yarn

Yarn [https://yarnpkg.com/zh-Hans/](https://yarnpkg.com/zh-Hans/)

npm [https://www.npmjs.com/](https://www.npmjs.com/)

<!-- more -->


npm 和 Yarn 都是 JavaScript 的管理工具，但是 Yarn 会比 npm 快的多，Yarn 会缓存它下载的每个包，所以无需重复下载。它还能并行化操作以最大化资源利用率，安装速度之快前所未有。

### 2. npm 和 cnpm 

npm 的仓库在国外，国内用户访问会慢很多，甚至有时候影响了项目的构建。

因此出现了 cnpm 淘宝的 npm 镜像 [https://npm.taobao.org/](https://npm.taobao.org/)

可以使用淘宝定制的 cnpm (gzip 压缩支持) 命令行工具代替默认的 npm:


```shell
$ npm install -g cnpm --registry=https://registry.npm.taobao.org
```

安装完之后就可以使用 cnpm 命令了，详细的使用方法还是看官方的说明吧 [https://npm.taobao.org/](https://npm.taobao.org/)


### 3. eslint - JavaScript 代码规范

刚开始 init Vue.js 的项目时，有关于 JavaScript 语法检查的 eslint 的选项，如果我们开了之后，会发现运行的时候可能有很多错误，但是不知道错在哪里，其实有可能不是错误，只是不符合规范。

我们可以从下面两个链接中学习一下关于 JavaScript 的规范，这个规范只是大家约定俗成的的一套规范，能够让我们开发出更加优秀的代码。虽然看着比较艰难，有些规范也有很多人争论，但这并不是我们的重点，我们的重点在如何高效率的开发出程序来。


[https://github.com/standard/standard/blob/master/docs/README-zhcn.md](https://github.com/standard/standard/blob/master/docs/README-zhcn.md)

[https://github.com/standard/standard/blob/master/docs/RULES-zhcn.md](https://github.com/standard/standard/blob/master/docs/RULES-zhcn.md)

### 4. Yarn CLI 介绍

[https://yarnpkg.com/zh-Hans/docs/cli/](https://yarnpkg.com/zh-Hans/docs/cli/)

### Vuetify - Material Design Component Framework

https://vuetifyjs.com/

### 5. vue-2-boilerplate - 一个 Vue.js 的脚手架

Vue 2 boilerplate for developing medium to large single page applications.

[https://github.com/petervmeijgaard/vue-2-boilerplate](https://github.com/petervmeijgaard/vue-2-boilerplate)

### 6. Vue CLI 3

现在 Vue CLI 的版本号是 3.X.X，有关于他的用法的说明在官网上 [https://cli.vuejs.org/](https://cli.vuejs.org/) 

官网上面是这样描述 Vue CLI 3 的

> Standard Tooling for Vue.js Development.

> Vue.js 开发的标准工具

Vue CLI 3 的安装的方式是

```shell
npm install -g @vue/cli
# OR
yarn global add @vue/cli
```

创建一个项目：

```shell
vue create my-project
# OR 使用 web 管理界面管理 Vue.js 的项目
vue ui
```

![](https://up-img.yonghong.tech/pic/2021/07/29-17-26-ui-new-project-NTLfxv.png)

CLI 服务 (@vue/cli-service) 是一个开发环境依赖。它是一个 npm 包，局部安装在每个 @vue/cli 创建的项目中。

CLI 服务是构建于 webpack 和 webpack-dev-server 之上的。它包含了：

加载其它 CLI 插件的核心服务；
一个针对绝大部分应用优化过的内部的 webpack 配置；
项目内部的 vue-cli-service 命令，提供 serve、build 和 inspect 命令。


而之前的 Vue CLI 2 的安装方式却是不同的，因此网上的教程会让你眼花缭乱，不知所措，如果有特定需求需要安装低版本的话，按照下面的方式安装

```shell
npm install -g vue-cli
```

创建一个项目

```shell
vue init webpack my-project
```

### 7. vue-router 


Vue Router 是 Vue.js 官方的路由管理器。它和 Vue.js 的核心深度集成，让构建单页面应用变得易如反掌。

用法

```js
import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
```

App.vue 中这样写


```vue
<template>
  <router-view/>
</template>
```


### 参考文献

- [知乎 - npm和yarn的区别，我们该如何选择？](https://zhuanlan.zhihu.com/p/27449990)

