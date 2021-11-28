---
title: Nginx 配置 TLSv1.3
tags:
- Nginx
- TLS
categories:
- Nginx
date: 2020-07-29 22:24:00
updated: 2020-07-29 22:24:00
---

## 1.Nginx 版本

目前 Nginx 1.18 是默认支持的，低版本没有测试过。

## 2.虚拟主机配置

<!--more-->

以 source.yonghong.me 为例

```
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;

    server_name source.yonghong.me;

		# 抛弃老的协议，只保留 TLSv1.1 TLSv1.2 TLSv1.3
    ssl_protocols TLSv1.1 TLSv1.2 TLSv1.3;
    
    # 需要配置符合PFS规范的加密套件，推荐配置
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4:!DH:!DHE;
    # 配置 ssl_ciphers 后需要开启 ssl_prefer_server_ciphers
    ssl_prefer_server_ciphers on;

		# 证书
    ssl_certificate /etc/cert/live/yonghong.me/fullchain.pem;
    ssl_certificate_key /etc/cert/live/yonghong.me/privkey.pem;
    ssl_trusted_certificate  /etc/cert/live/yonghong.me/chain.pem;

		# HSTS（HTTP严格传输安全）的 max-age 需要大于15768000秒（半年）。
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

    location / {
        proxy_pass http://sourcegraph:7080;
    }
}

server {
    listen 80;
    listen [::]:80;

    server_name source.yonghong.me;

    location / {
        return 301 https://source.yonghong.me$request_uri;
    }
}
```

## 3.注意注意注意

#### 如果开启了TLSv1.3，那么所有的虚拟主机都需要开启，否则开启会失败！！！

#### 如果开启了TLSv1.3，那么所有的虚拟主机都需要开启，否则开启会失败！！！

#### 如果开启了TLSv1.3，那么所有的虚拟主机都需要开启，否则开启会失败！！！

### 4.检测

https://myssl.com/

![29-18-09-hWcQsy-MwhmVa](https://up-img.yonghong.tech/pic/2020/07/29-18-09-29-18-09-hWcQsy-MwhmVa-48nHB8.png)


![29-18-10-8qSMAs-Dm7jsg](https://up-img.yonghong.tech/pic/2020/07/29-18-10-29-18-10-8qSMAs-Dm7jsg-hlQldx.png)


![29-18-11-NJed9V-ymQV9n](https://up-img.yonghong.tech/pic/2020/07/29-18-11-29-18-11-NJed9V-ymQV9n-MMdQoT.png)