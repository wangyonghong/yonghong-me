---
layout: post
title:  "在 Ubuntu 上使用 Android Studio 开发"
category: "Android"
tags: ["Android", "镜像", "maven", "AS", "as"]
date: 2019-03-18 00:00:00
updated: 2018-03-18 00:00:00
---

## 下载 Android Studio 

https://developer.android.com

https://developer.android.google.cn

<!-- more -->

这两个网址都要 FQ 下载，区别是上面的网址不 FQ 打都打不开。

下载我建议是用迅雷下载，Ubuntu 上还是可以安装迅雷的。详情看这里 https://github.com/Jactor-Sue/Deepin-Apps-Installation

## 安装 Android Studio 

安装比较简单，直接解压就可以。我把解压好的文件放在了 `/opt/android-studio` 这个目录中了。

启动可以直接命令行启动 

```shell
nohup /opt/android-studio/bin/studio.sh &
```

或者在 `/usr/share/applications` 目录中创建一个快捷方式

```shell
sudo vim /usr/share/applications/Studio.desktop
```

在 `Studio.desktop` 写入下面内容

```
[Desktop Entry] 
Name=AndroidStudio 
Type=Application 
Icon=/opt/android-studio/bin/studio.png 
Exec=sh /opt/android-studio/bin/studio.sh
```

给 `Studio.desktop` 加上可执行权限

```shell
sudo chmod +x /usr/share/applications/Studio.desktop
```

> 注意：上面文件内容里 Android Studio 的目录是你自己设置的目录，并且文件中不要包含多余空格。

## SDK 镜像加速

SDK 下载很慢一直是一个很头疼的问题。

可以在设置中 `Appearance & Behavior -> System Settings -> HTTP Proxy` 中进行设置，勾选 `Auto-detect proxy settings`，勾选 `Automatic proxy configuration URL`，填写 `mirrors.neusoft.edu.cn`

保存设置就可以了。

目前来看，这个设置好之后确实会很快，但是有时候也会抽风，不行就重启试试，再不行就等会再试。

> 更新：还是直接下载吧，网络不好就等一等，换了代理之后也好像也没有什么用。

## /dev/kvm permission denied on Ubuntu 18.04

下载完 SDK 后新建模拟器可能会出现这样的报错。这是因为当前的用户没有权限写 `/dev/kvm` 文件。执行下面命令即可

```shell
sudo chown your_name /dev/kvm
```

## 加速 gradle-4.10.3-all.zip

这个文件是最头疼的了，好像还没有一个镜像站内快速的下载这个文件，一个不太友好的解决办法是去官网上下载好到本地，然后直接在 `gradle-warper.properties` 引用本地文件

https://services.gradle.org/distributions/

或者我的[百度云分享](https://pan.baidu.com/s/1zLxEQ35YaPIGfZKiluua5A) 提取码: bicm 

## 加速 gradle 依赖

原来的文件是这样的

```
// Top-level build file where you can add configuration options common to all sub-projects/modules.

buildscript {
    repositories {
        google()
        jcenter()
        
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:3.3.2'
        
        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
    }
}

allprojects {
    repositories {
        google()
        jcenter()
    }
}

task clean(type: Delete) {
    delete rootProject.buildDir
}

```

现在改成这样

```
// Top-level build file where you can add configuration options common to all sub-projects/modules.

buildscript {
    repositories {
        maven { url 'https://maven.aliyun.com/repository/public' }
        maven { url 'https://maven.aliyun.com/repository/google' }
        
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:3.3.2'
        
        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
    }
}

allprojects {
    repositories {
        maven { url 'https://maven.aliyun.com/repository/public' }
        maven { url 'https://maven.aliyun.com/repository/google' }
    }
}

task clean(type: Delete) {
    delete rootProject.buildDir
}
```

https://maven.aliyun.com/repository/public

包括 https://maven.aliyun.com/repository/central 和 https://maven.aliyun.com/repository/jcenter

所以这里需要用 public 和 google 两个仓库代替 google() 和 jcenter() 

如果需要其他的也可以继续添加，下面包括安卓或者后端需要用到的仓库

```
maven { url 'https://maven.aliyun.com/repository/apache-snapshots' }
maven { url 'https://maven.aliyun.com/repository/apache-central' }
maven { url 'https://maven.aliyun.com/repository/gradle-plugin' }
maven { url 'https://maven.aliyun.com/repository/jcenter' }
maven { url 'https://maven.aliyun.com/repository/spring' }
maven { url 'https://maven.aliyun.com/repository/spring-plugin' }
maven { url 'https://maven.aliyun.com/repository/releases' }
maven { url 'https://maven.aliyun.com/repository/snapshots' }
maven { url 'https://maven.aliyun.com/repository/grails-core' }
maven { url 'https://maven.aliyun.com/repository/mapr-public' }
```

https://maven.aliyun.com/repository/public 是推荐的新的地址，http://maven.aliyun.com/nexus/content/groups/public 是老的地址，为了兼容仍然可以使用。

> 这里有个问题是，如果 SDK 没有装全，可能会导致 Gradle 依赖无法下载。笔者在试验的时候，发现没有安装 28.0.3 版本的 platform-tools 导致无法下载 com.android.tools.build:gradle:3.3.2

