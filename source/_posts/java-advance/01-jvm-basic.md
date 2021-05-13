---
title: Java 进阶 01 —— 5 分钟回顾一下 Java 基础知识
tags:
- Java进阶
- JVM
categories:
- Java进阶
date: 2021-05-14 21:00:00
updated: 2021-05-14 21:00:00
---

## Java 生态圈

Java 是目前应用最为广泛的软件开发平台之一。随着 Java 以及 Java 社区的不断壮大，Java 也早已不再是简简单单的一门计算机语言了，它更是一个平台、一种文化、一个社区。

- 作为一个平台：Java 虚拟机扮演着举足轻重的作用。
  - Groovy、Scala、JRuby、Kotlin 等都是 Java 平台的一部分。
- 作为一种文化：Java 几乎成为了开源的代名词
  - 第三方开源软件和框架，如，Tomcat、Struts、MyBatis、Spring 等
  - 就连 JDK 和 JVM 自身也有不少开源的实现，如 OpenJDK、Harmony
- 作为一个社区，Java 拥有全世界最多的技术拥护者和开源社区的支持，有数不清的论坛和资料。从桌面应用软件、嵌入式开发到企业级应用、后台服务器、中间件，都可以看到 Java 的身影。其应用形式之复杂、参与人数之众也令人咋舌。

<!-- more -->

## Java 跨平台的语言

### Java 虚拟机规范

The Java Virtual Machine is the cornerstone of the Java platform. **It is the component of the technology responsible for its hardware- and operating system-independence**, the small size of its compiled code, and its ability to protect users from malicious programs.

The Java Virtual Machine is an abstract computing machine. Like a real computing machine, it has an instruction set and manipulates various memory areas at run time. It is reasonably common to implement a programming language using a virtual machine; the best-known virtual machine may be the P-Code machine of UCSD Pascal.

### JVM 跨语言的平台

随着 Java 7 的正式发布，Java 虚拟机的设计者们通过 JSR-292 规范基本实现在 Java 虚拟机平台上运行非 Java 语言编写的程序。

Java 虚拟机根本不关心运行在其内部的程序到底是使用何种编程语言编写的，它只关心“字节码”文件。也就是说，Java 虚拟机拥有语言无关性，并不会单纯地与 Java 语言“终身绑定”，只要其他编程语言的编译结果满足并包含 Java 虚拟机的内部指令集，符号表以及其他的辅助信息，他就是一个有效的字节码文件，就能够被虚拟机所识别并装载运行。

