---
layout: post
title:  "web 服务器 lnmp 的使用"
category: "Linux"
tags: ["Linux", "linux", "web", "lnmp"]
date: 2019-03-19 00:00:00
updated: 2018-03-19 00:00:00
---

lnmp 官网 [https://lnmp.org/](https://lnmp.org/)

安装文档 [https://lnmp.org/install.html](https://lnmp.org/install.html)

<!-- more -->

很简单按照教程安装

```
wget http://soft.vpser.net/lnmp/lnmp1.5.tar.gz -cO lnmp1.5.tar.gz && tar zxf lnmp1.5.tar.gz && cd lnmp1.5 && ./install.sh lnmp
```

添加一个站点：

[https://lnmp.org/faq/lnmp-vhost-add-howto.html](https://lnmp.org/faq/lnmp-vhost-add-howto.html)


```
lnmp vhost add
```

> 注意：如果需要使用 https，则需要提前设置域名解析，最好等几分钟后在设置，这样 DNS 中才能查询得到。

FAQ [https://lnmp.org/faq.html](https://lnmp.org/faq.html)

Nginx 默认是安装在 /usr/local/nginx/ 目录中的

Nginx 的默认配置文件在 `/usr/local/nginx/conf/nginx.conf` 中。这里的 http {} 中有一个 server {} ，这是默认的 server， 监听 80 端口，web 文件在 /home/wwwroot/default 中，server_name 为 _，意味着接收。

http {} 中还有一行 include vhost/*.conf; 这意味着 /usr/local/nginx/conf/vhost/ 文件夹下的 .conf 文件都会被引入到这里。

如果将 `/usr/local/nginx/conf/nginx.conf` 文件中的 server {} 删除，并且没有直接访问 IP 配置的 server，那么访问 IP 地址则会从 vhost 中选取第一个（笔者测试结果是这样）。

详细的配置参考
- [https://www.nginx.com/resources/wiki/start/topics/examples/full/](https://www.nginx.com/resources/wiki/start/topics/examples/full/)
- [https://docs.nginx.com/nginx/admin-guide/web-server/web-server/](https://docs.nginx.com/nginx/admin-guide/web-server/web-server/)
