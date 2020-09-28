---
title: 【国内镜像】CentOS 8 epel 阿里云镜像
categories:
- 国内镜像
tags:
- 国内镜像
- 镜像
- 镜像站
- aliyun
- 阿里
- 阿里云
- 阿里云镜像
- mirror
- 国内源
- 阿里源
- 开源
- 开源软件
- 开源软件镜像
- CentOS
- Linux
- epel
date: 2020-09-28 08:00:00
updated: 2020-09-28 08:42:00
---

CentOS Linux 是一个由社群支持的发行版本，它是由 Red Hat 或 CentOS git 公开的 Red Hat 企业级 Linux（RHEL）源代码所衍生出来的。因此，CentOS Linux 以兼容 RHEL 的功能为目标。CentOS 计划对组件的修改主要是去除上游提供者的商标及美工图。CentOS Linux 是免费的及可自由派发的。每个 CentOS 版本均获维护直至相等的 RHEL 版本支持被中止。新的 CentOS 版本会随著新版 RHEL 的出现而被重建 —— 次要版本约 6-12 个月发行一次，主要版本数年才发行一次。重建所需的时间由次要版本的数星期到主要版本的数月不等。这样做能创建一个安全、低维护、稳定、高预测性、高重复性的 Linux 环境。

EPEL(Extra Packages for Enterprise Linux)是由Fedora Special Interest Group维护的Enterprise Linux（RHEL、CentOS）中经 常用到的包。

## 添加epel源

```txt /etc/yum.repos.d/epel.repo
[epel]
name=Extra Packages for Enterprise Linux $releasever - $basearch
baseurl=https://mirrors.aliyun.com/epel/$releasever/Everything/$basearch
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-8

[epel-debuginfo]
name=Extra Packages for Enterprise Linux $releasever - $basearch - Debug
baseurl=https://mirrors.aliyun.com/epel/$releasever/Everything/$basearch/debug
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-8
gpgcheck=1

[epel-source]
name=Extra Packages for Enterprise Linux $releasever - $basearch - Source
baseurl=https://mirrors.aliyun.com/epel/$releasever/Everything/SRPMS
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-8
gpgcheck=1
```

<!-- more -->

## 相关链接

- https://developer.aliyun.com/mirror/centos
- https://developer.aliyun.com/mirror/epel
- https://developer.aliyun.com/mirror/ius
- https://mirrors.tuna.tsinghua.edu.cn/help/centos/
- https://mirrors.tuna.tsinghua.edu.cn/help/epel/
- [【国内镜像】CentOS 6 阿里云镜像](/mirror/centos-6-aliyun-mirror/)
- [【国内镜像】CentOS 7 阿里云镜像](/mirror/centos-7-aliyun-mirror/)
- [【国内镜像】CentOS 8 阿里云镜像](/mirror/centos-8-aliyun-mirror/)
- [【国内镜像】CentOS 6 清华镜像](/mirror/centos-6-tuna-mirror/)
- [【国内镜像】CentOS 7 清华镜像](/mirror/centos-7-tuna-mirror/)
- [【国内镜像】CentOS 8 清华镜像](/mirror/centos-8-tuna-mirror/)
- [【国内镜像】CentOS 6 epel 阿里云镜像](/mirror/centos-6-epel-aliyun-mirror/)
- [【国内镜像】CentOS 7 epel 阿里云镜像](/mirror/centos-7-epel-aliyun-mirror/)
- [【国内镜像】CentOS 8 epel 阿里云镜像](/mirror/centos-8-epel-aliyun-mirror/)
- [【国内镜像】CentOS 6 epel 清华镜像](/mirror/centos-6-epel-tuna-mirror/)
- [【国内镜像】CentOS 7 epel 清华镜像](/mirror/centos-7-epel-tuna-mirror/)
- [【国内镜像】CentOS 8 epel 清华镜像](/mirror/centos-8-epel-tuna-mirror/)
- [【国内镜像】CentOS 6 ius 阿里云镜像](/mirror/centos-6-ius-aliyun-mirror/)
- [【国内镜像】CentOS 7 ius 阿里云镜像](/mirror/centos-7-ius-aliyun-mirror/)
- [【国内镜像】CentOS 6 ius 清华镜像](/mirror/centos-6-ius-tuna-mirror/)
- [【国内镜像】CentOS 7 ius 清华镜像](/mirror/centos-7-ius-tuna-mirror/)
