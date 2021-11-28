---
title: 爱奇艺直播 WebAssembly 优化之路
tags:
- WebAssembly
categories:
- 转载
date: 2020-07-28 22:24:00
updated: 2020-07-28 22:24:00
---

## WebAssembly 技术简介

近几年，WebAssembly 技术非常火，可以说是成为了 JavaScript 一个新的转折点。JavaScript 自 1995 年诞生之日起，其性能问题就被大家诟病。直到 2008 年，很多浏览器加入了即时编译器，JavaScript 也开始引入 JITs，再加上 Google 等厂商对其的大力优化，其性能提升了 10 倍不止。由此，JavaScript 也开始跳出了浏览器的范围，在各个领域崭露头脚，比如后台使用的 Node.js 和桌面端使用的 Electron 等。

JIT 技术简而言之是在 JavaScript 解释执行时将常用的二进制代码块暂存下来，在下一次解释执行相同的代码块的时候可以直接运行暂存的二进制代码块，节约了解释的时间。那能不能将所有 JavaScript 代码一次性都编译成二进制，提升运行效率呢？WebAssembly 的出现回答了这个问题。

在 WebAssembly 出现之前，JavaScript 是浏览器里可以运行的唯一的编程语言。而 WebAssembly 技术使浏览器运行别的语言编写的程序变成了可能。目前可以使用 C、C++、Rust、Go、Java、C# 编译器（还有更多）来创建 wasm 模块。浏览器在运行时将 wasm 模块放在专有的虚拟机中运行。由于是二进制的文件，运行效率比解释执行的 JavaScript 脚本要高很多，因此，很多前端开发者也把 WebAssembly 技术视作下一代的前端技术。

目前 WebAssembly 的兼容性如下图所示：

<!--more-->

