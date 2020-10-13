---
title: Vue 3 One Piece 正式发布！
tags:
- release
- Vue
- Vue3
- One Piece
categories:
- release
date: 2020-09-25 21:00:00
updated: 2020-09-25 21:00:00
---

Vue.js 3.0 "One Piece" 已正式发布，此框架新的主要版本提供了更好的性能、更小的捆绑包体积、更好的 TypeScript 集成、用于处理大规模用例的新 API，并为框架未来的长期迭代奠定了坚实的基础。

3.0 版本的开发周期长达两年多，期间产生了 [30+ RFCs](https://github.com/vuejs/rfcs/tree/master/active-rfcs)、[2600+ commits](https://github.com/vuejs/vue-next/commits/master)、[628 pull requests](https://github.com/vuejs/vue-next/pulls?q=is%3Apr+is%3Amerged+-author%3Aapp%2Fdependabot-preview+)，以及核心仓库之外的大量开发和文档工作。

Vue 3.0 的发布标志着此框架整体上已处于可用状态。尽管框架的某些子项目可能仍需要进一步的开发才能达到稳定状态（特别是 devtools 中的路由和 Vuex 集成），不过现在仍然是开始使用 Vue 3 启动新项目的合适时机。官方还鼓励库作者现在可以开始升级项目以支持 Vue 3。查阅[《Vue 3 Libraries Guide》](https://v3.vuejs.org/guide/migration/introduction.html#supporting-libraries)以获取有关所有框架子项目的详细信息。

<!-- more -->

## 分层内部模块 (Layered internal modules)

Vue 3.0 core 仍然可以通过`<script>`标签进行使用，但其内部架构已被彻底重写为[一组解耦的模块](https://github.com/vuejs/vue-next/tree/master/packages)。新架构提供了更好的可维护性，并允许使用者通过 tree-shaking 来减少多达一半的 runtime 大小。

这些模块还将许多底层 API 暴露出来，可用于许多高级用例：

- 编译器为定制 build-time 提供了对自定义 AST 转换的支持（例如 [build-time i18n](https://github.com/intlify/vue-i18n-extensions)）
- 内核 runtime 提供了优先级最高的 API，用于创建针对不同渲染目标（例如[原生移动设备](https://github.com/rigor789/nativescript-vue-next)、[WebGL](https://github.com/Planning-nl/vugel) 或[终端](https://github.com/ycmjason/vuminal)）的自定义渲染器。默认 DOM 渲染器使用相同的 API 构建
- [`@vue/reactivity`模块](https://github.com/vuejs/vue-next/tree/master/packages/reactivity)导出的函数可以直接访问 Vue 的 reactivity 系统，其本身也可以作为一个独立的程序包使用。它还可以与其他模板解决方案（例如 [vue-lit](https://github.com/yyx990803/vue-lit)）搭配使用，甚至可以在非 UI 场景中使用

## 用于处理大规模用例的新 API

在 Vue 3 中，基于对象的 2.x API 基本没有变化。不过 3.0 还引入了 [Composition API](https://v3.vuejs.org/guide/composition-api-introduction.html)，旨在解决 Vue 在大型应用程序中的使用痛点。Composition API 构建于 reactivity API 之上，可以实现类似于 React 钩子(React hooks)的逻辑组合和重用，与 2.x 基于对象的 API 相比，拥有更灵活的代码组织模式和更可靠的类型推导。

通过 [@vue/composition-api](https://github.com/vuejs/composition-api) 插件，Composition API 还可以与 Vue 2.x 搭配使用，并且目前已经有适用于 Vue 2 和 3 的 Composition API 实用程序库（例如 [vueuse](https://github.com/antfu/vueuse)，[vue-composable](https://github.com/pikax/vue-composable)）。

## 提升性能

与 Vue 2 相比，Vue 3 在捆绑包体积（通过 tree-shaking 减小约 41% 大小）、初始渲染（速度提升约 55%）、更新（速度提升约 133%）和内存使用率（降低约 54%）等方面有了[显著的性能提升](https://docs.google.com/spreadsheets/d/1VJFx-kQ4KjJmnpDXIEaig-cVAAJtpIGLZNbv3Lr4CR0/edit?usp=sharing)。

Vue 3 采用了"compiler-informed Virtual DOM"的方法：模板编译器执行激进的优化并生成渲染函数代码，以提升静态内容访问速度，为绑定类型留下 runtime 提示。最重要的是，将内部的动态节点扁平化处理，以降低 runtime 遍历的成本。因此，用户可以获得两全其美的效果：通过模板优化编译器的性能，或者在用例需要时通过手动渲染函数直接控制。

## 改进与 TypeScript 的集成

Vue 3 使用 TypeScript 编写，具有自动生成、测试和捆绑的类型定义等特性。Composition API 可与类型推导很好地搭配使用。Vetur，Vue 3 的官方 VSCode 扩展，现在支持模板表达式，以及利用 Vue 3 改进的内部类型进行 props 类型检查。

## 实验性功能

为单文件组件(SFC, Singe-File Components)，即 .vue 文件提供了两项新特性：

- [: 用于在 SFC 中使用 Composition API 的语法糖](https://github.com/vuejs/rfcs/blob/sfc-improvements/active-rfcs/0000-sfc-script-setup.md)
- [: SFC 中状态驱动的 CSS 变量](https://github.com/vuejs/rfcs/blob/sfc-improvements/active-rfcs/0000-sfc-style-variables.md)

上述已在 Vue 3.0 中实现并可用，但仅出于收集反馈的目的而提供。在合并 RFC 之前，它们将保持实验性状态。

此外还实现了一个当前未记录的`<Suspense>`组件，该组件允许在初始渲染或分支切换时等待嵌套的异步依赖项（异步组件或包含`async setup()`的组件）。目前正在与 Nuxt.js 团队一起测试和迭代此功能（[即将在 Nuxt 3发布](https://nuxtjs.slides.com/atinux/state-of-nuxt-2020)），并且可能会在 3.1 中到达稳定。

## 下一步

发布后的短期内，开发团队将专注于：

- 版本迁移
- 支持 IE11
- 新 devtools 中的路由和 Vuex 集成
- 对 Vetur 中模板类型推导的进一步改进

目前，Vue 3 和 v3-targeting 项目的文档网站、GitHub 分支和 npm dist 标签将保持 next-denoted 状态。这意味着使用`npm install vue`命令仍会安装 Vue 2.x，而要安装 Vue 3 需使用`npm install vue@next`命令。官方计划在 2020 年底前将所有的 doc 链接、分支和 dist 标签都切换为默认 3.0。

同时，团队已开始启动 2.7 的开发工作计划，这将是 2.x 的最后一个次要版本。2.7 将向后移植来自 v3 的兼容改进，并会提示有关 v3 中已删除/更改的 API 使用情况的警告。团队表示计划在 2021 年第一季度开发 2.7，发布后将直接变为 LTS 版本，具有 18 个月的维护周期。

## 使用

了解有关 Vue 3.0 的更多信息，访问[新文档网站](https://v3.vuejs.org/)。如果是 Vue 2.x 用户，访问[迁移指南](https://v3.vuejs.org/guide/migration/introduction.html)。

详情查看 https://github.com/vuejs/vue-next/releases/tag/v3.0.0