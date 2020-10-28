---
title: 微服务基础设施搭建必做的 4 件事
tags:
- 微服务
- 分布式
- RPC
categories:
- 学习笔记
date: 2020-10-24 17:00:00
updated: 2020-10-24 17:00:00
---

## 分布式系统中进程如何通信
由传统的函数调用变成跨网络的进程间通信(RPC)，通信中间件需要屏蔽复杂性，需要关注以下4点
- 公司的多语言诉求（多种语言需要要避开语言绑定的RPC框架）
- 性能方面 序列化协议
- 业务长期演进中通信框架替换成本
- 考虑通信框架背后的微服务组件生态是否完整（配置管理，服务发现，断路器，负载均衡）

RPC通讯框架的4个实践经验：
- 公司作战需要规范（趁早规范化、标准化）
- 具备服务异常保护机制（a.过载保护，节点，接口等，b.异常故障压制，弱化依赖，默认值，降级）
- 健壮的集群间容错策略（a.流量容错，b.调用端对端服务节点状态感知）
- 多样的调用方式支持多样的业务场景（异步，OneWay）

<!-- more -->
## 服务集群中节点和流量如何管理
问题一：单体应用中函数调用是基于内存中函数地址寻址，服务化后调用端如何找到对端节点？

![服务注册中心原理图](https://up-img.yonghong.tech/pic/2020/10/24-16-48-IMG_0034-NbTskD.PNG)

问题二：服务端扩容，调用端如何发现新节点并进行负载均衡？

![服务扩容原理图](https://up-img.yonghong.tech/pic/2020/10/24-17-17-IMG_0035-DBxxWH.PNG)

问题三：服务端个别节点宕机，如何自动使其失效避免调用端继续调用报错？

![异常节点摘除原理图](https://up-img.yonghong.tech/pic/2020/10/24-17-17-IMG_0036-78o40S.PNG)

场景一：单节点业务异常时，需要快速禁用异常节点。
场景二：对于服务发布时灰度的节点，期望降低其流量比例。
场景三：业务在多地域部署时，期望支持同地域优先级等个性化的路由策略。

![路由策略原理图](https://up-img.yonghong.tech/pic/2020/10/24-17-17-IMG_0037-9Q0Knr.PNG)

技术选型
- 经验一：系统要适当弱化对注册中心的依赖
- 经验二：趁早减少不必要的数据交互，规划扩容方案
- 经验三：有限保证可用性而非一致性（注册中心定位为AP系统而非CP系统）

## 系统复杂化后如何快速发现与定位异常
分布式系统监控的三大利器：
- 集中式的log日志系统
- metrics指标系统
- 分布式链路追踪tracing

推荐文章：Metrics, tracing, and logging

## 微服务拆分后团队组织如何变化

问题：按技术能力组织团队，协作效率低、不聚集导致专业度有限

建议：
- 按业务职能组织团队，聚集所属业务与产品
- 规模到一定程度，建设独立的基础技术团队

---

1024 程序员节快乐！