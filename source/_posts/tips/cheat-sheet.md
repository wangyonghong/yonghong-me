---
title: 速查
tags:
- 速查
- 技巧
categories:
- 技巧
date: 2021-11-24 22:24:00
updated: 2021-11-24 22:24:00
---


## 命令速查

### adb

- 安装
    ```bash
    adb -s device-name install demo.apk
    ```
- 获取手机属性
    ```bash
    adb -s device-name shell getprop
    ```
- 获取手机model
    ```bash
    adb -s device-name shell getprop | grep product
    ```
- 设置代理
    ```bash
    adb shell settings put global http_proxy ip:port
    adb shell settings put global https_proxy ip:port
    ```
- 清除代理
    ```bash
    adb shell settings put global http_proxy :0
    adb shell settings put global https_proxy :0
    ```

<!-- more -->

### ffmpeg 

- 转码
    ```bash
    ffmpeg -i input.mp4 -profile:v baseline -level 3.0 output.mp4
    ```
- 视频按帧转图片
    ```bash
    ffmpeg -i input.mp4 -f image2 test/%05d.jpeg
    ```

### ffprobe

- 查看视频格式
    ```bash
    ffprobe input.mp4 -show_streams -show_format -v quiet
    ```

### gradle

- 生成 gradlew
    ```bash
    gradle wrapper
    ```
- gradlew 修改版本
    ```bash
    ./gradlew wrapper --gradle-version 7.2
    ```
- gradlew 执行
    ```bash
    ./gradlew :ModuleName:taskName
    ```

### git

- git 浅克隆
    ```bash
    git clone -b branchName remote-url --single-branch
    ```
- git clone 只clone一个分支，并且还能checkout远端分支
    ```bash
    git clone --filter=blob:none --no-checkout
    ```
- git 彻底删除 .gitignore 中文件
    ```bash
    git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch file.txt' --prune-empty --tag-name-filter cat -- --all
    git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch file_dir' --prune-empty --tag-name-filter cat -- --all
    ```

## Android 版本号

| 名称                 | 版本号       | 发行日期       | API等级  |  安全性更新状态 |
| ------------------- | ----------- | ------------- | ------- | ------------- |
| Android Jelly Bean  | 4.1 – 4.3.1 | 2012年7月9日   | 16 – 18 | 不支持         |
| Android KitKat      | 4.4 – 4.4.4 | 2013年10月31日 | 19 – 20 | 不支持         |
| Android Lollipop    | 5.0 – 5.1.1 | 2014年11月12日 | 21 – 22 | 不支持         |
| Android Marshmallow | 6.0 – 6.0.1 | 2015年10月5日  | 23      | 不支持         |
| Android Nougat      | 7.0 – 7.1.2 | 2016年8月22日  | 24 – 25 | 不支持         |
| Android Oreo        | 8.0 – 8.1   | 2017年8月21日  | 26 – 27 | 支持           |
| Android Pie         | 9           | 2018年8月6日   | 28      | 支持           |
| Android 10          | 10          | 2019年9月3日   | 29      | 支持           |
| Android 11          | 11          | 2020年9月8日   | 30      | 支持           |
| Android 12          | 12          | 2021年10月4日  | 31      | 支持           |


