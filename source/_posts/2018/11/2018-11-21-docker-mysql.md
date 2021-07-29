---
layout: post
title:  "使用 docker 安装多版本的 MySQL"
category: "docker"
tags: ["MySQL", "docker"]
date: 2018-11-21 00:00:00
updated: 2018-11-21 00:00:00
---

首先从 docker 官网下载安装 docker。Windows 和 macOS 安装都是图形界面的比较方便

Linux 的话，有的可能也比较简单，比如 Ubuntu

<!-- more -->

```
sudo snap install docker
```

检查 docker 安装是否成功，出现类似下面的信息就是安装好了

```shell
$ docker version
Client: Docker Engine - Community
 Version:           18.09.0
 API version:       1.39
 Go version:        go1.10.4
 Git commit:        4d60db4
 Built:             Wed Nov  7 00:47:43 2018
 OS/Arch:           darwin/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          18.09.0
  API version:      1.39 (minimum version 1.12)
  Go version:       go1.10.4
  Git commit:       4d60db4
  Built:            Wed Nov  7 00:55:00 2018
  OS/Arch:          linux/amd64
  Experimental:     true

```

从 docker hub 上找到 MySQL 的镜像，查询得到 MySQL 的版本主要有 5.6 5.7 和 8.0。

下面我们分别拉取镜像进行启动

```shell
docker pull mysql:5.6
docker pull mysql:5.7
docker pull mysql:8.0
```

mysql 是官方的镜像，冒号后面跟的是版本号。为了方便，我们把三个 mysql 的容器分别叫做 mysql56, mysql57, mysql80

```shell
docker run -p 3316:3306 --name mysql56 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.6
docker run -p 3317:3306 --name mysql57 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7
docker run -p 3318:3306 --name mysql80 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:8.0
```

> -p 3316:3306 是把容器的3306端口映射到本机的3316端口
> --name 是给运行的容器一个别名
> -e MYSQL_ROOT_PASSWORD=123456 是初始化 MySQL 的密码


这样的话我们连接 MySQL 的命令就是下面的


```shell
mysql --port 3316 -uroot -h127.0.0.1 -p123456
mysql --port 3317 -uroot -h127.0.0.1 -p123456
mysql --port 3318 -uroot -h127.0.0.1 -p123456
```

但是这样可能不太行。

因为直接从外面连 MySQL 可能是没有权限的

我们先进入容器

```shell
docker exec -it mysql80 bash
```

这样就相当于进入了容器中的 bash

```shell
mysql -uroot -p123456
```

进入 MySQL

```sql
update mysql.user set host="%" where user="root";
flush privileges;
```

这样就可以了。

一般情况下 MySQL5.6 和 MySQL5.7 应该是没问题了，但是 MySQL8.0 的密码验证方式变了，我们应该要改一下

```sql
update mysql.user set host="%" where user="root";
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456';
flush privileges;
```

这样就大功告成

```shell
$ mysql --port 3318 -uroot -h127.0.0.1 -p123456
Warning: Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 49
Server version: 8.0.13 MySQL Community Server - GPL

Copyright (c) 2000, 2017, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> select version();
+-----------+
| version() |
+-----------+
| 8.0.13    |
+-----------+
1 row in set (0.01 sec)
```

安装 phpmyadmin

```
docker run --name myadmin56 -d --link mysql56:db -p 3600:80 phpmyadmin/phpmyadmin
```

访问 localhost:3600 即可


最后我们看一下 docker 其他常用的命令

| 命令 | 功能 |
| -- | -- |
| docker ps  | 查看正在运行的容器 |
| docker ps -a | 查看所有的容器 |
| docker stop mysql56 | 停止 mysql56 这个容器 |
| docker start mysql56 | 启动 mysql56 这个容器 |
| docker images | 查看 docker 所有镜像 |
| docker image list | 同上 |
| docker rm mysql56 | 删除 mysql56 这个容器 |
| docker rmi mysql:5.6 | 删除 mysql 5.6 版本的 image | 


