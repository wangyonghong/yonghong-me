---
layout: post
title:  "使用 OpenGrok 阅读优秀开源代码"
category: "opensource"
tags: ["opensource"]
date: 2019-02-01 00:00:00
updated: 2019-02-01 00:00:00
---

OpenGrok is a fast and usable source code search and cross reference engine, written in Java

OpenGrok 的项目地址是 [https://github.com/oracle/opengrok](https://github.com/oracle/opengrok)

OpenGrok 还提供了 docker 的安装方式 [https://hub.docker.com/r/opengrok/docker/](https://hub.docker.com/r/opengrok/docker/)

<!-- more -->

安装运行：

The container exports ports 8080 for OpenGrok.

```shell
docker run -d -v :/src -p 8080:8080 opengrok/docker:latest
```

The volume mounted to /src should contain the projects you want to make searchable (in sub directories). You can use common revision control checkouts (git, svn, etc...) and OpenGrok will make history and blame information available.

By default, the index will be rebuild every ten minutes. You can adjust this time (in Minutes) by passing the REINDEX environment variable:

```shell
docker run -d -e REINDEX=30 -v :/src -p 8080:8080 opengrok/docker:latest
```

Setting REINDEX to 0 will disable automatic indexing. You can manually trigger an reindex using docker exec:

```shell
docker exec /scripts/index.sh
```