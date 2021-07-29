---
layout: post
title:  "vuetifyjs 和 Nuxt 配合使用时，样式在生产环境失效"
category: "vuetify"
tags: ["vuetify"]
date: 2019-01-16 00:00:00
updated: 2019-01-16 00:00:00
---

vuetify 按钮有一些属性，[比如 info, warning, error 和 success 等](https://vuetifyjs.com/zh-Hans/components/buttons)，这些在 dev 模式下是正常显示的，如下图，到了生产环境却不显示了，这是什么原因呢？

- npm run dev 正常
- npm run generate 放到 Nginx 中不正常

<!-- more -->

![29-17-55-ScreenShot2019-01-19at12.19.20AM-UkN4wY](https://up-img.yonghong.tech/pic/2021/07/29-17-55-Screen%20Shot%202019-01-19%20at%2012.19.20%20AM-UkN4wY.png)


我查了好久，终于在 Stack Overflow 上找到了答案

[https://stackoverflow.com/questions/50003226/vuetify-colors-are-not-showing-up](https://stackoverflow.com/questions/50003226/vuetify-colors-are-not-showing-up)

很简单，就是需要让这些内容被 v-app 标签给包起来

```vue
<v-app>
  <v-btn color="success">Success</v-btn>
  <v-btn color="error">Error</v-btn>
  <v-btn color="warning">Warning</v-btn>
  <v-btn color="info">Info</v-btn>
</v-app>
```

然后我又发现了问题，一刷新，颜色又没了。后来经过一步步定位，发现问题在中间件（middleware），我在中间件中发现了一个问题，我在中间件中使用了 vuex 读取了一个数据，但是问题是这个数据在刷新页面后并不存在，导致不能继续进行。这个数据应该是每次刷新都从 cookie 中读取的，然而为什么没有读取呢？

进过查资料，发现 nuxt 在 universal 模式下是有问题的，middleware 只有在刷新时的服务端执行，但是页面没有变化，服务端并不会刷新。这样就出现了问题。导致后面的程序无法执行，而且没有错误提示。不知道是不是这样的问题

后来由于是内部使用的平台也不需要搜索引擎收录，所以还是改成了 spa。

提了 issue

https://github.com/nuxt/nuxt.js/issues/5064