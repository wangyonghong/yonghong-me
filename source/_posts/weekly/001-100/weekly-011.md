---
title: 技术爱好者周刊 第11期 | 2020年12月14日
permalink: /weekly-011/
tags:
- 技术爱好者周刊
categories:
- 技术爱好者周刊
date: 2020-12-14 10:24:00
updated: 2020-12-14 10:24:00
---

> 技术爱好者周刊，每周一发布，欢迎提[issue](https://github.com/wangyonghong/yonghong-me/issues)贡献内容。


## 后端
- [C++服务编译耗时优化原理及实践](https://tech.meituan.com/2020/12/10/apache-kylin-practice-in-meituan.html)
大型C++工程项目，都会面临编译耗时较长的问题。不管是开发调试迭代、准入测试，亦或是持续集成阶段，编译行为无处不在，降低编译时间对提高研发效率来说具有非常重要意义。
- [爱奇艺微服务标准技术架构实践](https://mp.weixin.qq.com/s/2soLr1F0X7rc8fZ-2fTE6A)
为数以亿计的用户提供优质的视频服务的爱奇艺技术产品团队，为了适应业务的快速迭代和创新，并支撑海量的用户请求，很多团队都对各自的业务系统自发地进行了微服务架构的改造。
- [步入超高清视频时代视频编码技术的机遇与挑战——AV1时代要来了](https://mp.weixin.qq.com/s/lHGC9JeKb3okVuuQy3zCWg)
近些年随着视频行业的迅猛发展，尤其像短视频、点播、直播、VR等领域的爆发，人们对于高清、超高清视频体验的追求越来越强烈，流媒体平台如何在提升观众观看体验，同时降低播放成本，利用技术降低带宽消耗的同时又能最大化的还原视频的画质和质量，成为了重要的课题。
- [一文彻底理解 I/O 多路复用](https://mp.weixin.qq.com/s/LkCoaUE5sl88J90iVwln9A)
这里的关键点在于，我们事先并不知道一个文件描述对应的I/O设备是否是可读的、是否是可写的，在外设的不可读或不可写的状态下进行I/O只会导致进程阻塞被暂停运行。
- [10 张图告诉你，Kafka 是怎么做到支持百万级 TPS 的？](https://mp.weixin.qq.com/s/ViHKf9cB3n_IjS4LUHyzKQ)
谈到大数据传输都会想到 Kafka，Kafka 号称大数据的杀手锏，在业界有很多成熟的应用场景并且被主流公司认可。这款为大数据而生的消息中间件，以其百万级TPS的吞吐量名声大噪，迅速成为大数据领域的宠儿，在数据采集、传输、存储的过程中发挥着举足轻重的作用。在业界已经有很多成熟的消息中间件如：RabbitMQ, RocketMQ, ActiveMQ, ZeroMQ，为什么 Kafka 在众多的敌手中依然能有一席之地，当然靠的是其强悍的吞吐量。下面带领大家来揭秘。

<!-- more -->

## 大数据
- [Apache Arrow：一种适合异构大数据系统的内存列存数据格式标准](https://tech.ipalfish.com/blog/2020/12/08/apache_arrow_summary/)
本文介绍一种内存列存数据格式：Apache Arrow，它有一个非常大的愿景：提供内存数据分析 (in-memory analytics) 的开发平台，让数据在异构大数据系统间移动、处理地更快。同时，比较特别的是这个项目的启动形式与其他项目也不相同，Arrow 项目的草台班子由 5 个 Apache Members、6 个 PMC Chairs 和一些其它项目的 PMC 及 committer 构成，他们直接找到 ASF 董事会，征得同意后直接以顶级 Apache 项目身份启动。

## 近期会议

### 第十一届中国数据库技术大会（DTCC2020）

报名链接：http://dtcc.it168.com/

会议时间：2020年12月21日 ~ 1010年12月23日

2020年12月21日~12月23日，由 IT168 旗下 ITPUB 企业社区平台主办的第十一届中国数据库技术大会（DTCC2020），将在北京隆重召开。大会以“架构革新 高效可控”为主题，设置2大主会场，20+技术专场，将邀请超百位行业专家，重点围绕数据架构、AI与大数据、传统企业数据库实践和国产开源数据库等内容展开分享和探讨，为广大数据领域从业人士提供一场年度盛会和交流平台。

为了帮助更多企业落地数据项目实施方案，今年将继续开设多门深度培训课程，内容涵盖数据中台、去IOE实践、区块链技术、内核开发实践等。3天传统技术演讲+1天深度主题，将汇聚各行业精英、技术领袖、行业专家和数据英雄，带来超过100场主题演讲和超5场培训课程的头脑风暴，诚邀您的加入。

历经十年的积累与沉淀，如今的DTCC已然成为国内数据库领域的技术风向标，见证了整个行业的发展与演变。作为顶级的数据领域技术盛会，DTCC2020将继续秉承一贯的干货分享和实践指导原则，期待大家的热情参与！

### 第十届PostgreSQL中国技术大会

报名链接：http://pgconf2020.postgres.cn/

会议时间：2021年1月15日 ~ 2021年1月16日

2021年1月15～1月16日，由 PostgreSQL 中文社区主办的第十届《PostgreSQL 中国技术大会》将在南京索菲特银河大酒店现场隆重举办。

PostgreSQL 作为功能最强的的开源关系型数据库之一，得到了越来越多企业的推广和运用，也越来越受到广大技术爱好者的欢迎和重视。

本次大会以“开源，自研，新机遇”为主题。除了设立一个主会场外，还设立了多个分会场。大会汇聚了来自互联网、电商、教育，金融等各行业领域的专家，这将是 PostgreSQL 发展史上的又一次交流盛会。

## 其他周报

- [科技爱好者周刊（第 137 期）：Slack 被收购，以及企业的技术选型](https://github.com/ruanyf/weekly/blob/master/docs/issue-137.md)

- [Go语言爱好者周刊：第 73 期](https://github.com/polaris1119/golangweekly/blob/master/docs/issue-073.md)

- [2020.12.07 - Flying the Nest: WebThings Gateway 1.0](https://github.com/zenany/weekly/blob/master/software/2020/1207.md)

- [老司机 iOS 周报 #139 | 2020-12-14](https://github.com/SwiftOldDriver/iOS-Weekly/blob/master/Reports/2020/%23137-2020.12.14.md)

- [R Weekly 2020-49 ggplot2, static code analysis, visual CV](https://rweekly.org/2020-49.html)

