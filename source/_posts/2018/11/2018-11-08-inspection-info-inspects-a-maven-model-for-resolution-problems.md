---
layout: post
title:  "Inspection info: Inspects a Maven model for resolution problems"
category: "Maven"
tags: ["Maven"]
date: 2018-11-08 00:00:00
updated: 2018-11-08 00:00:00
---

在 spring 多模块的项目中，某个模块依赖了另一个模块，发现 pom 文件爆红了，显示的错误是

<!-- more -->

> <div style="color: red;">Inspection info: Inspects a Maven model for resolution problems.<div>

处理办法很简单：

只需要在 pom.xml 上右键 -> Maven -> Reimport 即可，爆红消失了

这样会让 Maven 强制重新加载依赖包，所以会解决问题。