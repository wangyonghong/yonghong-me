---
title: IDEA 技巧
tags:
- IDEA
- 技巧
categories:
- 技巧
date: 2021-08-02 22:24:00
updated: 2021-08-02 22:24:00
---

## properties 文件 Unicode 转中文

- Preference -> Editor -> File Encodings -> Properties Files (*.properties) 
- 勾选上 Transparent native-to-ascii conversion

## 调整 import 多个类时不变成 import *

- Preference -> Editor -> Code Style -> Java -> Imports 
- Class count to use import with "*"
- Names count to use static import with "*"
- 这两个数值调大到 999

<!-- more -->

## 关闭XML中SQL的黄色背景

- Preference -> Editor -> Inspections -> SQL 
- 取消勾选 No data sources configured 和 SQL dialect detection

![pic](https://up-img.yonghong.tech/pic/2021/08/03-15-20-xhH8ST-vf3mKv.jpg)

## 格式化代码

- 格式化整个文件，⌘ + ⌥ + L
- 格式化选中区域，选中指定区域后，⌘ + ⌥ + L

## 补全方法调用的返回值

光标放在调用的方法名上，⌘ + ⌥ + V 

