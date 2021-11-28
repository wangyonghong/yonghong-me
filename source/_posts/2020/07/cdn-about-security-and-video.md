---
title: CDN 的访问控制 & 视频相关
tags:
- CDN
- 视频
categories:
- CDN
date: 2020-07-28 22:24:00
updated: 2020-07-28 22:24:00
---



## 1.Referer

### 又拍云

https://help.upyun.com/knowledge-base/cdn-referer-limite/

### 七牛云

https://developer.qiniu.com/fusion/manual/3839/domain-name-hotlinking-prevention

### 腾讯云

https://cloud.tencent.com/document/product/228/41454

### 阿里云

https://help.aliyun.com/document_detail/27134.html

<!--more-->

### AWS

未找到相关文档

## 2.回源鉴权（自定义接口）

### 又拍云

https://help.upyun.com/knowledge-base/cdn-back-source-auth/

可添加多种鉴权配置

资源地址 鉴权资源地址，如：www.example.com/a/*，仅支持在路径部分使用通配符 *

鉴权服务器地址，格式： http://validate.example.com/app/cdnValidate

请求方法支持 GET POST

鉴权参数 URL 参数 支持最多20个

鉴权成功 失败根据 http 状态码确定

超时默认 通过 或 失败

### 七牛云

https://developer.qiniu.com/fusion/manual/3930/back-to-the-source-authentication

**回源鉴权与时间戳防盗链功能不能同时开启。**

**无法指定某些资源不参与鉴权。**

鉴权服务器地址 格式： https://auth.example.com/cdnauth 或者 http://127.0.0.1:8080/cdnauth

请求方法支持 HEAD GET POST

鉴权参数 URL 参数 支持最多20个

可以添加 不参加鉴权的 Header URL 参数 

鉴权成功 失败根据 http 状态码确定

超时默认 通过 或 失败

### 腾讯云

未找到相关文档

### 阿里云

未找到相关文档

### AWS

未找到相关文档

## 3.URL Token鉴权

### 又拍云 

https://help.upyun.com/knowledge-base/cdn-token-limite/

不支持指定文件类型，但是可以通过边缘规则实现自定义防盗链

https://help.upyun.com/knowledge-base/cdn-edgerules-grammar/

https://help.upyun.com/knowledge-base/cdn-edgerules-cases/

### 七牛云

https://developer.qiniu.com/fusion/manual/3841/timestamp-hotlinking-prevention-fusion

不支持指定文件类型

但是可以找客服。先开通时间戳防盗链功能，然后找客服，让他们去指定 ts 文件不鉴权。该功能目前暂未开放，只能找客服后台开启。

### 腾讯云

https://cloud.tencent.com/document/product/228/41622、

支持指定文件类型

### 阿里云

https://help.aliyun.com/document_detail/85117.html

不支持指定文件类型

可以使用边缘脚本 EdgeScript 定制鉴权

https://help.aliyun.com/document_detail/126565.html

https://help.aliyun.com/document_detail/126571.html

### AWS

支持指定文件类型

[使用签名 URL](https://docs.aws.amazon.com/zh_cn/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html)

[使用固定政策创建签名 URL](https://docs.aws.amazon.com/zh_cn/AmazonCloudFront/latest/DeveloperGuide/private-content-creating-signed-url-canned-policy.html)

[使用自定义政策创建签名 URL](https://docs.aws.amazon.com/zh_cn/AmazonCloudFront/latest/DeveloperGuide/private-content-creating-signed-url-custom-policy.html)

[使用 Java 创建 URL 签名](https://docs.aws.amazon.com/zh_cn/AmazonCloudFront/latest/DeveloperGuide/CFPrivateDistJavaDevelopment.html)

## 4.视频拖拽

### 又拍云

https://help.upyun.com/knowledge-base/cdn-video-drag/

### 七牛云

未找到相关文档

### 腾讯云

https://cloud.tencent.com/document/product/228/8111

### 阿里云

https://help.aliyun.com/document_detail/27130.html

可以实现音视频试看

https://help.aliyun.com/document_detail/140382.html

### AWS 

未找到相关文档



## 5.刷新缓存

### 又拍云

https://help.upyun.com/knowledge-base/refresh/

https://github.com/upyun/java-purge-sdk

### 七牛云

https://developer.qiniu.com/fusion/manual/3845/refresh-the-prefetch-fusion

https://developer.qiniu.com/kodo/sdk/1239/java#9

### 腾讯云

https://cloud.tencent.com/document/product/228/11204

### 阿里云

https://help.aliyun.com/document_detail/27140.html

### AWS

https://docs.aws.amazon.com/zh_cn/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html

## 6.访问日志

### 又拍云

https://help.upyun.com/knowledge-base/cdm-log-download/

### 七牛云

https://developer.qiniu.com/fusion/manual/3847/cdn-log-fusion

### 腾讯云

https://cloud.tencent.com/document/product/228/6316

### 阿里云

https://help.aliyun.com/document_detail/27142.html

###  AWS

https://docs.aws.amazon.com/zh_cn/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html

URL上的参数不在日志中

## 101.总结

### 防盗链

Referer 设置最简单

Token 鉴权  腾讯支持度最好，可以支持指定类型文件鉴权



### 普通HLS加密

当ts文件是开放（不需要鉴权）的情况下，用户可以直接下载ts文件，拼接出完整的视频，但是如果拿不到解密的key，仍然无法播放。

这种方法不能防止直接使用 m3u8 下载的情况

[HLS视频加密 - Hi, I'm Vimiix](https://www.vimiix.com/post/74/)

[知识付费——移动端音视频加密、防盗播实现方案](https://segmentfault.com/a/1190000021126567)

[通过HLS加密防止视频泄露](https://support.huaweicloud.com/bestpractice-vod/vod_10_0004.html)

### 自定义HLS加密

https://blog.csdn.net/z13192905903/article/details/102655575

### 缓存刷新

如果资源位置相同，重转后应刷新CDN

