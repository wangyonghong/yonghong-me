---
title: 看看大厂是如何用云原生解决千万视频会议难题的
tags:
- 云原生
categories:
- 云原生
date: 2021-07-09 22:24:00
updated: 2021-07-09 22:24:00
---

## 腾讯：揭秘日活千万腾讯会议全量云原生化上TKE技术实践

文章链接：https://juejin.cn/post/6844904192830603272

本文总结了腾讯会议在TKE容器化部署时用到的平台相关特性，包括业务镜像自动分批灰度发布、ConfigMap分批灰度发布、Pod内A/B容器ms级切换发布、多集群发布管理、基于DynamicQuota的产品配额管理、探测节点和集群稳定性问题以提升自愈能力等。

## 华为：远程办公利器华为云WeLink，如何练就硬核抗压能力？

文章链接：https://zhuanlan.zhihu.com/p/106388133

业务快速增长带来的挑战聚焦在海量请求的冲击，从消息到语音模块、视频会议系统，华为云WeLink核心业务采用全容器化架构，结合华为云容器引擎单集群百万容器的超大规模支撑，可以迅速在新扩容的云服务器上启动业务，每秒最快可新增1000业务实例，大大降低了业务高峰时段的断线率、故障率和请求等待时长。更能通过瑶光的二次调度进行热点消除，保障计算资源压力的平均分布，助力业务平稳运行。

<!-- more -->

## 字节：字节跳动容器化场景下的性能优化实践

文章链接：https://www.infoq.cn/article/mu-1bFHNmrdd0kybgPXx

字节跳动资源调度团队负责私有云平台 TCE 的底层 Kubernetes 集群的开发和维护工作。TCE 托管了头条、抖音、字节国际化业务等内部上万个在线微服务。随着这些业务的快速发展，集群规模不断扩大，机器负载越来越高，运维难度和成本问题越发显著。原生 Kubernetes 作为控制面系统，并不能很好地解决这些问题。为了提升系统可见性，我们基于 eBPF 实现了系统监控，使内核能更好地理解微服务，极大地提升了问题诊断效率。为提升资源利用率，我们通过动态超售，实现了业务实例的高密度部署，并通过优化 Kubernetes 资源模型，有效保证了延时敏感服务的 QoS。

## 微软：Advancing Microsoft Teams on Azure—operating at pandemic scale

文章链接：https://azure.microsoft.com/en-us/blog/advancing-microsoft-teams-on-azure-operating-at-pandemic-scale/


## Zoom：Zoom deploys its core videoconferencing service on Oracle Cloud

文章链接：https://www.zdnet.com/article/zoom-deploys-its-core-videoconferencing-service-on-oracle-cloud/


## 声网：企业云原生创新与实践

视频链接：https://yunqi.aliyun.com/2020/session88?liveId=44191
