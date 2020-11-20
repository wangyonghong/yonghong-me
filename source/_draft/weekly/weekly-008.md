---
title: 技术爱好者周刊 第8期 | 2020年11月23日
permalink: /weekly-008/
tags:
- 技术爱好者周刊
categories:
- 技术爱好者周刊
date: 2020-11-23 10:24:00
updated: 2020-11-23 10:24:00
---

> 技术爱好者周刊，每周一发布，欢迎提[issue](https://github.com/wangyonghong/yonghong-me/issues)贡献内容。

## 后端
- [干货 | 携程 Cilium+BGP 云原生网络实践](https://mp.weixin.qq.com/s/vX30d4sAX2oETnNh3uZlEA)
Cilium 是近两年最火的云原生网络方案之一。Cilium 的核心基于 eBPF，有两大亮点：基于 eBPF 的灵活、高性能网络，以及基于 eBPF 的 L3-L7 安全策略实现。携程 2019 年开始在生产环境使用 Cilium，本文将介绍 Cilium 在携程的落地情况，以及我们基于 Cilium 的、覆盖虚拟机、物理机和容器的云原生安全的一些探索。

## 前端
- [双十一SSR优化实践：秒开率提升新高度](https://juejin.cn/post/6896288990765252616)
会场是每年双十一的主角之一，会场的用户体验自然也是每年最关注的点。在日趋复杂的业务需求下，如何保障我们的用户体验不劣化甚至能更优化是永恒的命题。
今年（2020）我们在不改变现有架构，不改变业务的前提下，在会场上使用了 SSR 技术，将秒开率提高到了新的高度（82.6%）；也观察到在用户体验得到优化的同时，业务指标如 UV 点击率等也有小幅的增长（视不同业务场景有不同的提升，最大可达 5%），带来了不错的业务价值。
本文将从服务端、前端两个角度介绍我们在 SSR 上的方案与经验
1、前端在解决工程化、业务效果评估上的具体实践与方法论
2、服务端在解决前端模块代码于服务端执行、隔离和性能优化上的具体实践与方法论
- [爱奇艺知识移动端组件化探索和实践](https://mp.weixin.qq.com/s/DCrixXqnEnuHpYfUPjyACA)
组件化对于任何一个业务场景复杂的APP以及经过多次迭代之后的产品来说都是必经之路，组件化是指解耦复杂系统时将多个功能模块拆分、重组的过程。组件化要做的不仅仅是表面上看到的模块拆分解耦，其背后还有很多工作来支撑组件化的进行，例如结合业务特性的模块拆分策略、模块间的交互方式和构建系统等等。本文主要讲述爱奇艺知识APP如何结合自身的业务特点，探索和实践了一套高效的移动端组件化方案。

<!-- more -->

## 测试
- [基于chaosblade的故障注入平台实践](https://mp.weixin.qq.com/s/5e9cmqvvaIhNs8CNVJuNog)
当今社会互联网应用越来越广泛，用户量日益剧增。在人们对互联网服务的依赖性增大的同时，也对服务的可用性和体验感有了更高的要求。那么如何保障服务在运营过程中能一直给用户提供稳定的、不间断的、可靠可信的服务呢？例如一个金融产品，如果出现过一次问题，那可能带来巨大的损失。大家都知道金融产品的系统架构和服务逻辑是相当复杂的，至此大家都会第一时间联想到测试工程师，他们会通过单元测试、集成测试、性能测试等来验证服务的稳定性。但尽管如此，也是远远不够的，因为错误可以在任何时间以任何形式发生，尤其是对分布式系统。所以这里就需要引入混沌工程（Chaos Engineering）。

## 设计模式
- [设计模式最佳套路—— 愉快地使用策略模式](https://juejin.cn/post/6897011052601409549)
策略模式（Strategy Pattern）定义了一组策略，分别在不同类中封装起来，每种策略都可以根据当前场景相互替换，从而使策略的变化可以独立于操作者。比如我们要去某个地方，会根据距离的不同（或者是根据手头经济状况）来选择不同的出行方式（共享单车、坐公交、滴滴打车等等），这些出行方式即不同的策略。

## 大数据
- [Apache Kylin的实践与优化](https://tech.meituan.com/2020/11/19/apache-kylin-practice-in-meituan.html)
Apache Kylin是一个基于Hadoop大数据平台打造的开源OLAP引擎，它采用了多维立方体预计算技术，利用空间换时间的方法，将查询速度提升至亚秒级别，极大地提高了数据分析的效率，并带来了便捷、灵活的查询功能。
- [双汇大数据方案选型：从棘手的InfluxDB+Redis到毫秒级查询的TDengine](https://www.taosdata.com/blog/2020/11/17/2028.html)
双汇发展多个分厂的能源管控大数据系统主要采用两种技术栈：InfluxDB/Redis和Kafka/Redis/HBase/Flink，对于中小型研发团队来讲，无论是系统搭建，还是实施运维都非常棘手。经过对InfluxDB/Redis和TDengine大数据平台的功能和性能对比测试，最终将TDengine作为实施方案。

## 近期会议

### [2020 MongoDB 中国线上用户大会](https://www.mongodb.com/live-china-zh)

会议时间：11 月 24 日 星期二

报名链接：https://www.mongodb.com/live-china-zh

线上参会，全天精彩享不停！MongoDB重磅嘉宾主题演讲、头部客户使用心得分享、干货满满的多个分会场、动手实操培训，MongoDB 只为助您轻松构建可扩展、高性能、现代化应用程序。

## 其他周报

- [科技爱好者周刊（第 134 期）：未来的游戏业比现在大100倍](https://github.com/ruanyf/weekly/blob/master/docs/issue-134.md)

- [Go语言爱好者周刊：第 70 期](https://github.com/polaris1119/golangweekly/blob/master/docs/issue-070.md)

- [2020.11.16 - KISS, SOLID, YAGNI And Other Fun Acronyms](https://github.com/zenany/weekly/blob/master/software/2020/1116.md)

- [老司机 iOS 周报 #137 | 2020-11-23](https://github.com/SwiftOldDriver/iOS-Weekly/blob/master/Reports/2020/%23137-2020.11.23.md)

- [R Weekly 2020-46 Open Acces, YAPOEH, Docker](https://rweekly.org/2020-46.html)

