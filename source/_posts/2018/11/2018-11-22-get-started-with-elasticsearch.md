---
layout: post
title:  "ElasticSearch 入门"
category: "ElasticSearch"
tags: ["ElasticSearch"]
date: 2018-11-22 00:00:00
updated: 2018-11-22 00:00:00
---

### 单实例安装

安装 ElasticSearch，首先到官网下载 [https://www.elastic.co/downloads/elasticsearch](https://www.elastic.co/downloads/elasticsearch)

<!-- more -->

下载 tar.gz 文件，下载好之后解压

```shell
tar -xvf elasticsearch-x.x.x.tar.gz
```

进到解压好的目录里之后，就可以执行下面的命令运行了

```shell
./bin/elasticsearch
```

如果看到 started 字样，说明已经启动了

再来确认一下是不是启动了

```shell
$ curl http://localhost:9200
{
  "name" : "CW4wfvI",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "jTCyqCjbQcq9DWekXXlfSg",
  "version" : {
    "number" : "6.5.1",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "8c58350",
    "build_date" : "2018-11-16T02:22:42.182257Z",
    "build_snapshot" : false,
    "lucene_version" : "7.5.0",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```


安装 ElasticSearch 的 web 前端管理界面 https://github.com/mobz/elasticsearch-head

- `git clone git://github.com/mobz/elasticsearch-head.git`
- `cd elasticsearch-head`
- `npm install`
- `npm run start`

接下来，我们用浏览器打开 `http://localhost:9100`

发现未连接 ElasticSearch，为什么呢？我们看到 elasticsearch-head 的文档中写了，想要用这个服务，必须在 ElasticSearch 的配置文件中开启 CORS

所以，我们修改一下 config 目录中的 elasticsearch.yml 文件，在文件的末尾添加两行

```yml
http.cors.enabled: true
http.cors.allow-origin: "*"
```

这样之后，我们重启 ElasticSearch，再次查看，集群健康值: green (0 of 0)，已经是正常的了。

### 分布式安装

拷贝三份，elasticsearch-master，elasticsearch-slave1，elasticsearch-slave2

master 配置

```yml
cluster.name: 0xl2oot
node.name: master
node.master: true

network.host: 127.0.0.1
```

```shell
$ curl http://localhost:9200
{
  "name" : "master",
  "cluster_name" : "0xl2oot",
  "cluster_uuid" : "jTCyqCjbQcq9DWekXXlfSg",
  "version" : {
    "number" : "6.5.1",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "8c58350",
    "build_date" : "2018-11-16T02:22:42.182257Z",
    "build_snapshot" : false,
    "lucene_version" : "7.5.0",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

slave1 配置

```yml
cluster.name: 0xl2oot
node.name: slave1

network.host: 127.0.0.1
http.port: 9201
discovery.zen.ping.unicast.hosts: ["127.0.0.1"]
```

```shell
curl http://localhost:9201
{
  "name" : "slave1",
  "cluster_name" : "0xl2oot",
  "cluster_uuid" : "0fQo4KuxQhSh4g6HZmkwZA",
  "version" : {
    "number" : "6.5.1",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "8c58350",
    "build_date" : "2018-11-16T02:22:42.182257Z",
    "build_snapshot" : false,
    "lucene_version" : "7.5.0",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

slave2 配置

```yml
cluster.name: 0xl2oot
node.name: slave2

network.host: 127.0.0.1
http.port: 9202
discovery.zen.ping.unicast.hosts: ["127.0.0.1"]
```

```shell
$ curl http://localhost:9202
{
  "name" : "slave2",
  "cluster_name" : "0xl2oot",
  "cluster_uuid" : "0fQo4KuxQhSh4g6HZmkwZA",
  "version" : {
    "number" : "6.5.1",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "8c58350",
    "build_date" : "2018-11-16T02:22:42.182257Z",
    "build_snapshot" : false,
    "lucene_version" : "7.5.0",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

打开 http://localhost:9100 查看

![29-17-53-ScreenShot2018-11-22at12.10.42PM-8uCfEC](https://up-img.yonghong.tech/pic/2021/07/29-17-53-Screen%20Shot%202018-11-22%20at%2012.10.42%20PM-8uCfEC.png)


### 在远程的机器上进行安装


如果是在远程的服务器上或者是虚拟机上进行安装，如果有需要暴露出端口，那么需要修改 host 为 0.0.0.0 


```
network.host: 0.0.0.0
```

并且添加下面的一行


```
transport.host: localhost
```

最新版的 Ubuntu 18.10 还需要修改防火墙配置

```
sudo ufw allow 9200 # 需要什么就暴露什么端口
```

查看防火墙信息 

```
sudo ufw status
```

