---
layout: post
title:  "日志框架的使用——如何选择日志框架"
category: "SpringBoot"
tags: ["Java", "JUL", "JCL", "Log4j", "Log4j2", "Logback", "SLF4F", "日志", "SpringBoot"]
date: 2018-10-29 00:00:00
updated: 2018-10-29 00:00:00
---

### 什么是日志框架

> 日志框架：是一套能实现日志输出的工具包

> 日志：能够描述系统运行状态的所有事件都可以算作日志

<!-- more -->

### 日志框架的能力

- 定制输出目标（比如输出到文件，输出到数据库，或者是网络第三方服务）
- 定制输出格式
- 携带上下文信息（输出的时间戳等，路径，线程，堆栈）
- 运行时选择性输出（比如只选择某一方面的日志）
- 灵活的配置
- 优异的性能

### 日志框架的选择

常用的日志框架有 JUL、JCL、Log4j、Log4j2、Logback、SLF4j、jboss-logging等，这么多日志框架我们选择哪一个好呢？

听我一一道来：

一个优秀的日志方案一定是一个日志门面和一个日志实现组成，也就是说面向接口编程。

- 日志门面包含 JCL、SLF4j、jboss-logging
- 日志实现包含 Log4j、Log4j2、Logback、JUL

#### Java Util Log

简称 JUL，是 JDK 中自带的 log 功能。虽然是官方自带的 log lib，JUL 的使用确不广泛。主要原因:

JUL 从 JDK 1.4 才开始加入(2002年)，当时各种第三方 log lib 已经被广泛使用了
JUL 早期存在性能问题，到 JDK1.5 上才有了不错的进步，但现在和 Logback/Log4j2 相比还是有所不如
JUL 的功能不如 Logback/Log4j2 等完善，比如 Output Handler 就没有 Logback/Log4j2 的丰富，有时候需要自己来继承定制，又比如默认没有从 ClassPath 里加载配置文件的功能。

#### Log4j

Log4j 是在 Logback 出现之前被广泛使用的 Log Lib, 由 Gülcü 于2001年发布，后来成为 Apache 基金会的顶级项目。Log4j 在设计上非常优秀，对后续的 Java Log 框架有长久而深远的影响，也产生了 Log4c, Log4s, Log4perl 等到其他语言的移植。Log4j 的短板在于性能，在 Logback 和 Log4j2 出来之后，Log4j 的使用也减少了。

#### Java Commons Logging

简称 JCL，是 Apache 下面的项目。JCL 是一个 Log Facade，只提供 Log API，不提供实现，然后有 Adapter 来使用 Log4j 或者 JUL 作为 Log Implementation。

就像之前所说，JDK 现在带了自己的JUL，然后又有第三方的 Log4j 等日志库存在，不同的项目可能各自使用了不同的日志库。如果你的项目依赖的其他 lib 各自使用了不同的日志库，你想控制日志行为，就需要针对每个日志库都写一个配置文件，是不是很酸爽?

然后这个时候 JCL 就出现了。在程序中日志创建和记录都是用 JCL 中的接口，在真正运行时，会看当前 ClassPath 中有什么实现，如果有 Log4j 就是用 Log4j, 如果啥都没有就是用 JDK 的 JUL。

这样，在你的项目中，还有第三方的项目中，大家记录日志都使用 JCL 的接口，然后最终运行程序时，可以按照自己的需求(或者喜好)来选择使用合适的 Log Implementation。如果用 Log4j, 就添加 Log4j 的 jar 包进去，然后写一个 Log4j 的配置文件；如果喜欢用 JUL，就只需要写个 JUL 的配置文件。如果有其他的新的日志库出现，也只需要它提供一个 Adapter，运行的时候把这个日志库的 jar 包加进去。

到这个时候一切看起来都很简单，很美好。接口和实现做了良好的分离，在统一的JCL之下，不改变任何代码，就可以通过配置就换用功能更强大，或者性能更好的日志库实现。

> 这种简单美好一直持续到 SLF4J 出现。

#### SLF4J/Logback

SLF4J(The Simple Logging Facade for Java) 和 Logback 也是 Gülcü 创立的项目，其创立主要是为了提供更高性能的实现。其中，SLF4j 是类似于 JCL 的 Log Facade，Logback 是类似于 Log4j 的 Log Implementation。

之前已经说过，Apache 有了个 JCL，用来做各种 Log lib 统一的接口，如果 Gülcü 要搞一个更好的 Log 实现的话，直接写一个实现就好了，为啥还要搞一个和 SLF4J 呢?

原因是 Gülcü 认为 JCL 的 API 设计得不好，容易让使用者写出性能有问题的代码。

比如在用 JCL 输出一个 debug 级别的 log:

```java
logger.debug("start process request, url:" + url);
```

这个有什么问题呢？一般生产环境 log 级别都会设到 info 或者以上，那这条 log 是不会被输出的。然而不管会不会输出，这其中都会做一个字符串连接操作，然后生产一个新的字符串。如果这条语句在循环或者被调用很多次的函数中，就会多做很多无用的字符串连接，影响性能。

