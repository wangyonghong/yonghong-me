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
- [数据人的“大考”：AnalyticDB如何强力支撑双11？](https://mp.weixin.qq.com/s/fyndobsiw4E5y_lXkrTBxw)
每年的双11都是云原生数据仓库AnalyticDB MySQL版（原分析型数据库MySQL版）的一块试金石。今年AnalyticDB除了在阿里数字经济体内进入更多核心交易链路，全力支撑双11以外，AnalyticDB全面拥抱云原生，构建极致弹性，大幅降低成本，释放技术红利，重磅发布了诸多全新企业级特性，让用户及时拥有极高性价比的云原生数据仓库。本文深度解析云原生数据仓库AnalyticDB面临的挑战和最新关键技术，分享双11护航背后的技术实践与经验。

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

## 近期会议公开课

### [2020 MongoDB 中国线上用户大会](https://www.mongodb.com/live-china-zh)

会议时间：11 月 24 日 星期二

报名链接：https://www.mongodb.com/live-china-zh

线上参会，全天精彩享不停！MongoDB重磅嘉宾主题演讲、头部客户使用心得分享、干货满满的多个分会场、动手实操培训，MongoDB 只为助您轻松构建可扩展、高性能、现代化应用程序。

### NGINX开源社区技术专题系列课程（安全专题）

报名链接：https://www.nginx.org.cn/article/detail/336

主题：使用ModSecurity/App Protect模块构建NGINX WAF

时间：11月25日下午2-3点

讲师：NGINX解决方案架构师邹俊


企业需要迅速将服务和应用推向市场，而快速将代码发布到生产环境中的压力使得安全性很容易下滑。过度依赖诸如漏洞扫描器之类的自动化工具是危险的，因为它们不能捕捉到所有问题。将各种跨功能开发团队提供的代码结合起来，就不太清楚谁负责实施安全性。在生产环境中运行多个应用和应用版本会使应用程序的防护层出现裂缝。

最终的结果是，对web应用防火墙（WAF）等安全工具的需求从未像现在这样迫切。这些安全工具通常与负载平衡代理集成，并部署在公司网络的边缘（或前门）以创建安全的外围环境。

安全不再是CISO和SecOps团队的唯一领域。DevOps团队在接受、测试和部署作为CI/CD管道一部分的安全策略方面扮演着重要角色。NGINX App Protect将F5先进WAF技术的有效性与NGINX的灵活性和性能相结合。它本机运行在NGINX Plus上，以解决现代DevOps环境面临的安全挑战。

通过本次公开课，您可以了解：
- NGINX WAF使用场景
- NGINX WAF vs NGINX App Protect
- NGINX App Protect策略配置
- KIC WAF策略配置

## 会议公开课资料

### 2020 Google 开发者大会 (Google Developer Summit)
Google 开发者大会 (Google Developer Summit) 是谷歌面向开发者展示最新产品和平台的年度盛会。2020 Google 开发者大会于 11 月 16 日 至 21 日举行，这是谷歌首次以全线上大会的形式与中国开发者相聚。本次大会以“代码不止”为主题，全面介绍了产品更新以及一系列面向本地开发者的技术支持内容，旨在赋能开发者高效创新、持续不断地创造愉悦的产品体验。

2020 Google 开发者大会 (Google Developer Summit) 全部视频 https://www.youtube.com/playlist?list=PLdcOMcDMrLrUmZuXRKtOlhDZGpsvQIXi7

2020 Google 开发者大会 主题演讲 https://youtu.be/5zO60HNQkWQ

2020 Google 开发者大会 技术演讲专场 Android、Google Play、ChromeOS https://youtu.be/N-x7tXYfOxE

2020 Google 开发者大会 技术演讲专场 Flutter、Web、Material Design https://youtu.be/4VLQMySQh8Q

2020 Google 开发者大会 技术演讲专场 TensorFlow、Google 女性开发者职业发展座谈会 https://youtu.be/Nu9zgUI5KTc

2020 Google 开发者大会 技术演讲专场 Google Cloud、Google Assistant、游戏和移动应用、Firebase https://youtu.be/yr8Axaje0C4

2020 Google 开发者大会 技术演讲专场 谷歌艺术与文化、ARCore by Google、WearOS by Google https://youtu.be/xqfpGAW8d_M

## 其他周报

- [科技爱好者周刊（第 134 期）：未来的游戏业比现在大100倍](https://github.com/ruanyf/weekly/blob/master/docs/issue-134.md)

- [Go语言爱好者周刊：第 70 期](https://github.com/polaris1119/golangweekly/blob/master/docs/issue-070.md)

- [2020.11.16 - KISS, SOLID, YAGNI And Other Fun Acronyms](https://github.com/zenany/weekly/blob/master/software/2020/1116.md)

- [老司机 iOS 周报 #137 | 2020-11-23](https://github.com/SwiftOldDriver/iOS-Weekly/blob/master/Reports/2020/%23137-2020.11.23.md)

- [R Weekly 2020-46 Open Acces, YAPOEH, Docker](https://rweekly.org/2020-46.html)

