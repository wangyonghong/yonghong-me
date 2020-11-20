---
title: 技术爱好者周刊 第7期 | 2020年11月16日
permalink: /weekly-007/
tags:
- 技术爱好者周刊
categories:
- 技术爱好者周刊
date: 2020-11-16 10:24:00
updated: 2020-11-16 10:24:00
---

> 技术爱好者周刊，每周一发布，欢迎提[issue](https://github.com/wangyonghong/yonghong-me/issues)贡献内容。

## 后端
- [Java中9种常见的CMS GC问题分析与解决](https://tech.meituan.com/2020/11/12/java-9-cms-gc.html)
目前，互联网上 Java 的 GC 资料要么是主要讲解理论，要么就是针对单一场景的 GC 问题进行了剖析，对整个体系总结的资料少之又少。前车之鉴，后事之师，美团的几位工程师搜集了内部各种 GC 问题的分析文章，并结合个人的理解做了一些总结，希望能起到“抛砖引玉”的作用。
- [Java-Collectors常用的20个方法](https://niocoder.com/2020/11/15/Java-Collectors%E5%B8%B8%E7%94%A8%E7%9A%8420%E4%B8%AA%E6%96%B9%E6%B3%95/)
- [TDengine + EMQ X + Grafana 轻松搭建高效低成本的边缘侧工业互联网平台](https://www.taosdata.com/blog/2020/11/12/2007.html)
本文将介绍基于TDengine、EMQ X搭建一个集工业数据采集、汇聚、清洗、存储分析以及可视化展示等能力于一体的轻量级边缘计算工业互联网平台。在此方案基础上，读者可以根据自身需求调整方案设计，从而搭建满足实际业务需求的工业互联网平台，加速实现工业智能化转型。
- [微服务授权应该怎么做？](https://segmentfault.com/a/1190000037781574)
前后端鉴权是一个很大的话题，不同组织的鉴权方式各不相同，甚至对同一协议的业务实现也可能相去甚远。本文尝试从认证与授权两个维度来描述标题中的鉴权，大部分篇幅还是偏认证。
- [分布式系统！如何实现用户追踪和认证？](https://segmentfault.com/a/1190000037785314)
讲使用 spring security 等具体技术的资料已经很多了，这篇文章不打算写框架和代码的具体实现。我们会讨论认证和授权的区别，然后会介绍一些被业界广泛采用的技术，最后会聊聊怎么为 API 构建选择合适的认证方式。
- [一例 Go 编译器代码优化 bug 定位和修复解析](https://mp.weixin.qq.com/s/Tyl6dSb7mHBuqqN6WvEuaw)
本文中介绍了 Go 编译器的整体编译流程脉络和一个编译优化错误导致数据越界访问的 bug，并分析了对这个 bug 的排查和修复过程，希望能够借此让大家对 Go 编译器有更多的了解，在遇到类似问题时有排查思路。
- [服务注册中心 | 记一次Consul故障分析与优化](https://mp.weixin.qq.com/s/fJ22y7MQvkcNJkiAnMwcUg)
在微服务体系中，服务注册中心是最基础的组件，它的稳定性会直接影响整个服务体系的稳定性。本文主要介绍了爱奇艺微服务平台基于Consul的服务注册中心建设方式，与内部容器平台、API网关的集成情况，并重点记录了Consul遇到的一次故障，分析解决的过程，以及针对这次故障从架构上的优化调整措施。Consul 是近几年比较流行的服务发现工具，用于实现分布式系统的服务发现与配置。与其它分布式服务注册与发现的方案相比Consul 的方案更“一站式”，使用起来也较 为简单。他的主要应用场景为：服务发现、服务隔离、服务配置。


<!-- more -->

## 前端
- [干货 | 携程移动直播探索](https://mp.weixin.qq.com/s/fZOpnikrrWZYDHc9nIRjWQ)
直播行业大概在10年前就开始兴起了，秀场直播和游戏直播是pc时代比较成功的应用场景。现阶段，移动互联网的大规模普及，流量价格越来越便宜，移动视频直播异常火爆，随着各行各业的不断融合，直播带货超高的营业额，明星艺人、销售、秀场网红的涌入，直播行业迎来了空前的繁荣发展。从pc直播到渐渐火爆的移动直播，直播技术也在不断地更新迭代，趋于成熟。本文从直播流的选择、交互优化、快速迭代等方面介绍携程直播技术。

## 大数据
- [【技术猩球】​七牛云内部平台架构 QStreaming——轻量级大数据ETL的开发框架](https://blog.qiniu.com/archives/8938)
QStreaming is a framework that simplifies writing and executing ETLs on top of Apache Spark. It is based on a simple sql-like configuration file and runs on any Spark cluster
- [HDFS慢节点监控及处理](https://mp.weixin.qq.com/s/wP8MlQr6Q-Z542YzpBCZEA)
HDFS集群随着使用时间的增长，难免会出现一些“性能退化”的节点，主要表现为磁盘读写变慢、网络传输变慢，我们统称这些节点为慢节点。当集群扩大到一定规模，比如上千个节点的集群，慢节点通常是不容易被发现的。大多数时候，慢节点都藏匿于众多健康节点中，只有在客户端频繁访问这些有问题的节点，发现读写变慢了，才会被感知到。

## 人工智能
- [日均5亿字符翻译量，百毫秒内响应，携程机器翻译平台实践](https://tech.ctrip.com/articles/a_ai/11125/)
随着国际化进程的开展，携程正加速第三次创业，各部门及业务场景对多语种的需求日益增长，依靠译员或精通多语种的客服难以支撑持续扩大的自然文本翻译流量。机器翻译技术作为近年来人工智能领域在自然语言处理任务上探索的先驱，逐渐走出学术的象牙塔，开始为普通用户提供实时便捷的翻译服务，并已取得了显著的成效。在这样的形势下，针对旅游服务场景提供更高质量低成本的机器翻译服务成为了一个重要课题。

## 近期会议

### [2020 MongoDB 中国线上用户大会](https://www.mongodb.com/live-china-zh)

会议时间：11 月 24 日 星期二

报名链接：https://www.mongodb.com/live-china-zh

线上参会，全天精彩享不停！MongoDB重磅嘉宾主题演讲、头部客户使用心得分享、干货满满的多个分会场、动手实操培训，MongoDB 只为助您轻松构建可扩展、高性能、现代化应用程序。

## 其他周报

- [科技爱好者周刊（第 133 期）：贵州变瑞士，有没有可能？](https://github.com/ruanyf/weekly/blob/master/docs/issue-133.md)

- [Go语言爱好者周刊：第 69 期](https://github.com/polaris1119/golangweekly/blob/master/docs/issue-069.md)

- [2020.11.09 - 7GUIs: A GUI Programming Benchmark](https://github.com/zenany/weekly/blob/master/software/2020/1109.md)

- [老司机 iOS 周报 #136 | 2020-11-16](https://github.com/SwiftOldDriver/iOS-Weekly/blob/master/Reports/2020/%23136-2020.11.16.md)

- [R Weekly 2020-45 Publishing, Prefrontal Cortex, Parentheses](https://rweekly.org/2020-45.html)

