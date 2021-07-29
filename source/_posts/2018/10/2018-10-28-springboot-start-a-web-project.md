---
layout: post
title:  "使用 IDEA 创建一个简单的 Java Web 项目"
category: "SpringBoot"
tags: ["Java", "SpringBoot", "Web"]
date: 2018-10-28 00:00:00
updated: 2018-10-28 00:00:00
---

Just follow me!

打开 IDEA -> Create New Project -> Spring Initializr

<!-- more -->

Choose Initializr Service Url 选择默认即可

![](https://up-img.yonghong.tech/pic/2021/07/29-17-35-Screen%20Shot%202018-10-28%20at%204.23.26%20PM-Tz21SX.png)

填写 Group 和 Artifact，这一页中的内容是 Maven 项目的参数，关于这个可以参考 [知乎 -- Maven中的参数分别是什么意思？](https://www.zhihu.com/question/24494667)

![](https://up-img.yonghong.tech/pic/2021/07/29-17-35-Screen%20Shot%202018-10-28%20at%204.23.40%20PM-KKi31n.png)

接下来我们看到了很多 Web 的组件，我们只勾选一个 Web 里的 Web 选项。

![](https://up-img.yonghong.tech/pic/2021/07/29-17-35-Screen%20Shot%202018-10-28%20at%204.23.48%20PM-yCFawm.png)

接下来选择项目文件的存储位置，选完之后就可以进入项目了。

![](https://up-img.yonghong.tech/pic/2021/07/29-17-35-Screen%20Shot%202018-10-28%20at%204.24.14%20PM-qshVZC.png)

进入项目之后可能需要等一段时间，让 IDEA 帮我们下载好所需的文件。

接下来我们看一下项目的目录结构：
- .idea 文件夹内是 IDEA 自动生成的关于 IDEA 的一些配置，我们不需要管
- .mvn 文件夹是 Maven 帮我们生成的文件
- src 目录是我们主要关注的目录，和一般的 Java 项目一样，都有包和 .java 文件，main 目录是主要的程序目录，test 是用来写测试用例的。resources 目录存放一些静态的资源文件。
- .gitignore 文件是 git 生成的用来忽略指定文件变化的
- mvnw 和 mvnw.cmd 分别是 Linux/macOS 和 Windows 的 Maven 脚本
- pom.xml 是 Maven 项目的配置文件，我们如果需要什么组件都可以在这里进行配置。

![](https://up-img.yonghong.tech/pic/2021/07/29-17-35-Screen%20Shot%202018-10-28%20at%204.38.16%20PM-vutqfV.png)

看过配置之后我们来运行一下这个简单的 Java Web 项目

项目的入口文件是 main 目录下的 java 目录下的 com.example.demo 包的 DemoApplication.java 的 main() 方法。右键 Run 'DemoApplication'

可以看到控制台中出现了很多日志。如果我们看到下面的这句，说明我们运行成功了，那么怎么查看呢，在浏览器中
输入 [http://localhost:8080/](http://localhost:8080/)

Tomcat started on port(s): 8080 (http) with context path ''

如果项目正常的话，应该会出现下图所示页面

![](https://up-img.yonghong.tech/pic/2021/07/29-17-36-Screen%20Shot%202018-10-28%20at%2011.51.06%20PM-Wr7ArW.png)

That's all.
