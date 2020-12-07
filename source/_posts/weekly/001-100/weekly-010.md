---
title: 技术爱好者周刊 第10期 | 2020年12月07日
permalink: /weekly-010/
tags:
- 技术爱好者周刊
categories:
- 技术爱好者周刊
date: 2020-12-07 10:24:00
updated: 2020-12-07 10:24:00
---

> 技术爱好者周刊，每周一发布，欢迎提[issue](https://github.com/wangyonghong/yonghong-me/issues)贡献内容。


## 后端
- [ClickHouse集群搭建（一）](https://niocoder.com/2020/11/28/ClickHouse%E9%9B%86%E7%BE%A4%E6%90%AD%E5%BB%BA1/)
- [ClickHouse集群搭建（二）](https://niocoder.com/2020/11/29/ClickHouse%E9%9B%86%E7%BE%A4%E6%90%AD%E5%BB%BA2/)
ClickHouse 是俄罗斯的Yandex于2016年开源的列式存储数据库（DBMS），主要用于在线分析处理查询（OLAP），能够使用SQL查询实时生成分析数据报告。
- [ReentrantLock 的这几个问题，你都知道吗？](http://generalthink.github.io/2020/11/23/about-ReentrantLock-problems/)
之前分析 AQS 的时候，了解到 AQS 依赖于内部的两个 FIFO 队列来完成同步状态的管理，当线程获取锁失败的时候，会将当前线程以及等待状态等信息构造成 Node 对象并将其加入同步队列中，同时会阻塞当前线程。当释放锁的时候，会将首节点的 next 节点唤醒 (head 节点是虚拟节点)，使其再次尝试获取锁。
- [复杂环境下落地Service Mesh的挑战与实践](https://tech.meituan.com/2020/12/03/service-mesh-in-meituan.html)
在私有云集群环境下建设 Service Mesh ，往往需要对现有技术架构做较大范围的改造，同时会面临诸如兼容困难、规模化支撑技术挑战大、推广困境多等一系列复杂性问题。本文会系统性地讲解在美团在落地 Service Mesh 过程中，我们面临的一些挑战及实践经验，希望能对大家有所启发或者帮助。
- [CDN工作原理及其在淘宝图片业务中的应用](https://juejin.cn/post/6901479190244098062)
淘宝的图片访问，有98%的流量都走了CDN缓存，只有2%会回源到源站，节省了大量的服务器资源。但是，如果在用户访问高峰期，图片内容大批量发生变化，大量用户的访问就会穿透cdn，对源站造成巨大的压力。今年双11，淘宝鹿班的主图价格表达升级项目，就面临了这种挑战，让我们看看是如何解决的吧。
<!-- more -->

## 人工智能
- [CIKM 2020 | 一文详解美团6篇精选论文](https://tech.meituan.com/2020/12/03/cikm-2020-nlp.html)
AI平台/搜索与NLP部/NLP中心/知识图谱组共有六篇论文（其中4篇长文，2篇短文）被国际会议CIKM2020接收，这些论文是知识图谱组在多模态知识图谱、MT-BERT、Graph Embedding和图谱可解释性等方向上的技术沉淀和应用。


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

- [科技爱好者周刊（第 136 期）：利特伍德奇迹定律](https://github.com/ruanyf/weekly/blob/master/docs/issue-136.md)

- [Go语言爱好者周刊：第 72 期](https://github.com/polaris1119/golangweekly/blob/master/docs/issue-072.md)

- [2020.11.30 - FrontPage: The Good, The Bad, and The Ugly](https://github.com/zenany/weekly/blob/master/software/2020/1130.md)

- [老司机 iOS 周报 #138 | 2020-12-07](https://github.com/SwiftOldDriver/iOS-Weekly/blob/master/Reports/2020/%23137-2020.12.07.md)

- [R Weekly 2020-48 Your first R package, magrittr, engineering Shiny](https://rweekly.org/2020-48.html)