![爱奇艺直播WebAssembly优化之路](https://up-img.yonghong.tech/pic/2020/07/28-17-57-5963ff768bcf49e76cf779db582fdc94-L4PL0t.png)

可以看到，在新版本上，主流浏览器不管是在 PC 端还是移动端都支持了 WebAssembly，而且各大浏览器厂商还在持续支持此项技术，相信不久就会得到非常普遍的应用。

## WebAssembly 和直播，不一样的火花

一直以来，爱奇艺生产的直播流有 mp4 和 flv 两种格式，但 Html5 的 video 标签原生只支持 mp4 的播放，如何解决 flv 格式在网页端播放的问题就摆在了所有人的面前。一般来说 flv 格式在网页端播放有以下几种解决方案：

**1、使用 flash 播放器插件**

不过因为性能和安全等各种问题，各大浏览器已经逐渐弱化了这种方式，Chrome 也将在 2020 年左右停止对 flash player 的支持，所以现在基本很少有人用了。

**2、网页对 flv 格式的视频解码**

使用 canvas 渲染图像，使用 audio 播放声音，相当于网页端做一个播放器，这也是可行的。但各大浏览器厂商对原生 video 控件会针对不同的平台做硬件加速渲染的优化，如果自己渲染的话，硬件加速这块便也需要自己做，这样会耗费极大的人力，并且效果也很难和浏览器原生的硬件加速相比。

**3、在网页端将 flv 格式转成 mp4 格式然后使用原生播放器**

这也是目前使用得最多的方案。这样既可以播放 flv 的直播流，也可以将渲染丢给原生播放器去做，充分发挥原生播放器的优化能力。

爱奇艺直播使用的就是第三种方式，当 flv 的直播流到达前端时，使用 JavaScript 将 flv 转换成 mp4，再交给原生播放器。但由于 JavaScript 运行效率较低，这部分的性能一直都令人不太满意，所以决定引入 WebAssembly 技术，看看是否能带来不一样的提升。现在打开任意的爱奇艺直播间，在后面输入 __enablewasm__=true，就能打开 WebAssembly 转码模式，如下图所示：

![爱奇艺直播WebAssembly优化之路](https://up-img.yonghong.tech/pic/2020/07/28-17-57-b3ca2ddccc47784ef6ac973131e3e070-Hk2a6X.png)

体验上，两种模式都能满足流畅观看直播的需求。由此可见，WebAssembly 模块可以很完美地替换原来的 JavaScript 所写的转码模块。下面来看一下如何接入 WebAssembly。

## 接入 WebAssembly 的步骤

使用 WebAssembly 非常简单，总的来说，分为以下几步：

**1、使用 c 编写 flv 转 mp4 的代码**

首先定义 WebAssembly 被 js 调用的接口文件：

![爱奇艺直播WebAssembly优化之路](https://up-img.yonghong.tech/pic/2020/07/28-17-57-4bfde2b37f431818c42ad4a454405b45-tEikjQ.png)

如果想在被编译成 wasm 文件后可以被 JavaScript 调用，就需要在可以被外部调用的函数前使用 EM_PORT_API 来标识，这样在后面编译的时候 WebAssembly 就会将此函数作为可被 JavaScript 调用的方法抛出。

然后还需定义一些 WebAssembly 调用 JavaScript 的接口，如下面所示：

![爱奇艺直播WebAssembly优化之路](https://up-img.yonghong.tech/pic/2020/07/28-17-57-c2a9e99fd9f257008cd0e95077a3c3e3-0llF3W.png)

主要是通知 js 转换 mp4 流的头部信息和已经转好的部分流的缓存区地址等，实际调用的代码需要使用 EM_ASM_() 函数包起来，里面填上调用的 JavaScript 方法名和带的参数。

定义好接口后就是转码实现的部分了，这里涉及到 flv 和 mp4 格式的相关知识（对这两种格式不太了解的同学可以自行阅读相关文档）。整体转码采用 flv 和 mp4 双缓存区的模式，流程如下图所示：

![爱奇艺直播WebAssembly优化之路](https://up-img.yonghong.tech/pic/2020/07/28-17-57-d988c2a90f6888a8511f7d879709b6a3-Ongn5R.png)

a. JavaScript 获取到直播流后将流存入 flv 缓存区；

b. JavaScript 通知 WebAssembly 缓存区首地址和进度；

c. WebAssembly 请求缓存区数据；

d. WebAssembly 进行转码；

e. 将转好的 mp4 片段存入 mp4 缓存区；

f. WebAssembly 通知 JavaScript 转码进度；

最后由 JavaScript 通知原生播放器直接播放 mp4 缓存区的视频流。

**2、使用 emcc 编译出 flv2Mp4.js 和 flv2Mp4.wasm**

首先需要安装 emscripten 环境，安装和配置的具体步骤可以参考 emscripten 的[官网](https://emscripten.org/)。

安装完成后就可以使用emcc 命令编译c 文件了，使用命令 emcc main.c -s TOTAL_MEMORY=268435456 -g -o flvToMp4.js，最终可以得到两个文件，flvToMp4.js 和flvToMp4.wasm。

其中flvToMp4.wasm 是实际转码的code，flvToMp4.js 相当于接口文件，播放器可以通过引入flvToMp4.js 来加载wasm 文件和调用wasm 文件中的二进制代码。

通过阅读flvToMp4.js，我们可以发现自动生成初始化WebAssembly 的相关代码，获取WebAssembly 的二进制文件后，调用了WebAssembly.instantiate()，初始化了WebAssembly，并且在获取或加载wasm 文件失败后还能再次重试。

![爱奇艺直播WebAssembly优化之路](https://up-img.yonghong.tech/pic/2020/07/28-17-57-8c39550cbb1ab8375878aa9956f936ff-BYl4gv.png)

通过查看getBinaryPromise() 方法也可以看到下载的过程。



使用自动生成的代码，就基本可以不用管加载wasm 文件等问题，非常方便。

**3、对接编译好的 wasm 文件**

因为转码是高 cpu 的工作，所以将其放入 web_worker 中运行，这样不会阻碍主线程的渲染。

![爱奇艺直播WebAssembly优化之路](https://up-img.yonghong.tech/pic/2020/07/28-17-57-4e85e4a7eb56b77bef508d0771045ad3-7Y6cBL.png)

worker 创建后将事件和主线程对应绑定，也即绑定前面定义的 wasm 调用 JavaScript 的几个方法：

![爱奇艺直播WebAssembly优化之路](https://up-img.yonghong.tech/pic/2020/07/28-17-57-2161d4a1bb0259911194193d671f50aa-Ewh2We.png)

上面就是 WebAssembly 通知 JavaScript 的相关消息接口的定义，到此已经完成了整个转码过程的全部接口定义，全部流程就如下面的时序图所展示。

![爱奇艺直播WebAssembly优化之路](https://up-img.yonghong.tech/pic/2020/07/28-17-57-10ce45621b62b9db618bbac96c480e2a-9cWZh7.png)

由时序图可以看到播放器在收到流时就会初始化 WebAssembly 模块，初始化完成后进入转码阶段，通知 WebAssembly 进行转码并存入缓存区，再通知播放器播放。

## 使用 WebAssembly 实际性能对比

体验上能保持一致，那实际性能上有多少提升呢？还是要用数据说话。爱奇艺直播团队先后使用代码打点和浏览器自带的性能监测工具实时监测数据的方式来测试 WebAssembly 的实际使用性能。

**1、直播流转码效率情况**

首先，测试使用 WebAssembly 实际转码的速度。分别使用原来 JavaScript 所开发的转码模块和使用 WebAssembly 的转码模块进行转换，在实际直播间转换 flv 流数据包的前后进行打点计时，最终得到的数据如下所示：

![爱奇艺直播WebAssembly优化之路](https://up-img.yonghong.tech/pic/2020/07/28-17-57-33b4773fb18b449a019c2e51dd8992e8-FEHKAa.png)

前后各挑取了 30 包 flv 数据，表中第二列是每一包转码耗时，第三列是包的大小，在表的最后统计了总包的大小和总耗时，由此计算出未开启 WebAssembly 和开启 WebAssembly 的平均传输速率分别为 35305.6 字节 /s 和 46608.1 字节 /s。可以看出，WebAssembly 开启后转码速度的提升还是非常明显的。

**2、运行时浏览器资源消耗情况**

WebAssembly 实际应用在直播间中，能给直播间带来什么样的提升呢？最明显的是 cpu 占用率的下降。这一点可以通过使用 Chrome 浏览器自带的 Performance monitor 对使用 WebAssembly 前后的资源消耗做对比来证明。

![爱奇艺直播WebAssembly优化之路](https://up-img.yonghong.tech/pic/2020/07/28-17-57-e0878c89249cb60aa710756f3a04cbc6-cP8EkF.png)

如上图所示，可以在开发者工具 More tools 中找到 Performance monitor。通过这个工具，可以大概得到平时运行时的 cpu 占用率。下面两张图分别显示稳定播放时未开启 WebAssembly 和开启 WebAssembly 的 cpu 占用率情况：

- **未开启 WebAssembly**：

![爱奇艺直播WebAssembly优化之路](https://up-img.yonghong.tech/pic/2020/07/28-17-57-6c114b0987735353906bcb5af7e9480b-2kzUWt.png)

- **开启 WebAssembly**：

![爱奇艺直播WebAssembly优化之路](https://up-img.yonghong.tech/pic/2020/07/28-17-57-d694268ff2a13225c8ce3c1c186bd127-FKfVfE.png)

从图中可以大致看到，未开启 WebAssembly 时，cpu 占用率基本稳定在 7% 左右，而开启 WebAssembly 之后，cpu 占用率能稳定在 5% 上下，由此可以估算出大约有 10%-20% 的提升 (注：使用测试机型为 macbookpro 2018 款，cpu i7 2.2 GHz，不同机器测试出的性能可能有差别，波动状况也不完全一致，但在不同平台开启 WebAssembly 基本都能获得不同程度性能的提升)。

## WebAssembly 未来的更多可能

使用 WebAssembly 转码还只是 WebAssembly 的一个非常小的用处，爱奇艺直播团队还将使用 WebAssembly 技术实现更多有趣、有价值的功能，比如：

- **c++ 项目的移植**。现在很多图像相关的项目、算法都是由 c++ 编写的，如果想在浏览器上运行，以前就只能使用 JavaScript 重写一遍；而现在，通过 WebAssembly，只需要极小的改动，就使其能在浏览器上跑起来。
- **算法的加密**。由于 WebAssembly 编译成的 wasm 是二进制文件，反编译的成本很高，部分保密性比较强的算法会使用 WebAssembly 技术。
- **H.265 编码格式的支持**。H.265 编码方式凭借其出色的压缩比，被越来越多的产品所应用，但目前各主流浏览器原生还不支持 H.265 的硬解。但是也可以根据同样的思路，使用 WebAssembly 将 H.265 的流转化为 H.264 的流，然后再使用原生播放器播放，最终达到 Web 端播放 H.265 流的效果，这样可以极大地降低带宽成本。

得益于性能上的提升，WebAssembly 开始在各个领域崭露头脚，今后，爱奇艺直播团队也将尝试使用 WebAsssembly 实现更多的功能来优化爱奇艺的直播体验。

**本文转载自公众号爱奇艺技术产品团队（ID：iQIYI-TP）**。

**原文链接**：

**https://mp.weixin.qq.com/s/LRGNOuFwHXALs_lhPyN3Zw**