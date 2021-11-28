---
title: 超链接中 utm_source, utm_medium 等参数的含义是什么？
tags:
- utm
categories:
- 转载
date: 2020-06-02 22:24:00
updated: 2020-06-02 22:24:00
---

> 作者：张溪梦 Simon
> 
> 链接：https://www.zhihu.com/question/48724061/answer/122730629
> 
> 来源：知乎
> 
> 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

在这里详细介绍下 UTM 的使用和含义。

UTM 除了最基础的追踪流量来源外，还可以根据不同渠道、不同内容做精细化运营分析，帮你对比区分优质和劣质渠道，提高流量在产品内的转化。

先来看一个结果：添加 UTM 参数的链接的链接投放后，我们就可以看到这样的统计了：

![img](https://up-img.yonghong.tech/pic/2020/06/02-16-34-4a97c5556403190d36124b826b4c454b_1440w-jgT6NZ.jpg)

<!--more-->

每一个渠道带来的流量都十分清晰，用户在产品内的行为也一目了然，是否注册了，是否最终购买了，都可以看到。我们可以看到讲述 heatmap 热图的这篇内容在渠道「微博 1」投放的链接，带来了 9992 个页面浏览量，2066 个注册用户量，以及 1614 个购买用户量。



而且不仅可以看到同一篇文章在不同渠道的流量情况，如 heatmap 热图这篇内容在微信、微博和其他渠道的推广情况；还可以看到同一个渠道不同文章带来的流量情况，如在微博渠道，heatmap 热图的文章的导流情况比 features 功能文章的导流情况更好。

用户在产品内的行为，有多少进行了注册，有多少完成了购买，清清楚楚，而且，我们还可以将不同渠道进行分组，查看不同渠道的用户留存和转化。

那么，我们先来看下，这样的 UTM 参数是怎样设置的呢？



**Part 1 | UTM 参数的设置**

通过 UTM 参数追踪外部流量的访问情况的原理是：把你投放在不同渠道的链接打上特定的标记，以监控各个链接的流量情况。

*1. 确定目标链接*

首先，确定这个链接最终指向的目标网页是哪个？一般来说是你自己的网站的某个页面，然后这个页面需要加载过数据统计分析工具的 SDK 。举个例子，如果使用 [GrowingIO](https://link.zhihu.com/?target=https%3A//www.growingio.com/%3Futm_source%3Dzhihu%26utm_medium%3Dqa%26utm_campaign%3Dq48724061%26utm_content%3D160919-utm%26utm_term%3Dtool) 进行接下来的拆解分析，就需要这个页面是加载过 Growing JS 代码的网址。不要以为在别人网站的链接后加上 UTM 参数，你就可以看到别人网站的点击情况了，这一切的前提是，链接最终指向加载了相应的分析代码的你自己的网站。

*2. 添加自定义的参数*

接下来，我们需要设置 UTM 的参数，也就是在链接上添加规则，进行标记，投放链接后我们就可以知道是哪个来源带来的流量了。对于不同的活动或文章，我们要设置不同的 UTM 参数用来区分。
说白了，这里就是你用各种各样的内容来描述这条链接是放在哪个活动、哪个来源上的，我们来看一个例子进行理解。

![img](https://up-img.yonghong.tech/pic/2020/06/02-16-34-1f3cfbaad4660f74969cd45807dceed1_1440w-TdUa7q.jpg)


以现在很常用的新媒体营销方式为例，我们在微信的阅读原文里放了一条引导流量的链接：
[https://www.growingio.com/?utm_source=zhihu&utm_medium=article&utm_campaign=product&utm_content=0811-tool&utm_term=tool](https://link.zhihu.com/?target=https%3A//www.growingio.com/%3Futm_source%3Dzhihu%26utm_medium%3Darticle%26utm_campaign%3Dproduct%26utm_content%3D0811-tool%26utm_term%3Dtool)



这条链接的意思是什么呢？

1. [https://www.growingio.com/](https://link.zhihu.com/?target=https%3A//www.growingio.com/%3Futm_source%3Dzhihu%26utm_medium%3Darticle%26utm_campaign%3Dproduct%26utm_content%3D0811-tool%26utm_term%3Dtool) 这条链接最终指向的地址；
2. [utm_source=zhihu](https://link.zhihu.com/?target=https%3A//www.growingio.com/%3Futm_source%3Dzhihu%26utm_medium%3Darticle%26utm_campaign%3Dproduct%26utm_content%3D0811-tool%26utm_term%3Dtool) 投放的渠道是知乎；
3. [utm_medium=article](https://link.zhihu.com/?target=https%3A//www.growingio.com/%3Futm_source%3Dzhihu%26utm_medium%3Darticle%26utm_campaign%3Dproduct%26utm_content%3D0811-tool%26utm_term%3Dtool) 媒介是一篇文章；
4. [utm_campaign=product](https://link.zhihu.com/?target=https%3A//www.growingio.com/%3Futm_source%3Dzhihu%26utm_medium%3Darticle%26utm_campaign%3Dproduct%26utm_content%3D0811-tool%26utm_term%3Dtool) 这篇文章是产品介绍系列的；
5. [utm_content=0811-tool](https://link.zhihu.com/?target=https%3A//www.growingio.com/%3Futm_source%3Dzhihu%26utm_medium%3Darticle%26utm_campaign%3Dproduct%26utm_content%3D0811-tool%26utm_term%3Dtool) 文章内容是「8.11 编辑，介绍工具」；
6. [utm_term=tool](https://link.zhihu.com/?target=https%3A//www.growingio.com/%3Futm_source%3Dzhihu%26utm_medium%3Darticle%26utm_campaign%3Dproduct%26utm_content%3D0811-tool%26utm_term%3Dtool) 文章的关键词是「tool」;



你一定会问，这个 URL “ ? ” 之后的参数都是什么？简单说，可以把 “ ? ” 之后的 UTM 参数理解为链接的名字，即为投放在不同渠道的每个链接起的分析工具能够识别的名字。

我们把这些信息连起来，这条 UTM 代表的含义就是：这个指向 [http://www.growingio.com/](https://link.zhihu.com/?target=http%3A//www.growingio.com) 的投放链接，是在 8 月 11 日 utm_content=0811-tool，知乎 utm_source=zhihu 的文章里 utm_medium=article 投放的，这篇文章是介绍工具 utm_term=tool 的产品文章 utm_campaign=product 。

当你在数据分析工具里做分析时，就可以像破解密码一样读出它的意思了，知道它放在了哪个内容里，用在了哪个活动里。

当我们有很多内容同时在各个渠道投放时，这样的链接就十分有用了，我们知道每个渠道每条内容带来的流量，也可以按照不同的渠道将流量进行分组，分析不同渠道带量的效果和质量。

我们提供的 UTM 参数和自定义参数的方式采用的是目前市面上最常用的定义方式：


![img](https://up-img.yonghong.tech/pic/2020/06/02-16-34-53be54fc398bdf52c97b7c77fdef6b54_1440w-ptcVns.jpg)


我们可以根据需要，进行各种各样自定义的填充，因为 UTM 最初是用在广告监控上的，所以它的很多名称还是关于广告的，但是我们现在已经可以把它放在各个内容、活动、推广中，监控渠道的流量情况。



具体的填写参数的意义和方法，可以根据下面这些情景进行灵活的变通。

*1. 当这条链接用于付费推广时，可以这样定义：*

![img](https://up-img.yonghong.tech/pic/2020/06/02-16-34-457a27ca5b2aceb7b8003a8f91f95e06_1440w-W4rIel.jpg)


*2. 当这条链接用于内容文章时，可以这样定义：*

![img](https://up-img.yonghong.tech/pic/2020/06/02-16-34-5f2af1e60a8a94bd9df0ff23a0026db3_1440w-YXLP30.jpg)


*3. 当这条链接用于活动时，可以这样定义：*

![img](https://up-img.yonghong.tech/pic/2020/06/02-16-34-aaee8514c40384b1fb4761b96c117a27_1440w-MGoCUz.jpg)



如果是你自己看这个数据，只要设置你能看懂的内容就可以，涉及到团队协作时，最好统一下标准，以便后续的数据分析。



**Part 2 | UTM使用的案例**

UTM 做好了之后，可以做哪些分析呢？我们就可以进行日常的监控和活动的监控了。

现在，我们知道哪些投放的渠道来的量高、哪些量低了，可以有的放矢地进行市场推广和渠道运营，我们可以用 UTM 里面的维度来制图，看一下这一周文章投放的效果：

![img](https://up-img.yonghong.tech/pic/2020/06/02-16-34-235999524bc591a9cef6f9bdfd60703c_1440w-byPf31.jpg)


接下来，你可能想了解更多细节，这些人都访问了哪些页面呢？比如说他们是否最终注册完成了呢？我们可以加上注册页面的指标来做图：

![img](https://up-img.yonghong.tech/pic/2020/06/02-16-34-8c4cdaf08d3bde47f3101e395e0deca5_1440w-ZSnevE.jpg)


这些都只是一个开始，接下来我们还可以做更有价值的数据分析，在漏斗里，用UTM参数作为不同的维度，可以对比不同来源不同内容的转化率：

![img](https://up-img.yonghong.tech/pic/2020/06/02-16-34-832f3ffac07d108828142e07d1967e67_1440w-oDNmLI.jpg)


借助 UTM，可以把流量来源、转化、ROI 都分析清楚。


