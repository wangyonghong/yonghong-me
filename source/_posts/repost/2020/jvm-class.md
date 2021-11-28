---
title: class文件结构与格式——思维导图
tags:
- class
- JVM
categories:
- 转载
date: 2020-07-12 22:24:00
updated: 2020-07-12 22:24:00
---

## 前言

class文件作为操作系统无关的格式文件，是JVM直接识别的字节码文件。它可由java、scala、groovy等语言编译而来，校验后可在JVM中执行。下面我们一起看看class文件的结构与格式规范。

### 1. class文件基本概念

![class文件基本概念](https://up-img.yonghong.tech/pic/2020/07/12-21-24-watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTAwODYxMjI=,size_16,color_FFFFFF,t_70-g7ARYc.jpeg)
<!--more-->

### 2. class文件的结构

![class文件的结构](https://up-img.yonghong.tech/pic/2020/07/12-21-24-watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTAwODYxMjI=,size_16,color_FFFFFF,t_70-20200712212433688-RIThe9.jpeg)

##### PS：符号引用的概念

![符号引用的概念](https://up-img.yonghong.tech/pic/2020/07/12-21-24-watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTAwODYxMjI=,size_16,color_FFFFFF,t_70-20200712212433934-Iy6K1B.jpeg)

### 3. 字节码指令

![字节码指令](https://up-img.yonghong.tech/pic/2020/07/12-21-24-watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTAwODYxMjI=,size_16,color_FFFFFF,t_70-20200712212434852-20vwxN.jpeg)