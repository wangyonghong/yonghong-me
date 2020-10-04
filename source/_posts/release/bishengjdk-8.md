---
title: 【release】毕昇 JDK 8 开源了！
tags:
- release
- JDK
- Java
- 毕昇
- bisheng
- bishengjdk
categories:
- release
date: 2020-10-04 21:00:00
updated: 2020-10-04 21:00:00
---

毕昇JDK是华为内部OpenJDK定制版Huawei JDK的开源版本，是一个高性能、可用于生产环境的OpenJDK发行版。Huawei JDK运行在华为内部500多个产品上，积累了大量使用场景和java开发者反馈的问题和诉求，解决了业务实际运行中遇到的多个问题，并在ARM架构上进行了性能优化，毕昇JDK运行在大数据等场景下可以获得更好的性能。毕昇JDK 8与Java SE标准兼容，目前仅支持Linux/AArch64平台。毕昇JDK同时是OpenJDK的下游，现在和未来也会持续稳定为OpenJDK社区做出贡献。

二进制可以从[这里](https://mirrors.huaweicloud.com/kunpeng/archive/compiler/bisheng_jdk/)下载。

<!-- more -->

## 平台支持

毕昇JDK 当前支持 `Linux/AArch64` 平台。

## 支持特性

**毕昇JDK已经升级至8u262版本**，感谢OpenJDK社区众多开发者的贡献，现在毕昇JDK也已支持JFR，它是默认关闭的，用户可以使用以下命令在java应用启动的时候启用JFR，您还需要一个jmc 7.0以上的版本来读取jfr dump文件。

```
java -XX:+FlightRecorder
```

[**快速序列化**](https://gitee.com/openeuler/bishengjdk-11/wikis/FastSerializer?sort_id=2879166) 对于一些需要使用Java原生序列化接口而无法使用第三方序列化框架的场景，我们对Java序列化做了一些优化，用户可以使用如下命令打开：

```
-XX:+UnlockExperimentalVMOptions -XX:+UseFastSerializer -DfastSerializerEscapeMode=true
```

该参数不能兼容所有序列化场景，对于`序列化对象在读写两端不一致`或者`classmeta信息在运行时发生改变`等场景，fastSerializer会无法支持，这时需要保证打开了`-DfastSerializerEscapeMode=true`选项保证可以回退到原生的序列化模式

## 安装指南

您可以使用tar压缩包格式或者yum源方式来安装JDK（Java Development Kit）或者JRE（Java Runtime Environment）。

JDK是JRE的超集，包含了JRE的所有内容，并包含javac/jdb等开发者必须的编译器和调试器。JRE提供运行时库、Java虚拟机和其他运行java应用程序所必须的组件。请注意JRE不只包含Java SE规范的内容，也包含一些规范之外java应用程序常用的内容。

用户可以通过以下两种方式来安装：

- tar压缩包格式（.tar.gz）：通过这种方式您可以将JDK安装到系统的任意位置，且不会和系统中其他JDK产生影响。但是这种方式会需要用户进行一些手动设置。详情请见下表。
- 从yum源安装：通过这种方式您可以将JDK安装到系统的某个固定路径中，并为所有用户提供，这种安装方式需要root权限。`当前只有openEuler操作系统支持该操作`，详情请见下表。

| 下载文件                                                     | 操作指南                                                     | 支持架构      | 安装所需权限 | Sha256                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------- | ------------ | ------------------------------------------------------------ |
| [bisheng-jdk-8u262-linux-aarch64.tar.gz](https://mirrors.huaweicloud.com/kunpeng/archive/compiler/bisheng_jdk/bisheng-jdk-8u262-linux-aarch64.tar.gz) | [在 Linux/AArch64 平台上安装JDK 8](https://gitee.com/openeuler/bishengjdk-8/wikis/%E6%AF%95%E6%98%87JDK%208%20%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97?sort_id=2891179#1) | Linux/AArch64 | 任何人       | [sha256](https://mirrors.huaweicloud.com/kunpeng/archive/compiler/bisheng_jdk/bisheng-jdk-8u262-linux-aarch64.tar.gz.sha256) |
| [bisheng-jre-8u262-linux-aarch64.tar.gz](https://mirrors.huaweicloud.com/kunpeng/archive/compiler/bisheng_jdk/bisheng-jre-8u262-linux-aarch64.tar.gz) | [在 Linux/AArch64 平台上安装JRE 8](https://gitee.com/openeuler/bishengjdk-8/wikis/%E6%AF%95%E6%98%87JDK%208%20%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97?sort_id=2891179#2) | Linux/AArch64 | 任何人       | [sha256](https://mirrors.huaweicloud.com/kunpeng/archive/compiler/bisheng_jdk/bisheng-jre-8u262-linux-aarch64.tar.gz.sha256) |
| 从yum源安装                                                  | 即将推出                                                     | *             | root权限     | *                                                            |

### 在 Linux/AArch64 平台上安装JDK 8

- 下载压缩包 [bisheng-jdk-8u262-linux-aarch64.tar.gz](https://mirrors.huaweicloud.com/kunpeng/archive/compiler/bisheng_jdk/bisheng-jdk-8u262-linux-aarch64.tar.gz).
- 进入到你想要将JDK安装的目录中，并将 .tar.gz 压缩包拷贝到当前目录。

```
$ cd /path/to/jdk
```

- 将 .tar.gz 压缩包解压缩：

```
$ tar zxvf bisheng-jdk-8u262-linux-aarch64.tar.gz
```

JDK的安装目录为 jdk-8u262.

- 如果您想节省磁盘空间，您可以删除 .tar.gz 压缩包。

### 在 Linux/AArch64 平台上安装JRE 8

- 下载压缩包 [bisheng-jre-8u262-linux-aarch64.tar.gz](https://mirrors.huaweicloud.com/kunpeng/archive/compiler/bisheng_jdk/bisheng-jre-8u262-linux-aarch64.tar.gz).
- 进入到你想要将JDK安装的目录中，并将 .tar.gz 压缩包拷贝到当前目录。

```
$ cd /path/to/jre
```

- 将 .tar.gz 压缩包解压缩：

```
$ tar zxvf bisheng-jre-8u262-linux-aarch64.tar.gz
```

JRE的安装目录为 jre-8u262.

## 参考文章

- [openeuler/bishengjdk-8](https://gitee.com/openeuler/bishengjdk-8)