![Java 跨平台的语言](https://up-img.yonghong.tech/pic/2021/04/03-19-34-orUTHy-CAZ1Zb.png)

![源码跨平台和二进制跨平台](https://up-img.yonghong.tech/pic/2021/04/02-19-40-%E6%BA%90%E7%A0%81%E8%B7%A8%E5%B9%B3%E5%8F%B0%E5%92%8C%E4%BA%8C%E8%BF%9B%E5%88%B6%E8%B7%A8%E5%B9%B3%E5%8F%B0-R6Uzxy.png)

- Java、C++、Rust 的区别
  - C/C++ 完全相信而且惯着程序员，让大家自行管理内存，可以编写很自由的代码，但一 不小心就会造成内存泄漏等问题，导致程序崩溃。
  - Java/Golang 完全不相信程序员，但也惯着程序员。所有的内存生命周期都由 JVM 运行 时统一管理。 在绝大部分场景下，你可以非常自由的写代码，而且不用关心内存到底是 什么情况。 内存使用有问题的时候，我们可以通过 JVM 来进行信息相关的分析诊断和 调整。 这也是本课程的目标。
  - Rust 语言选择既不相信程序员，也不惯着程序员。 让你在写代码的时候，必须清楚明白 的用 Rust 的规则管理好你的变量，好让机器能明白高效地分析和管理内存。 但是这样 会导致代码不利于人的理解，写代码很不自由，学习成本也很高。

### 多语言混合编程

Java 平台上的多语言混合编程正在成为主流，通过特定领域的语言去解决特定领域的问题是当前软件开发应对日趋复杂的项目需求的一个方向。

试想一下，在一个项目之中，并行处理使用 Clojure 语言编写，展示层使用 JRuby/Rails，中间层则是 Java，每个应用层都将使用不同的编程语言来完成，而且，接口对每一层开发者都是透明的，各种语言之间的交互不存在任何困难，就像使用自己语言的原生 API 一样方便，因为他们最终都运行在一个虚拟机之上。

对于这些运行在虚拟机之上、Java 语言之外的语言，来自系统级的、底层的支持正在迅速增强，以 JSR-292 为核心的一系列项目和功能改进（如，Davinci Machine 项目、Nashorn 引擎、InvokeDynamic 指令、java.lang.invoke 包等），推动 Java 虚拟机从 Java 语言的虚拟机向多语言虚拟机发展。

### 两种架构

Java 编译器输入的指令流基本上是一种基于栈的指令集架构，另外一种指令集架构则是基于寄存器的指令集架构。

具体来说两种架构之间的区别：

- 基于栈式架构的特点
  - 设计和实现更简单，适用于资源受限的系统；
  - 避开了寄存器的分配难题：使用零地址指令方式分配；
  - 指令流中的指令大部分是零地址指令，其执行过程依赖于操作数。指令集更小，编译器容易实现；
  - 不需要硬件支持，可移植性更好，更好实现跨平台。
- 基于寄存器架构的特点
  - 典型的应用是 x86 的二进制指令集：比如传统的 PC 以及 Android 的 Davlik 虚拟机；
  - 指令集架构则完全依赖硬件，可移植性差；
  - 性能优秀和执行更高效；
  - 花费更少的指令去完成一项操作；
  - 在大部分情况下，基于寄存器架构的指令集往往都是一地址指令、二地址指令和三地址指令为主，而基于栈式架构的指令集却是以零地址指令为主。

#### 举例

同样执行 2+3 这种逻辑操作，其指令分别如下：

基于栈的计算流程（以 Java 虚拟机为例）：

```java
iconst_2 // 常量 2 入栈
istore_1
iconst_3 // 常量 3 入栈
istore_2
iload_1
iload_2
iadd     // 常量 2、3 出栈，执行相加
istore_0 // 结果 5 入栈
```

而基于寄存器的计算流程

```java
mov eax,2  // 将 eax 寄存器的值设置为 2
mov eax,3  // 使 eax 寄存器的值加 3
```

代码演示一下

```java
public class StackStruTest {
    public static void main(String[] a) {
        int i = 2 + 3;
    }
}
```

```shell
cd chapter_01
javac StackStruTest.java
javap -v StackStruTest
Classfile /Users/yonghong/Coding/jvm/song/chapter_01/StackStruTest.class
  Last modified 2020-11-17; size 277 bytes
  MD5 checksum 9a7da6f68b8101238c5ab826d90154c5
  Compiled from "StackStruTest.java"
public class StackStruTest
  minor version: 0
  major version: 52
  flags: ACC_PUBLIC, ACC_SUPER
Constant pool:
   #1 = Methodref          #3.#12         // java/lang/Object."<init>":()V
   #2 = Class              #13            // StackStruTest
   #3 = Class              #14            // java/lang/Object
   #4 = Utf8               <init>
   #5 = Utf8               ()V
   #6 = Utf8               Code
   #7 = Utf8               LineNumberTable
   #8 = Utf8               main
   #9 = Utf8               ([Ljava/lang/String;)V
  #10 = Utf8               SourceFile
  #11 = Utf8               StackStruTest.java
  #12 = NameAndType        #4:#5          // "<init>":()V
  #13 = Utf8               StackStruTest
  #14 = Utf8               java/lang/Object
{
  public StackStruTest();
    descriptor: ()V
    flags: ACC_PUBLIC
    Code:
      stack=1, locals=1, args_size=1
         0: aload_0
         1: invokespecial #1                  // Method java/lang/Object."<init>":()V
         4: return
      LineNumberTable:
        line 2: 0

  public static void main(java.lang.String[]);
    descriptor: ([Ljava/lang/String;)V
    flags: ACC_PUBLIC, ACC_STATIC
    Code:
      stack=1, locals=2, args_size=1
         0: iconst_5 // 直接返回了 5
         1: istore_1
         2: return
      LineNumberTable:
        line 4: 0
        line 5: 2
}
SourceFile: "StackStruTest.java"
```

由于跨平台的设计，Java 的指令都是根据栈来设计的。不同平台 CPU 架构不同，所以不能设计为基于寄存器的。优点是跨平台、指令集小，编译器容易实现；缺点是性能下降，实现同样的功能需要更多的指令。

时至今日，尽管嵌入式平台已经不是 Java 程序的主流运行平台了（准确来说是 HotSpot 虚拟机的宿主环境已经不局限于嵌入式平台了），那么为什么不将架构更换为基于寄存器的架构呢？

答：基于栈式架构的虚拟机跨平台、指令集小，编译器容易实现，在非资源受限的场景中也是可以使用的。

## JVM 的生命周期

### 虚拟机的启动

Java 虚拟机的启动时通过引导类加载器（bootstrap class loader）创建一个初始类（initial class）来完成的，这个类是由虚拟机的具体实现指定的。

### 虚拟机的执行

- 一个运行中的 Java 虚拟机有着一个清晰的任务：执行 Java 程序；
- 程序开始执行时他才运行，程序结束时他就停止；
- 执行一个所谓的 Java 程序的时候，真真正正在执行的是一个叫做 Java 虚拟机的进程。

### 虚拟机的退出

有如下的几种情况：

- 程序正常执行结束；
- 程序在执行过程中遇到了异常或错误而异常终止；
- 由于操作系统出现错误而导致 Java 虚拟机进程终止；
- 某线程调用 Runtime 类或 System 类的 exit 方法，或 Runtime 类的 halt 方法，并且 Java 安全管理器也允许这次 exit 或者 halt 操作；
- 除此之外，JNI（Java Native Interface）规范中描述了用 JNI Invocation API 来加载或卸载 Java 虚拟机时 Java 虚拟机的退出情况。

## JVM 发展历程

### Sun Classic VM

- 早在 1996 年 Java 1.0 版本的时候，Sun 公司发布了一款名为 Sun Classic VM 的 Java 虚拟机，它同时也是世界上第一款商用 Java 虚拟机，JDK 1.4 时完全被淘汰。
- 这款虚拟机内部只提供解释器。
- 如果使用 JIT 编译器，就需要进行外挂。但是一旦使用了 JIT 编译器，JIT 就会接管虚拟机的执行系统。解释器就不再工作。解释器和编译器不能配合工作。
- 现在 HotSpot 内置了此虚拟机。

### Exact VM

- 为了解决上一个虚拟机问题，JDK 1.2 时，Sun 提供了此虚拟机；
- Exact Memory Management: 准确式内存管理；
  - 也可以叫 Non-Conservative/Accurate Memory Management
  - 虚拟机可以知道内存中某个位置的数据具体是什么类型
- 具备现代高性能虚拟机的雏形
  - 热点探测
  - 编译器与解释器混合工作模式
- 只在 Solaris 平台短暂使用，其他平台上还是 Classic VM
  - 英雄气短，终被 HotSpot 虚拟机替换

### HotSpot

- HotSpot 历史
  - 最初由一家名为 Longview Technologies 的小公司设计
  - 1997 年，此公司被 Sun 收购；2009 年，Sun 公司被 Oracle 收购
  - JDK 1.3 时，HotSpot VM 成为默认虚拟机
- 目前 HotSpot 占有绝对的市场地位，称霸武林
  - 现在使用比较多的 JDK 8、JDK 11中默认的虚拟机是 HotSpot
  - Sun/Oracle JDk 和 OpenJDK 的默认虚拟机
- 从服务端、桌面端、嵌入式都有应用
- 名称中的 HotSpot 指的就是它的热点代码探测技术
  - 通过计数器找到最具编译价值代码，触发即时编译或栈上替换
  - 通过编译器与解释器协同工作，在最优的程序响应时间与最佳执行性能中取得平衡

### BEA 的 JRockit

- 专注于服务器应用
  - 它可以不太关注程序启动速度，因此 JRockit 内部不包含解释器实现，全部代码都是靠即时编译器编译后执行
- 大量的行业基准测试显示，JRockit JVM 是世界上最快的 JVM。
  - 使用 JRockit 产品，客户已经体验带了显著的性能提高（一些超过了 70%）和硬件成本的减少（达50%）。
- 优势：全面的 Java 运行时解决方案组合
  - JRockit 面向延迟敏感型应用的解决方案 JRockit Real Time 提供以毫秒或微秒级的 JVM 响应时间，适合财务，军事指挥，电信网络的需要。
  - MissionControl 服务套件，它是一组以极低的开销来监控、管理和分析生产环境中的应用程序的工具。
- 2008年，BEA 被 Oracle 收购

### IBM 的 J9

- 全称：IBM Technology for Java Virtual Machine，简称 IT4J，内部代号 J9
- 市场定位与 HotSpot 接近，服务端、桌面应用、嵌入式等多用途 VM
- 广泛应用于 IBM 的各种 Java 产品
- 目前，有影响力的三大商用虚拟机之一，也号称是世界上最快的虚拟机。
- 2017左右，IBM 发布了开源 J9 VM，命名为 OpenJ9，交给 Eclipse 基金会管理，也称为 Eclipse OpenJ9