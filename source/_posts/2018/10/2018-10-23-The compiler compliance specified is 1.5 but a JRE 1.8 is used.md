---
layout: post
title:  "The compiler compliance specified is 1.5 but a JRE 1.8 is used"
tags: ["eclipse", "compiler", "jre", "jdk"]
date: 2018-10-23 00:00:00
updated: 2018-10-23 00:00:00
---

### 问题：

The compiler compliance specified is 1.5 but a JRE 1.8 is used

<!-- more -->

### 情景再现：

Eclipse 在编译执行程序的时候，可能会出现这样的 warning，如图所示

![](https://up-img.yonghong.tech/pic/2021/07/29-17-20-Screen%20Shot%202018-10-24%20at%2012.18.45%20AM-atS527.png)

### 原因：

Compiler compliance level 的含义说明：设置编译级别，既 Eclipse 中设置 Compiler compliance level为较低版本，只是让编译器相信你的代码是兼容较低版本的，在编译时生成的bytecode(class)兼容较低版本。

这样设置与你写代码时引用的 JDK 是没关系的，也就是说你在写代码时仍可以引用较高版本的 API.（这样就可能导致错误）设置 Compiler compliance level 为较低版本，这样的好处是当别人使用了较低版本的 JDK 时也可以引用你写的编译后的代码。它可以保证编译后的 class 文件的版本一致性。但是，如果你的代码里面(java source)里面调用了较高版本 JDK 的 API.那么即使设置了 Compiler compliance level 为较低版本，在较低版本的 JDK 上运行你的代码也会报错。所以建议在写代码时引用的 JDK，要跟你 Compiler compliance level设置的版本，要求是一致的。

### 解决：

项目上右键 -> Properties -> Java Compiler -> Compiler compliance level

将这一项改为 1.8 (你对应的版本)，保存或者应用就可以了。

![](https://up-img.yonghong.tech/pic/2021/07/29-17-21-Screen%20Shot%202018-10-24%20at%2012.22.48%20AM-a9P4VC.png)

