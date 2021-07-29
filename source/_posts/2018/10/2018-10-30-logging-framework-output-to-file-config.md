---
layout: post
title:  "日志框架的使用——如何输出日志到文件"
category: "SpringBoot"
tags: ["Java", "Logback", "SLF4F", "日志", "SpringBoot"]
date: 2018-10-30 00:00:00
updated: 2018-10-30 00:00:00
---

### Logback 的配置

application.yml 可配置的比较简单

logback-spring.xml 可以进行复杂的配置

<!-- more -->

比如我们有两个需求
- 区分 info 和 error 日志
- 每天产生一个日志文件

这是一个很合理的需求，便于我们查找日志

### 配置 application.yml

```xml
logging:
  pattern:
    console: "%d - %msg%n"
  file: /var/log/tomcat/sell.log
  level:
    com.example : debug
```

这是最简单的配置，分别配置了控制台输出格式，输出到文件的目录，和日志级别

这里日志级别要用包名，或者精确到类名来控制。像上面这样写的话，就是 com.example 这个包里面是 debug 级别的。

### 配置 logback-spring.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<configuration>
    <appender name="consoleLog" class="ch.qos.logback.core.ConsoleAppender">
        <layout class="ch.qos.logback.classic.PatternLayout">
            <pattern>
                %d - %msg%n
            </pattern>
        </layout>
    </appender>
    <root level="info">
        <appender-ref ref="consoleLog" />
    </root>
</configuration>
```

这是配置控制台的输出，接下来我们配置输出到文件

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<configuration>
    <appender name="consoleLog" class="ch.qos.logback.core.ConsoleAppender">
        <layout class="ch.qos.logback.classic.PatternLayout">
            <pattern>
                %d - %msg%n
            </pattern>
        </layout>
    </appender>
    <appender name="fileInfoLog" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>INFO</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
        <encoder>
            <pattern>
                %d - %msg%n
            </pattern>
        </encoder>
        <!-- 滚动策略 -->
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <!-- 路径 -->
            <fileNamePattern>/var/log/tomcat/info.%d.log</fileNamePattern>
        </rollingPolicy>
    </appender>
    <appender name="fileErrorLog" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>ERROR</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
        <encoder>
            <pattern>
                %d - %msg%n
            </pattern>
        </encoder>
        <!-- 滚动策略 -->
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <!-- 路径 -->
            <fileNamePattern>/var/log/tomcat/error.%d.log</fileNamePattern>
        </rollingPolicy>
    </appender>
    <root level="info">
        <appender-ref ref="consoleLog" />
        <appender-ref ref="fileInfoLog" />
        <appender-ref ref="fileErrorLog" />
    </root>
</configuration>
```

这样之后 我们看文件

```shell
/var/log/tomcat   
❯ ls
error.2018-10-30.log info.2018-10-30.log
```

已经出现了文件，并且通过过滤器把 info 和 error 输出到了两个文件 

### 参考文献

- [SpringBoot学习－（十）SpringBoot日志处理](https://blog.csdn.net/qq_28988969/article/details/78085784) 
