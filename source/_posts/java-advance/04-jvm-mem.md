---
title: Java 进阶 04 —— JVM 内存模型：堆和栈是什么？
tags:
- Java进阶
- JVM
categories:
- Java进阶
date: 2021-05-16 21:00:00
updated: 2021-05-16 21:00:00
---

## JVM 运行时数据区概述

内存是非常重要的系统资源，是硬盘和 CPU 的中间仓库及桥梁，承载着操作系统和应用程序的实时运行。JVM 内存布局规定了 Java 在运行过程中内存申请、分配、管理的策略，保证了 JVM 的高效稳定运行。不同的 JVM 对于内存的划分方式和管理机制存在着部分差异。结合 JVM 虚拟机规范，来讨论一下经典的 JVM 内存布局。

Java 虚拟机定义了若干种程序运行期间会使用到的运行时数据区，其中有一些会随着虚拟机启动而创建，随着虚拟机退出而销毁。而另外一些则是与线程一一对应的，这些与线对应的数据区域会随着线程开始和结束而创建和销毁。

<!-- more -->

### JVM 整体架构

![JVM 整体架构 - 英文](https://up-img.yonghong.tech/pic/2021/04/03-19-47-VusNfO-S1kg66.png)

---

![JVM 整体架构 - 中文](https://up-img.yonghong.tech/pic/2021/04/03-19-46-8oddUR-oMwPkk.png)


### JVM 系统线程

线程是一个程序里的运行单元。JVM 允许一个应用有多个线程并行的执行

在 HotSpot 虚拟机里，每个线程都与操作系统的本地线程直接映射。当一个 Java 线程准备好执行以后，此时一个操作系统的本地线程也同时创建。Java 线程执行终止后，本地线程也会回收

操作系统负责所有的线程的安排调度到任何一个可用的 CPU 上。一旦本地线程初始化成功，它就会调用 Java 线程中的人run() 方法

如果你使用 jconsole 或者是任何一个调试工具，都能看到在后台有许多线程在运行。这些后台线程不包括调用 public static void main(String[] args) 的 main 线程以及所有这个 main 线程自己创建的线程。

这些主要的后台系统线程在 HotSpot 虚拟机里主要是以下几个

- 虚拟机线程：这种线程的操作是需要 JVM 达到安全点才会出现。这些操作必须在不同的线程中发生的原因是他们都需要 JVM 达到安全点，这样堆才不会变化。这种线程的执行类型包括“stop-the-world”的垃圾收集，线程栈收集，线程挂起以及偏向锁撤销
- 周期任务线程：这种线程是时间周期事件的体现（比如中断），他们一般用于周期性操作的调度执行
- GC 线程：这种线程对在 JVM 里不同种类的垃圾收集行为提供了支持
- 编译线程：这种线程在运行时会将字节码编译成本地代码
- 信号调度线程：这种线程接收信号并发送给 JVM，在它内部通过调用适当的方法进行处理


## JVM 内存结构

![JVM内存结构](https://up-img.yonghong.tech/pic/2021/04/02-20-39-01-JVM%E5%86%85%E5%AD%98%E7%BB%93%E6%9E%84-OjY1mD.png)

- 每个线程只能访问自己的线程栈。
- 每个线程都不能访问（看不见）其他线程的局部变量。
- 所有原生类型的局部变量都存储在线程栈中，因此对其他线程是不可见的。
- 线程可以将一个原生变量值的副本传给另一个线程，但不能共享原生局部变量本身。
- 堆内存中包含了 Java 代码中创建的所有对象，不管是哪个线程创建的。其中也涵盖了包装类型（例如，Byte，Integer，Long等）。
- 不管是创建一个对象并将其值赋值给局部变量，还是赋值给另一个对象的成员变量，创建的对象都会被保存到堆内存中。

---

- 如果是原生数据类型的局部变量，那么它的内容就全部保留在线程栈上。 
- 如果是对象引用，则栈中的局部变量槽位中保存着对象的引用地址，而实际的对象内容保存在堆中。
- 对象的成员变量与对象本身一起存储在堆上，不管成员变量的类型是原生数据类型，还是对象引用。
- 类的静态原生变量和静态变量对象的引用则和类定义一样都保存在方法区中。类的静态变量对象的值保存在堆中。

---

- 总结一下：方法中使用的原生数据类型和对象引用地址在栈上存储；对象、对象成员与类静态变量对象的值在堆上；类定义、静态原生变量、静态对象的引用在方法区中。
- 堆内存又称为“共享堆”，堆中的所有对象，可以被所有线程访问，只要他们能拿到对象的引用地址。
- 如果一个线程可以访问某个对象时，也就可以访问该对象的成员变量。
- 如果两个线程同时调用某个对象的同一方法，则它们都可以访问到这个对象的成员变量，但每个线程的局部变量副本是独立的。


## JVM 内存整体结构

![JVM内存整体结构](https://up-img.yonghong.tech/pic/2021/04/02-20-41-01-JVM%E5%86%85%E5%AD%98%E6%95%B4%E4%BD%93%E7%BB%93%E6%9E%84-eSeqP8.png)

- 每启动一个线程，JVM就会在栈空间栈分配对应的线程栈，比如 1MB 空间（-Xss1m） 
- 线程栈也叫做 Java 方法栈。如果使用了 JNI 方法，则会分配一个单独的本地方法栈（Native Stack） 
- 线程执行过程中，一般会有多个方法组成调用栈（Stack Trace），比如 A 调用 B，B 调用 C 。每执行到一个方法，就会创建对应的栈帧（Frame）。


## JVM 栈内存机构

![JVM栈内存结构](https://up-img.yonghong.tech/pic/2021/04/02-20-44-01-JVM%E6%A0%88%E5%86%85%E5%AD%98%E7%BB%93%E6%9E%84-Z8QlQS.png)

- 栈帧是一个逻辑上的概念，具体的大小在一个方法编写完成后基本上就能确定。 
- 比如返回值，需要有一个空间存放吧，每个局部变量都需要对应的地址空间，此外还有给指令使用的操作数栈，以及 Class 指针（标识这个栈帧对应的是哪个类的方法，指向非堆里面的 Class 对象）。

## JVM 堆内存结构

![JVM堆内存结构](https://up-img.yonghong.tech/pic/2021/04/02-20-45-01-JVM%E5%A0%86%E5%86%85%E5%AD%98%E7%BB%93%E6%9E%84-0TRoeN.png)

![jconsole内存](https://up-img.yonghong.tech/pic/2021/04/02-20-46-01-jconsole%E5%86%85%E5%AD%98-KNrKkU.png)

- 堆内存是所有线程共用的内存空间，JVM 将 Heap 内存分为年轻代（Young generation）和老年代（Old generation，也叫 Tenured）两部分。
- 年轻代还划分为3个内存池，伊甸园区（Eden space）和存活区（Survivor space），在大部分GC算法中有两个存活区（S0，S1），在我们可以观察到的任何时刻，S0和S1总有一个是空的，但一般很小，也浪费不了多少空间。
- Non-Heap本质上还是Heap，只是一般不归GC管理，里面划分为3个内存区池。
- Metaspace 以前叫持久代（永久代，Permanent generation），Java 换了个名字叫 Metaspace
- CCS Compressed Class Space，存放 class 信息的，和 Metaspace 有交叉
- Code Cache，存放 JIT 编译器编译后的本地机器代码。

## CPU 与内存行为

![计算机硬件架构](https://up-img.yonghong.tech/pic/2021/04/02-20-47-01-%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A1%AC%E4%BB%B6%E6%9E%B6%E6%9E%84-3aWMrH.png)

- CPU 乱序执行
- volatile 关键字
- 原子性操作
- 内存屏障

## Java对象模型

![Java对象模型](https://up-img.yonghong.tech/pic/2021/04/02-20-47-01-Java%E5%AF%B9%E8%B1%A1%E6%A8%A1%E5%9E%8B-K1uNvD.png)


## Java内存模型

![Java内存模型](https://up-img.yonghong.tech/pic/2021/04/02-20-47-01-Java%E5%86%85%E5%AD%98%E6%A8%A1%E5%9E%8B-G12dzM.jpg)

JMM 规范对应的是 JSR-133 Java Memory Model and Thread Specification 《Java 语言规范》 $17.4 Memory Model 章节

JMM 规范明确定义了不同的线程之间通过哪些方式，在什么时候可以看见其他线程保存到共享变量中的值；以及在必要时，如何对共享变量的访问进行同步。这样的好处是屏蔽各种硬件平台的操作系统之间的内存访问差异，实现了Java并发程序真正的跨平台。

- 所有的对象（包括内部的实例成员变量），static 变量，以及数组，都必须存放到堆内存中。
- 局部变量，方法的形参/入参，异常处理语句的入参不允许在线程之间共享，所以不受内存模型的影响。
- 多个线程同时对一个变量访问时【读取/写入】，这时候只要有某个线程执行的是写操作，那么这种现象称之为“冲突”。
- 可以被其他线程影响或感知的操作，称为线程间的交互行为，可分为：读取、写入、同步操作、外部操作等等。其中同步操作包括：对 volatile 变量的读写，对管程（monitor）的锁定与解锁，线程的起始操作与结尾操作，线程启动和结束等等。外部操作则是指对线程执行环境之外的操作，比如停止其他线程等等。
- JMM 规范的是线程间的交互操作，而不管线程内部对局部变量进行的操作。

---

## JVM 启动参数

- 以 - 开头为标准参数，所有的 JVM 都要实现这些参数，并且向后兼容。例，`-server`
- -D 设置系统属性。例，`-Dfile.encoding=UTF-8`
- 以 -X 开头为非标准参数，基本都是传给 JVM 的，默认 JVM 实现这些参数的功能，但是并不保证所有 JVM 实现都满足，且不保证向后兼容。可以使用 `java -X` 命令来查看当前 JVM 支持的非标准参数。例，`-Xmx8g`
- 以 -XX: 开头为非稳定参数，专门用于控制 JVM 的行为，跟具体的 JVM 实现有关，随时可能会在下个版本取消。
  - -XX: +-Flags 形式，+-是对布尔值进行开关。例，`-XX:+UseG1GC`
  - -XX: key=value 形式，指定某个选项的值。例，`-XX:MaxPermSize=256m`

1.系统属性参数

```java
-Dfile.encoding=UTF-8
-Duser.timezone=GMT+08
-Dmaven.test.skip=true
-Dio.netty.eventLoopThreads=8

// 还可以这样
System.setProperty("a", "A100");
String a = System.getProperty("a");
```

2.运行模式参数

- -server: 设置 JVM 使用 server 模式，特点是启动速度比较慢，但运行时性能和内存管理效率很高，适用于生产环境。在具有 64 位能力的 JDK 环境下将默认启用该模式，而忽略 -client 参数。
- -client: JDK1.7 之前在32位的 x86 机器上的默认值是 -client 选项。设置 JVM 使用 client 模式，特点是启动速度比较快，但运行时性能和内存管理效率不高，通常用于客户端应用程序或者 PC 应用开发和调试。此外，我们知道 JVM 加载字节码后，可以解释执行，也可以编译成本地代码再执行，所以可以配置 JVM 对字节码的处理模式。
- -Xint: 在解释模式(interpreted mode)下运行，-Xint 标记会强制 JVM 解释执行所有的字节码，这当然会降低运行速度，通常低10倍或更多。
- -Xcomp: -Xcomp 参数与 -Xint 正好相反，JVM 在第一次使用时会把所有的字节码编译成本地代码，从而带来最大程度的优化。【注意预热】
- -Xmixed: -Xmixed 是混合模式，将解释模式和编译模式进行混合使用，有 JVM 自己决定，这是 JVM 的默认模式，也是推荐模式。 我们使用 java -version 可以看到 mixed mode 等信息。

3.堆内存设置参数

- -Xmx, 指定最大堆内存。 如 -Xmx4g. 这只是限制了 Heap 部分的最大值为4g。这个内存不包括栈内存，也不包括堆外使用的内存。
- -Xms, 指定堆内存空间的初始大小。 如 -Xms4g。 而且指定的内存大小，并不是操作系统实际分配的初始值，而是GC先规划好，用到才分配。专用服务器上需要保持 –Xms 和 –Xmx 一致，否则应用刚启动可能就有好几个 FullGC。 当两者配置不一致时，堆内存扩容可能会导致性能抖动。
- -Xmn, 等价于 -XX:NewSize，使用 G1 垃圾收集器 不应该 设置该选项，在其他的某些业务场景下可以设置。官方建议设置为 -Xmx 的 1/2 ~ 1/4.
- -XX:MaxPermSize=size, 这是 JDK1.7 之前使用的。Java8 默认允许的 Meta空间无限大，此参数无效。
- -XX:MaxMetaspaceSize=size, Java8 默认不限制 Meta 空间, 一般不允许设置该选项。
- -XX:MaxDirectMemorySize=size，系统可以使用的最大堆外内存，这个参数跟 -Dsun.nio.MaxDirectMemorySize 效果相同。
- -Xss, 设置每个线程栈的字节数，影响栈的深度。 例如 -Xss1m 指定线程栈为 1MB，与-XX:ThreadStackSize=1m 等价

1. 如果什么都不配置会如何?
2. Xmx 是否与 Xms 设置相等?
3. Xmx 设置为机器内存的什么比例合适?
4. 作业: 画一下 Xmx、Xms、Xmn、Meta、DirectMemory、Xss 这些内存参数的关系

4.GC设置参数

- -XX:+UseG1GC:使用 G1 垃圾回收器 
- -XX:+UseConcMarkSweepGC:使用 CMS 垃圾回收器 
- -XX:+UseSerialGC:使用串行垃圾回收器 
- -XX:+UseParallelGC:使用并行垃圾回收器
- -XX:+UnlockExperimentalVMOptions -XX:+UseZGC // Java 11+
- -XX:+UnlockExperimentalVMOptions -XX:+UseShenandoahGC // Java 12+

各个 JVM 版本的默认 GC 是什么?

5.分析诊断参数

- -XX:+-HeapDumpOnOutOfMemoryError 选项, 当 OutOfMemoryError 产生，即内存溢出(堆内存或持久代)时，自动 Dump 堆内存。
  - 示例用法: java -XX:+HeapDumpOnOutOfMemoryError -Xmx256m ConsumeHeap
- -XX:HeapDumpPath 选项, 与 HeapDumpOnOutOfMemoryError 搭配使用, 指定内存溢出时 Dump 文件的目 录。如果没有指定则默认为启动 Java 程序的工作目录。
  - 示例用法: java -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/usr/local/ ConsumeHeap 
  - 自动 Dump 的 hprof 文件会存储到 /usr/local/ 目录下
- -XX:OnError 选项, 发生致命错误时(fatal error)执行的脚本。
  - 例如, 写一个脚本来记录出错时间, 执行一些命令, 或者 curl 一下某个在线报警的 url. 示例用法:java -XX:OnError="gdb - %p" MyApp
  - 可以发现有一个 %p 的格式化字符串，表示进程 PID。
- -XX:OnOutOfMemoryError 选项, 抛出 OutOfMemoryError 错误时执行的脚本。 
- -XX:ErrorFile=filename 选项, 致命错误的日志文件名,绝对路径或者相对路径。
- -Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=1506，远程调试

6.JavaAgent参数

Agent 是 JVM 中的一项黑科技, 可以通过无侵入方式来做很多事情，比如注入 AOP 代码，执行统计等等，权限非常大。这里简单介绍一下配置选项，详细功能需要专门来讲。

设置 agent 的语法如下:

- -agentlib:libname[=options] 启用 native 方式的 agent, 参考 LD_LIBRARY_PATH 路径。
- -agentpath:pathname[=options] 启用 native 方式的 agent。
- -javaagent:jarpath[=options] 启用外部的 agent 库, 比如 pinpoint.jar 等等。
- -Xnoagent 则是禁用所有 agent。 以下示例开启 CPU 使用时间抽样分析:
  - JAVA_OPTS="-agentlib:hprof=cpu=samples,file=cpu.samples.log"
