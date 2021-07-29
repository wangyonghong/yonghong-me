---
layout: post
title:  "IntelliJ IDEA SpringBoot 项目读取系统环境变量"
category: "macOS"
tags: ["macOS", SpringBoot]
date: 2018-11-07 00:00:00
updated: 2018-11-07 00:00:00
---

### 情景再现

现在很多项目为了在本地和线上部署方便，都采用了从系统环境变量读取 MySQL 等配置信息的

<!-- more -->

就像这样👇

```
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://${MYSQL_HOST}:${MYSQL_PORT}/test?useSSL=false&characterEncoding=utf8&autoReconnect=true
spring.datasource.username=${MYSQL_USER}
spring.datasource.password=${MYSQL_PASSWORD}
```

设置了环境变量，在命令行中也能 echo

但是就是 IntelliJ IDEA 读不到

### 解决办法

方法1：通过bash命令 open /Applications/xxx.app启动 IDEA。

方法2：不在环境变量中设置，在 IDEA 中设置 Application 的启动环境

在运行的按钮处，选择 Edit Configurations

![29-17-45-ScreenShot2018-11-08at3.36.13PM-s2Vn0p](https://up-img.yonghong.tech/pic/2021/07/29-17-45-Screen%20Shot%202018-11-08%20at%203.36.13%20PM-s2Vn0p.png)


接下来我们展开 Environment 选项，发现有个 Environment variables.我们点开进行修改

![29-17-45-ScreenShot2018-11-08at3.38.21PM-oe9Wt9](https://up-img.yonghong.tech/pic/2021/07/29-17-45-Screen%20Shot%202018-11-08%20at%203.38.21%20PM-oe9Wt9.png)


改成下面的样子就可以了

![29-17-45-ScreenShot2018-11-08at3.39.52PM-TYqDjJ](https://up-img.yonghong.tech/pic/2021/07/29-17-45-Screen%20Shot%202018-11-08%20at%203.39.52%20PM-TYqDjJ.png)


运行 -> 成功 ！！！ 

### 参考

-[mac上ide中无法获取环境变量的问题](https://blog.csdn.net/kobe1110/article/details/50524220)
-[IntelliJ Idea中设置和使用环境变量？](https://cloud.tencent.com/developer/ask/32339)