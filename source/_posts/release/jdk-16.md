---
title: JDK 16 正式发布！
tags:
- release
- JDK
- Java
- ZGC
- GitHub
- Vector
- Metaspace
- Sealed
- instanceof
categories:
- release
date: 2021-04-03 10:00:00
updated: 2021-04-03 10:00:00
---

JDK 16 在 2021 年 3 月 16 日正式发布了，这次发布的主要功能有：

- JEP 338: Vector API (Incubator)
- JEP 347: Enable C++14 Language Features
- JEP 357: Migrate from Mercurial to Git
- JEP 369: Migrate to GitHub
- JEP 376: ZGC: Concurrent Thread-Stack Processing
- JEP 380: Unix-Domain Socket Channels
- JEP 386: Alpine Linux Port
- JEP 387: Elastic Metaspace
- JEP 388: Windows/AArch64 Port
- JEP 389: Foreign Linker API (Incubator)
- JEP 390: Warnings for Value-Based Classes
- JEP 392: Packaging Tool
- JEP 393: Foreign-Memory Access API (Third Incubator)
- JEP 394: Pattern Matching for instanceof
- JEP 395: Records
- JEP 396: Strongly Encapsulate JDK Internals by Default
- JEP 397: Sealed Classes (Second Preview)

<!-- more -->

---

### JEP 338: Vector API (Incubator)

Vector API 这是一个新的初始迭代孵化器模块，模块包：`jdk.incubator.vector`，用于表示在运行时可靠地编译到支持的 CPU 架构上的最佳矢量硬件指令的矢量计算。

### JEP 347: Enable C++14 Language Features

允许在 JDK 底层的 C ++ 源代码中使用 C ++ 14 的新语言特性，并且提供了在 HotSpot 虚拟机代码中，哪些代码使用了这些新特性的指南。

### JEP 357: Migrate from Mercurial to Git

将 OpenJDK 社区的源代码存储库从 Mercurial（hg）迁移到 Git。

### JEP 369: Migrate to GitHub

在 GitHub 上托管 OpenJDK 社区的 Git 存储库。

### JEP 376: ZGC: Concurrent Thread-Stack Processing

ZGC 是一种较新的垃圾回收器，指在解决 HotSpot 虚拟机中的 GC 停顿及可伸缩问题。

ZGC 最早是在 JDK 11 中集成进来的，在 [JDK 15](https://yonghong.tech/release/jdk-15/) 中正式转正。

这个版本则是为了让 ZGC 支持并发栈处理，解决了最后一个重大瓶颈，把 ZGC 中的线程栈处理从安全点移到了并发阶段。并且还提供了一种机制，使得其他 HotSpot 子系统可以通过该机制延迟处理线程栈。

### JEP 380: Unix-Domain Socket Channels

UNIX 域套接字通道，为 `java.nio.channels` 包中的套接字通道和服务端套接字通道 APIs 增加 Unix 域套接字通道所有特性支持。

UNIX 域套接字主要用于同一主机上的进程间通信（IPC），大部分方面与 TCP/IP套接字类似，不同的是 UNIX 域套接字是通过文件系统路径名寻址，而不是通过 IP 地址和端口号。

### JEP 386: Alpine Linux Port

在 x64 和 AArch64 平台体系结构上，将 JDK 移植到 Alpine Linux 以及使用 musl 作为其主要 C 语言库的其他 Linux 发行版中。

### JEP 387: Elastic Metaspace

弹性的元空间，可以帮助 HotSpot 虚拟机，将元空间中未使用的 class 元数据内存更及时地返回给操作系统，以减少元空间的内存占用空间。

另外，还简化了元空间的代码，以降低维护成本。

### JEP 388: Windows/AArch64 Port

将 JDK 移植到 Windows/ AArch64 平台系列。

### JEP 389: Foreign Linker API (Incubator)

引入了一个新的 API，该 API 提供了对本地 native 代码的静态类型访问支持。

### JEP 390: Warnings for Value-Based Classes

基于值的类的警告，将基础类型包装类指定为基于值的类，废除其构造函数以进行删除，从而提示新的弃用警告。并且提供了在任何基于值的类的实例上不正常进行同步的警告。

### JEP 392: Packaging Tool

提供了 jpackage 打包工具，可用于打包独立的 Java 应用程序。

jpackage 打包工具是在 JDK 14 中首次作为孵化工具引入的新特性，到了 JDK 15 它仍然还在孵化中，现在它终于转正了。

### JEP 393: Foreign-Memory Access API (Third Incubator)

外部内存访问 API（三次孵化中），引入了一个新的 API，可以帮助 Java 应用程序更安全、有效地访问 Java 堆之外的外部内存。

这个最早在 JDK 14 中成为孵化特性，JDK 15/ JDK 16 中继续二、三次孵化并对其 API 有了一些更新，这个可以在 JDK 17 中好好期待一下转正。

### JEP 394: Pattern Matching for instanceof

模式匹配 for instanceof，相当于是增强的 instanceof，在 JDK 14 中首次成为预览特性，在 JDK 16 中正式转正。

模式匹配的到来将使得 instanceof 变得更简洁、更安全，为什么这么说，请看下面的示例。

正常的 instanceof 写法：

```java

if (object instanceof IPad) {
    IPad iPad = (IPad) object;
    // ...
} else if (object instanceof IPhone) {
    IPhone iPhone = (IPhone) object;
    // ...
}
```

模式匹配的 instanceof 写法：

```java
if (object instanceof IPad iPad) {
    // ...
} else if (object instanceof IPhone iPhone) {
    // ...
}
```

判断、赋值一步到位。

### JEP 395: Records

简单来说，Records 就是一种新的语法糖，目的还是为了简化代码，在 JDK 14 中首次成为预览特性，在 JDK 16 中正式转正。

Records 可以在一定程度上避免低级冗余的代码，比如：constructors, getters, equals(), hashCode(), toString() 方法等，相当于 Lombok 的 @Data 注解，但又不能完全替代。

### JEP 396: Strongly Encapsulate JDK Internals by Default

JDK 内部默认强封装，JDK 16 开始对 JDK 内部大部分元素默认进行强封装，sun.misc.Unsafe 之类的关键内部 API 除外，从而限制对它们的访问。

此外，用户仍然可以选择自 JDK 9 以来的默认的宽松的强封装，这样可以帮助用户毫不费力地升级到未来的 Java 版本。

### JEP 397: Sealed Classes (Second Preview)

封闭类（二次预览），可以是封闭类和或者封闭接口，用来增强 Java 编程语言，防止其他类或接口扩展或实现它们。

### 参考

官方日志：

- [https://openjdk.java.net/projects/jdk/16/](https://openjdk.java.net/projects/jdk/16/)
- [https://jdk.java.net/16/release-notes](https://jdk.java.net/16/release-notes)


