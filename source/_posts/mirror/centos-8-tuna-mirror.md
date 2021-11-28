---
title: 【国内镜像】CentOS 8 清华镜像
categories:
- 国内镜像
tags:
- 国内镜像
- 镜像
- 镜像站
- tuna
- 清华
- 清华镜像
- mirror
- 国内源
- 清华源
- 开源
- 开源软件
- 开源软件镜像
- CentOS
- Linux
date: 2020-09-28 08:00:00
updated: 2020-09-28 08:44:00
indexing: false
---

CentOS Linux 是一个由社群支持的发行版本，它是由 Red Hat 或 CentOS git 公开的 Red Hat 企业级 Linux（RHEL）源代码所衍生出来的。因此，CentOS Linux 以兼容 RHEL 的功能为目标。CentOS 计划对组件的修改主要是去除上游提供者的商标及美工图。CentOS Linux 是免费的及可自由派发的。每个 CentOS 版本均获维护直至相等的 RHEL 版本支持被中止。新的 CentOS 版本会随著新版 RHEL 的出现而被重建 —— 次要版本约 6-12 个月发行一次，主要版本数年才发行一次。重建所需的时间由次要版本的数星期到主要版本的数月不等。这样做能创建一个安全、低维护、稳定、高预测性、高重复性的 Linux 环境。

## 替换镜像源

```txt /etc/yum.repos.d/CentOS-Base.repo
# CentOS-Base.repo
#
# The mirror system uses the connecting IP address of the client and the
# update status of each mirror to pick mirrors that are updated to and
# geographically close to the client.  You should use this for CentOS updates
# unless you are manually picking other mirrors.
#
# If the mirrorlist= does not work for you, as a fall back you can try the
# remarked out baseurl= line instead.
#
#



[BaseOS]
name=CentOS-$releasever - Base
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/BaseOS/$basearch/os/
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=BaseOS&infra=$infra
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial

[AppStream]
name=CentOS-$releasever - AppStream
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/AppStream/$basearch/os/
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=AppStream&infra=$infra
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial

[PowerTools]
name=CentOS-$releasever - PowerTools
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/PowerTools/$basearch/os/
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=PowerTools&infra=$infra
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial


#additional packages that may be useful
[extras]
name=CentOS-$releasever - Extras
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/extras/$basearch/os/
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial



#additional packages that extend functionality of existing packages
[centosplus]
name=CentOS-$releasever - Plus
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/centosplus/$basearch/os/
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=centosplus
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
```

<!-- more -->

## 恢复

```txt /etc/yum.repos.d/CentOS-Base.repo
# CentOS-Base.repo
#
# The mirror system uses the connecting IP address of the client and the
# update status of each mirror to pick mirrors that are updated to and
# geographically close to the client.  You should use this for CentOS updates
# unless you are manually picking other mirrors.
#
# If the mirrorlist= does not work for you, as a fall back you can try the
# remarked out baseurl= line instead.
#
#

[BaseOS]
name=CentOS-$releasever - Base
mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=BaseOS&infra=$infra
#baseurl=http://mirror.centos.org/$contentdir/$releasever/BaseOS/$basearch/os/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
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
