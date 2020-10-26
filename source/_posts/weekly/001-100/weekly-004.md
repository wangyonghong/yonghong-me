---
title: 技术爱好者周刊 第4期 | 2020年10月26日
permalink: /weekly-004/
tags:
- 技术爱好者周刊
- 即时编译
- 数据同步
- 平台架构
- 有赞
- RDD
- 架构
- 设计模式
categories:
- 技术爱好者周刊
date: 2020-10-26 10:24:00
updated: 2020-10-26 10:24:00
---

> 技术爱好者周刊，每周一发布，欢迎提[issue](https://github.com/wangyonghong/yonghong-me/issues)贡献内容。

## 后端

- [基本功 | Java即时编译器原理解析及实践](https://tech.meituan.com/2020/10/22/java-jit-practice-in-meituan.html)
跟其他常见的编程语言不同，Java将编译过程分成了两个部分，这就对性能带来了一定的影响。而即时（Just In Time, JIT）编译器能够提高Java程序的运行速度。本文会先解析一下即时编译器的原理，然后再分享一些在美团实践的经验，希望能对大家有所帮助或者启发。

<!-- more -->
## 架构

- [有赞保理业务架构设计与实践](https://tech.youzan.com/you-zan-bao-li-ye-wu-jia-gou-she-ji-yu-shi-jian/)
为保障消费者权益，有赞提供基础消费保障服务。买家确认收货后，资金才可结算到卖家店铺余额，普遍的结算周期在7天左右。从商家的角度出发，结算账期的产生使得资金周转变慢，这为扩大生产交易规模制造了困难。于是快速回款产品应运而生，有赞通过引入保理机构，以应收账款保理转让的模式来帮助商家实现资金快速回笼。
- [低代码在爱奇艺鹊桥数据同步平台的实践](https://mp.weixin.qq.com/s/IfYG7TgFK0rRN70cvIoPrQ)
本文结合爱奇艺App后端在业务数据同步方面的实践，分享基于低代码平台高效交付业务需求及避免重复开发的经验。
- [软件开发必修课：你该知道的GRASP职责分配模式](https://mp.weixin.qq.com/s/IaxAnWfVqe3mM0bHFVV5Gg)
阿里妹导读：软件开发为什么需要职责驱动设计（RDD）？职责应该如何分配？如何结合架构模式在实际开发中实践落地？本文介绍一种通用的职责分配模式——GRASP，通过举例详解GRASP的几大原则，并分享两个实际运用的案例。

## 近期会议

### [携程技术沙龙——大数据与AI技术实践](https://mp.weixin.qq.com/s/DCTALw91IDgykewyoGJk2Q)

报名链接：https://mp.weixin.qq.com/s/DCTALw91IDgykewyoGJk2Q

- 10月27日 19:00-20:00 Trip全球化指标平台建设 协程曾荣军
- 11月3日 19:00-20:00 大数据离在线混合部署技术方案 腾讯高廉墀
- 11月10日 19:00-20:00 携程机器翻译技术 携程余谦
- 11月17日 19:00-20:00 智能写稿技术在58部落内容社区的应用实践 58同城李忠

### [2020 MongoDB 中国线上用户大会](https://www.mongodb.com/live-china-zh)

会议时间：11 月 24 日 星期二

报名链接：https://www.mongodb.com/live-china-zh

线上参会，全天精彩享不停！MongoDB重磅嘉宾主题演讲、头部客户使用心得分享、干货满满的多个分会场、动手实操培训，MongoDB 只为助您轻松构建可扩展、高性能、现代化应用程序。

## 其他周报

- [科技爱好者周刊（第 130 期）：低龄化的互联网](https://github.com/ruanyf/weekly/blob/master/docs/issue-130.md)

- [Go语言爱好者周刊：第 66 期](https://github.com/polaris1119/golangweekly/blob/master/docs/issue-066.md)

- [2020.10.19 - The Developer Experience Gap](https://github.com/zenany/weekly/blob/master/software/2020/1019.md)

- [老司机 iOS 周报 #133 | 2020-10-26](https://github.com/SwiftOldDriver/iOS-Weekly/blob/master/Reports/2020/%23133-2020.10.26.md)

- [R Weekly 2020-42 Climate animation, NNMF in soccer, and Raspberry Pi with R](https://rweekly.org/2020-42.html)

