---
layout: post
title:  "Maven 默认的 Java 版本"
category: "Maven"
tags: ["Maven", "mvn", "java", "version"]
date: 2018-11-08 00:00:00
updated: 2018-11-08 00:00:00
---

在使用 Maven 构建应用程序时，发现报了个错误，大概是非法反射类似的错误。

然后使用 -X 命令查看详细的信息，发现用的是 Java 11 的版本进行编译的，怪不得会发生这种错误。

然后，我查看 Java 版本和 Maven 版本。

<!-- more -->

```
$ java -version
java version "1.8.0_181"
Java(TM) SE Runtime Environment (build 1.8.0_181-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.181-b13, mixed mode)

$ mvn -version            
Apache Maven 3.5.3 (3383c37e1f9e9b3bc3df5050c29c8aff9f295297; 2018-02-25T03:49:05+08:00)
Maven home: /usr/local/Cellar/maven/3.5.3/libexec
Java version: 11, vendor: Oracle Corporation
Java home: /Library/Java/JavaVirtualMachines/jdk-11.jdk/Contents/Home
Default locale: en_US, platform encoding: UTF-8
OS name: "mac os x", version: "10.14.1", arch: "x86_64", family: "mac"
```

所以看来是 maven 的配置出了问题，参考了网上的资料发现只需要在 Maven 的配置文件中指定 JAVA_HOME 就可以了

Maven 可以从两个地方读取配置文件，分别是 `~/.mavenrc` 和 `/etc/mavenrc`

所以我选择在 `~/.mavenrc` 文件中指定 JAVA_HOME

```
JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home
```

再看

```
$ mvn -version            
Apache Maven 3.5.3 (3383c37e1f9e9b3bc3df5050c29c8aff9f295297; 2018-02-25T03:49:05+08:00)
Maven home: /usr/local/Cellar/maven/3.5.3/libexec
Java version: 1.8.0_181, vendor: Oracle Corporation
Java home: /Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "mac os x", version: "10.14.1", arch: "x86_64", family: "mac"
```

成功！
