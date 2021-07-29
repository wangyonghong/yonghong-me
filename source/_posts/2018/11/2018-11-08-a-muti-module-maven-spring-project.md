---
layout: post
title:  "记一次给 Maven 多个 module 的 SpringBoot 项目添加子模块的过程"
category: "Maven"
tags: ["Maven", "Spring", "SpringBoot", "pom.xml", "pom"]
date: 2018-11-08 00:00:00
updated: 2018-11-08 00:00:00
---

最近接手一个项目，项目是一个 Maven 多个 module 的 SpringBoot 项目，要求添加一个功能，也就是在不影响原有项目的情况下添加一个模块。于是我开始了这个艰难的旅程。

<!-- more -->

首先选中项目目录，右键 -> New -> Module -> Spring Initializr

这部分很普通的建立一个 SpringBoot 项目，不再赘述

接下来就是重点内容了，因为我们建的是一个子模块，所以，我们可以把目录下的 java 文件都删除，.mvn目录也删掉。保留 pom.xml 文件。接下来我们对 pom.xml 文件进行修改

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>demo</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <groupId>com.example.demo</groupId>
    <artifactId>child</artifactId>
    <version>1.0-SNAPSHOT</version>

    <name>child</name>
    <description>子模块</description>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        
    </build>
</project>

```

注意，我们把 parent 标签中的内容改为了我们的父工程的坐标

```xml
<parent>
    <groupId>com.example</groupId>
    <artifactId>demo</artifactId>
    <version>1.0-SNAPSHOT</version>
</parent>
```

并且把 build 标签里的 Maven 插件删除了。

接下来设置父模块的 pom.xml

```xml
<modules>
    <module>auth</module> <!-- 以前的子模块 -->
    <module>utils</module> <!-- 以前的子模块 -->
    <module>child</module> <!-- 新的的子模块 -->
</modules>
```


我们在 com.example.child 这个包里建一个 controller 包，在 controller 包中建一个 TestController.java 文件

```java
package com.example.child.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import lombok.extern.slf4j.Slf4j;

@RestController
@RequestMapping(value = "/hello")
@Slf4j
public class TestController{

    @GetMapping(value = "/test")
    public String test() {

        log.info("######################################测试测试");
        return "Hello Test Result";
    }
}

```

然后我们运行程序。

一般情况下这样配置是没有问题的。

但是很可能会出问题，比如说，导包没导进去，那么只需要在 pom.xml 文件上右键 -> Maven -> Reimport 即可。

👌，继续，如果上面的操作我们都执行了，那么我们去访问 http://localhost:8080/hello/test 或者说可能是别的前缀的地址，反正要访问 /hello/test 这个 API，浏览器应该会返回 Hello Test Result。

but，我这里报了错，是 404，what ？没有找到？

再看控制台，也没有 log。

这是为什么呢，都按照网上的参考做了啊。

> <div style="color: red;">后来我开始阅读以前的代码，发现同一个包名字下，不同的 module，竟然还有一个 TestController.java 。为什么没有报错呢？</div>


我就没再关心这个问题，继续找别的问题，我为什么要避开这个错误呢 ！！！

大概找了几个小时问题，后来才回到这个地方，我改了个名字就好了

