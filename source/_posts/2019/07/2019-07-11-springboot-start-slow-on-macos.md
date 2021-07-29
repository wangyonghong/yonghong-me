---
layout: post
title:  "解决Springboot在macOS上启动慢的问题"
category: "springboot"
tags: ["springboot", "启动慢", "macos", "macOS"]
date: 2019-07-11 00:00:00
updated: 2019-07-11 00:00:00
---

Springboot在其他人电脑上启动只需要3s，但是在我的电脑上却需要30s，这可能是Springboot在macOS上JDK1.8的一个bug，只要在host添加了你的主机名就正常了

<!-- more -->

## 查看自己的主机名

```sh
➜  hostname
wangyonghong.local
```

## 修改主机名

系统偏好设置 -> 共享 -> 电脑名称

## 添加host

```sh
sudo vim /etc/hosts

127.0.0.1       localhost wangyonghong.local
::1             localhost wangyonghong.local
```

改完之后，Springboot启动从30s变成了3s