所以 JCL 的最佳实践推荐这么写：

```java
if (logger.isDebugEnabled()) {
    logger.debug("start process request, url:" + url);
}
```

然而开发者常常忽略这个问题或是觉得麻烦而不愿意这么写。所以 SLF4J 提供了新的 API，方便开发者使用:

```java
logger.debug("start process request, url:{}", url);
```

这样的话，在不输出 log 的时候避免了字符串拼接的开销；在输出的时候需要做一个字符串 format，代价比手工拼接字符串大一些，但是可以接受。

而 Logback 则是作为 Log4j 的继承者来开发的，提供了性能更好的实现，异步 logger，Filter 等更多的特性。

现在事情变复杂了。我们有了两个流行的 Log Facade，以及三个流行的 Log Implementation。Gülcü 是个追求完美的人，他决定让这些Log之间都能够方便的互相替换，所以做了各种 Adapter 和 Bridge 来连接:

![](https://up-img.yonghong.tech/pic/2021/07/29-17-36-v2-4a3df07374fe31dbd6fbff88021630ed-FSIZGs.jpg)

可以看到甚至 Log4j 和 JUL 都可以桥接到SLF4J，再通过 SLF4J 适配到到 Logback!

在这里需要注意不能搞出循环的桥接，比如下面这些依赖就不能同时存在:

1. jcl-over-slf4j 和 slf4j-jcl
2. log4j-over-slf4j 和 slf4j-log4j12
3. jul-to-slf4j 和 slf4j-jdk14

总感觉事情在变得更麻烦呢！

#### Log4j2

现在有了更好的 SLF4J 和 Logback——你会想事情到这里总该了解了吧，让他们慢慢取代JCL 和 Log4j 好了。

然而维护 Log4j 的人不这样想，他们不想坐视用户一点点被 SLF4J/Logback 蚕食，继而搞出了 Log4j2。

Log4j2 和 Log4j1.x 并不兼容，设计上很大程度上模仿了 SLF4J/Logback，性能上也获得了很大的提升。

Log4j2 也做了 Facade/Implementation 分离的设计，分成了 log4j-api 和 log4j-core。

现在好了，我们有了三个流行的Log 接口和四个流行的Log实现，如果画出桥接关系的图来回事什么样子呢?

![](https://up-img.yonghong.tech/pic/2021/07/29-17-37-v2-57092397ff9d7a69d359856ef19e769d-uMe6Ag.jpg) 

是不是感觉有点晕呢？同样，在添加依赖的时候，要小心不要搞成循环依赖。

### 实践

上次我们用 IDEA 创建了一个简单的 Java Web Application，我们在这个基础上继续写，由于 SpringBoot 使用的就是 SLF4J 和 Logback，那我们也就使用这一组合。我们在 test 的 com.example.demo.service 这个包里新建一个 LoggerTest 类

```java
package com.example.demo.service;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

/**
 * 一个简单的 LogTest 
 *
 * @author 0xl2oot@gmail.com
 * @date 2018/10/30 10:31 AM
 */
@RunWith(SpringRunner.class)
@SpringBootTest
public class LoggerTest {

    private final Logger logger = LoggerFactory.getLogger(LoggerTest.class);

    @Test
    public void test1() {
        logger.debug("debug...");
        logger.info("info...");
        logger.error("error...");
    }
}
```

运行这个程序，发现控制台会输出 

```
2018-10-30 10:35:51.254  INFO 66590 --- [           main] com.example.demo.service.LoggerTest      : info...
2018-10-30 10:35:51.254 ERROR 66590 --- [           main] com.example.demo.service.LoggerTest      : error...
```

为什么没有 debug 呢，因为系统默认是 info 之上的级别，所以 debug 是不显示的

那有几种 Level 级别呢？ macOS 可以通过 Command + O 来搜索 Level (Slf4j) 


```java
public enum Level {
    ERROR(40, "ERROR"),
    WARN(30, "WARN"),
    INFO(20, "INFO"),
    DEBUG(10, "DEBUG"),
    TRACE(0, "TRACE");

    private int levelInt;
    private String levelStr;

    private Level(int i, String s) {
        this.levelInt = i;
        this.levelStr = s;
    }
}
```

可以看到一共有 5 种级别。

### 使用 Lombok 简化操作

在 pom.xml 中添加 依赖

```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
</dependency>
```

这样的话，我们就可以这样使用

```java
package com.example.demo.service;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import lombok.extern.slf4j.Slf4j;

@RunWith(SpringRunner.class)
@SpringBootTest
@Slf4j
public class LoggerTest {
    @Test
    public void test1() {
        log.debug("debug...");
        log.info("info...");
        log.error("error...");
    }
}
```


### 日志框架的最佳实践

#### 1. 总是使用Log Facade，而不是具体Log Implementation

正如之前所说的，使用 Log Facade 可以方便的切换具体的日志实现。而且，如果依赖多个项目，使用了不同的Log Facade，还可以方便的通过 Adapter 转接到同一个实现上。如果依赖项目使用了多个不同的日志实现，就麻烦的多了。

具体来说，现在推荐使用 Log4j-API 或者 SLF4j，不推荐继续使用 JCL。

#### 2. 只添加一个 Log Implementation依赖

毫无疑问，项目中应该只使用一个具体的 Log Implementation，建议使用 Logback 或者 Log4j2。如果有依赖的项目中，使用的 Log Facade 不支持直接使用当前的 Log Implementation，就添加合适的桥接器依赖。具体的桥接关系可以看上面的图。

#### 3. 具体的日志实现依赖应该设置为 optional 和使用 runtime scope

在项目中，Log Implementation 的依赖强烈建议设置为 runtime scope，并且设置为 optional。例如项目中使用了 SLF4J 作为 Log Facade，然后想使用 Log4j2 作为 Implementation，那么使用 maven 添加依赖的时候这样设置:

```xml
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-core</artifactId>
    <version>${log4j.version}</version>
    <scope>runtime</scope>
    <optional>true</optional>
</dependency>
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-slf4j-impl</artifactId>
    <version>${log4j.version}</version>
    <scope>runtime</scope>
    <optional>true</optional>
</dependency>
```

设为 optional，依赖不会传递，这样如果你是个 lib 项目，然后别的项目使用了你这个 lib，不会被引入不想要的 Log Implementation 依赖；

Scope 设置为 runtime，是为了防止开发人员在项目中直接使用 Log Implementation 中的类，而不适用 Log Facade 中的类。

#### 4. 如果有必要, 排除依赖的第三方库中的 Log Impementation 依赖

这是很常见的一个问题，第三方库的开发者未必会把具体的日志实现或者桥接器的依赖设置为 optional，然后你的项目继承了这些依赖——具体的日志实现未必是你想使用的，比如他依赖了 Log4j，你想使用 Logback，这时就很尴尬。另外，如果不同的第三方依赖使用了不同的桥接器和 Log 实现，也极容易形成环。

这种情况下，推荐的处理方法，是使用exclude来排除所有的这些Log实现和桥接器的依赖，只保留第三方库里面对 Log Facade 的依赖。

比如阿里的 JStorm 就没有很好的处理这个问题，依赖 jstorm 会引入对 Logback 和 log4j-over-slf4j 的依赖，如果你想在自己的项目中使用 Log4j 或其他 Log 实现的话，就需要加上 excludes:

```
<dependency>
    <groupId>com.alibaba.jstorm</groupId>
    <artifactId>jstorm-core</artifactId>
    <version>2.1.1</version>
    <exclusions>
        <exclusion>
            <groupId>org.slf4j</groupId>
            <artifactId>log4j-over-slf4j</artifactId>
        </exclusion>
        <exclusion>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-classic</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

#### 5. 避免为不会输出的log付出代价

Log 库都可以灵活的设置输出界别，所以每一条程序中的 log，都是有可能不会被输出的。这时候要注意不要额外的付出代价。

先看两个有问题的写法：

```java
logger.debug("start process request, url: " + url);
logger.debug("receive request: {}", toJson(request));
```

第一条是直接做了字符串拼接，所以即使日志级别高于debug也会做一个字符串连接操作；第二条虽然用了 SLF4J/Log4j2 中的懒求值方式来避免不必要的字符串拼接开销，但是 toJson() 这个函数却是都会被调用并且开销更大。

推荐的写法如下:

```java
logger.debug("start process request, url:{}", url); // SLF4J/LOG4J2
logger.debug("receive request: {}", () -> toJson(request)); // LOG4J2
logger.debug(() -> "receive request: " + toJson(request)); // LOG4J2
if (logger.isDebugEnabled()) { // SLF4J/LOG4J2
    logger.debug("receive request: " + toJson(request)); 
}
```

#### 6. 日志格式中最好不要使用行号，函数名等字段

原因是，为了获取语句所在的函数名，或者行号，log 库的实现都是获取当前的 stacktrace，然后分析取出这些信息，而获取 stacktrace 的代价是很昂贵的。如果有很多的日志输出，就会占用大量的 CPU。在没有特殊需要的情况下，建议不要在日志中输出这些这些字段。

最后，log 中不要输出稀奇古怪的字符！

部分开发人员为了方便看到自己的 log，会在 log 语句中加上醒目的前缀，比如:

```java
logger.debug("========================start process request=============");
```

虽然对于自己来说是方便了，但是如果所有人都这样来做的话，那 log 输出就没法看了！正确的做法是使用 grep 来看只自己关心的日志。


### 阅读延伸

- [轻松理解面向接口编程！](https://zhuanlan.zhihu.com/p/30572621)
- [GitHub - Ceki Gulcu](https://github.com/ceki)
- [GitHub - QOS.CH Sarl](https://github.com/qos-ch)


### 参考文献

- [知乎 - Java 日志框架解析(上) - 历史演进](https://zhuanlan.zhihu.com/p/24272450)
- [知乎 - Java 日志框架解析(下) - 最佳实践](https://zhuanlan.zhihu.com/p/24275518)
- [slf4j、jcl、jul、log4j1、log4j2、logback大总结](https://my.oschina.net/pingpangkuangmo/blog/410224)
