---
title: JDK 15 正式发布！
tags:
- release
- JDK
- Java
- JEP
- EdDSA
- ZGC
- Records
categories:
- release
date: 2020-09-27 20:00:00
updated: 2020-09-27 20:00:00
---

JDK 15 在 2020 年 9 月 15 号正式发布了，这次发布的主要功能有：

- JEP 339：EdDSA 数字签名算法
- JEP 360：密封类（预览）
- JEP 371：隐藏类
- JEP 372：删除 Nashorn JavaScript 引擎
- JEP 373：重新实现 Legacy DatagramSocket API
- JEP 374：重新实现 DatagramSocket API
- JEP 375：实例模式匹配（第二次预览）
- JEP 377：ZGC：一个可扩展的低延迟垃圾收集器
- JEP 378：文本块
- JEP 379：低暂停时间垃圾收集器
- JEP 381：移除 Solaris 和 SPARC 端口
- JEP 383：外部存储器访问 API（第二个内置程序）
- JEP 384：Records（第二次预览）
- JEP 385：不推荐的 RMI 激活去除

> JEP：JDK Enhancement Proposals，JDK 增强建议，也就是 JDK 的特性新增和改进提案。

<!-- more -->

这些年发布的版本对应的 JEPs 数量如下图所示：![img](https://up-img.yonghong.tech/pic/2020/09/27-11-07-a746bdfa-704a-439e-bd9c-883fa7e014cd-0oQ7ia.png)



### 发布版本说明

根据发布的规划，这次发布的 JDK 15 将是一个短期的过度版，只会被 Oracle 支持（维护）6 个月，直到明年 3 月的 JDK 16 发布此版本将停止维护。而 Oracle 下一个长期支持版（LTS 版）会在明年的 9 月份候发布（Java 17），LTS 版每 3 年发布一个，上一次长期支持版是 18 年 9 月发布的 JDK 11。



### JDK 15 新功能说明

JDK 15 为用户提供了十四项主要的增强/更改，包括一个孵化器模块，三个预览功能，两个不推荐使用的功能以及两个删除功能。



#### 1、EdDSA 数字签名算法

新加入 Edwards-Curve 数字签名算法（EdDSA）实现加密签名。在许多其它加密库（如 OpenSSL 和 BoringSSL）中得到支持。与 JDK 中的现有签名方案相比，EdDSA 具有更高的安全性和性能。这是一个新的功能。



#### 2、隐藏类

此功能可帮助需要在运行时生成类的框架。框架生成类需要动态扩展其行为，但是又希望限制对这些类的访问。隐藏类很有用，因为它们只能通过反射访问，而不能从普通字节码访问。此外，隐藏类可以独立于其他类加载，这可以减少框架的内存占用。这是一个新的功能。



#### 3、重新实现 DatagramSocket API

重新实现旧版 DatagramSocket API，更简单、更现代的实现来代替`java.net.DatagramSocket`和`java.net.MulticastSocket`API 的基础实现，提高了 JDK 的可维护性和稳定性。



#### 4、ZGC 功能转正

ZGC 已由JEP 333集成到JDK 11 中，其目标是通过减少 GC 停顿时间来提高性能。借助 JEP 377，ZGC 从预览功能转变为生产功能。



#### 5、文本块功能转正

文本块由JEP 355在 2019 年提出，文本块是一种多行字符串文字，它避免了大多数转义序列的需要，以一种可预测的方式自动设置字符串的格式，并在需要时使开发人员可以控制格式。借助 JEP 378，文本块已成为 Java 语言的永久功能。



#### 6、Shenandoah 垃圾回收算法转正

Shenandoah 垃圾回收从实验特性变为产品特性。这是一个从 JDK 12 引入的回收算法，该算法通过与正在运行的 Java 线程同时进行疏散工作来减少 GC 暂停时间。Shenandoah 的暂停时间与堆大小无关，无论堆栈是 200 MB 还是 200 GB，都具有相同的一致暂停时间。



#### 7、密封类（预览）

通过密封的类和接口来增强 Java 编程语言，用于限制超类的使用，密封的类和接口限制其它可能继承或实现它们的其它类或接口。



#### 8、instanceof 自动匹配模式（预览）

**旧写法：**

```java
// 先判断类型
if (obj instanceof String) {
    // 然后转换
    String s = (String) obj;
    // 然后才能使用
}
```

**新写法：**

```java
if (obj instanceof String s) {
    // 如果类型匹配 直接使用
} else {
    // 如果类型不匹配则不能直接使用
}
```

这是第二次预览该功能，我们已经在 Java 14 中首次预览过该特性。



#### 9、Records Class（预览）

Records Class 也是第二次出现的预览功能，它在 JDK 14 中也出现过一次了，使用 Record 可以更方便的创建一个常量类，使用的前后代码对比如下。

**旧写法：**

```
class Point {
    private final int x;
    private final int y;

    Point(int x, int y) { 
        this.x = x;
        this.y = y;
    }

    int x() { return x; }
    int y() { return y; }

    public boolean equals(Object o) { 
        if (!(o instanceof Point)) return false;
        Point other = (Point) o;
        return other.x == x && other.y = y;
    }

    public int hashCode() {
        return Objects.hash(x, y);
    }

    public String toString() { 
        return String.format("Point[x=%d, y=%d]", x, y);
    }
}
```

**新写法：**

```java
record Point(int x, int y) { }
```

也就是说在使用了 record 之后，就可以用一行代码编写出一个常量类，并且这个常量类还包含了构造方法、toString()、equals() 和 hashCode() 等方法。



#### 10、外部存储器访问 API（预览）

目的是引入一个 API，以允许 Java 程序安全有效地访问 Java 堆之外的外部内存。这同样是 Java 14 的一个预览特性。



#### 11、其它功能

其它功能里面还有一些弃用和不建议使用的功能，比如移除了 Nashorn JavaScript 引擎，同时也移除了删除 Solaris 和 SPARC 端口，并标记了一些弃用功能。



### 参考

官方日志：https://openjdk.java.net/projects/jdk/15/


