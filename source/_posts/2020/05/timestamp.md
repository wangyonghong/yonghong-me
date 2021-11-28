---
title: Linux/macOS 如何进行时间戳转换？
tags:
- timestamp
categories:
- 技巧
date: 2020-05-20 22:24:00
updated: 2020-05-20 22:24:00
---

## 时间戳转换网站

[https://tool.lu/timestamp/](https://tool.lu/timestamp/)

<!--more-->
![https://tool.lu/timestamp/](https://up-img.yonghong.tech/pic/2020/05/截屏2020-05-12%20下午2.08.09.png)

[https://tool.chinaz.com/tools/unixtime.aspx](https://tool.chinaz.com/tools/unixtime.aspx)
![https://tool.chinaz.com/tools/unixtime.aspx](https://up-img.yonghong.tech/pic/2020/05/截屏2020-05-12%20下午2.09.15.png)

## Linux 时间戳转日期时间
```shell
# date -d @timestamp
# date -d@timestamp
date -d @1574933006
date -d@1574933006
```


## macOS 时间戳转日期时间
```shell
# date -r timestamp
# date -rtimestamp
date -r 1574933006
date -r1574933006
```


## 日期时间转时间戳

目前没有特别好用的方法，还是去网站上转吧

## Linux 获取当前时间戳


```shell
date +%s
```


## macOS 获取当前时间戳


```shell
date +%s
```
