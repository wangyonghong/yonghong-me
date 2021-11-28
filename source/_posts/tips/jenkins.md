---
title: Jenkins 常用插件、配置
tags:
- Jenkins
- 插件
- 自动化
- k8s
- Kubernates
- 汉化
- NodeJs
- 参数化
categories:
- 技巧
description: Jenkins 常用插件、配置，中文插件、自动化构建、参数化构建、自动化部署、自动化部署到k8s
date: 2020-05-15 22:24:00
updated: 2020-05-15 22:24:00
---

### 0.更新国内镜像

系统管理 -> 插件管理 -> 高级 ->升级站点

[https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json](https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json)

这个链接中只是索引插件，但里面的下载地址仍然指向 updates.jenkins-ci.org ，所以通过改host+nginx反代的方式欺骗Jenkins去清华源下载

### 1.中文插件 Localization: Chinese (Simplified)

Jenkins Core 及其插件的简体中文语言包，由 [Jenkins 中文社区](https://jenkins-zh.cn/about) 维护。

<!--more-->

[https://www.jenkins.io/sigs/chinese-localization/](https://www.jenkins.io/sigs/chinese-localization/)

![截屏2020-05-14下午1.28.34](https://up-img.yonghong.tech/pic/2020/05/截屏2020-05-14%20下午1.28.34.png)

### 2.参数化构建

这个网上都说要安装两个插件，但是我自己试了一下没有安装这两个插件也有这个功能。

```
Build With Parameters 输入框式的参数
Persistent Parameter  下拉框式的参数
```

但是由于中文插件的问题，所以显示可能是中文也可能是英文。

![截屏2020-05-14下午1.17.01](https://up-img.yonghong.tech/pic/2020/05/截屏2020-05-14%20下午1.17.01.png)

![截屏2020-05-14下午1.15.59](https://up-img.yonghong.tech/pic/2020/05/截屏2020-05-14%20下午1.15.59.png)

### 3.rebuild

使用上次的参数重新构建，安装完这个插件后，项目左侧的按钮中会多一个【rebuild last】的选项，点击就可以重新构建而不用重新填写参数了。

![19-17-40-截屏2020-05-19下午5.40.03-TGmsh6](https://up-img.yonghong.tech/pic/2020/05/19-17-40-截屏2020-05-19%20下午5.40.03-TGmsh6.png)

![19-17-40-截屏2020-05-19下午5.40.12-sb4B9v](https://up-img.yonghong.tech/pic/2020/05/19-17-40-截屏2020-05-19%20下午5.40.12-sb4B9v.png)


### 4.node版本控制

系统管理->全局工具配置->NodeJS

可选 nodejs 版本，位数（Force 32bit architecture），可以预装一些工具（yarn 等），设置全局 npm 刷新时间，建议设置稍长一些，不然没过几天就会刷新一次，耗时长（Global npm packages refresh hours）

![截屏2020-05-14下午1.46.54](https://up-img.yonghong.tech/pic/2020/05/截屏2020-05-14%20下午1.46.54.png)

配置好之后就可以在项目中使用了

![截屏2020-05-14下午1.50.30](https://up-img.yonghong.tech/pic/2020/05/截屏2020-05-14%20下午1.50.30.png)

### 5.自动部署到k8s

自动部署到k8s需要Jenkins主机上安装了 Docker, kubectl 工具

还需要安装插件 [Kubernetes CLI Plugin](https://plugins.jenkins.io/kubernetes-cli/)

![5LnHZa](https://up-img.yonghong.tech/pic/2020/05/5LnHZa.jpg)

可以参考 GitHub readme 添加凭据

{% raw %}
```shell
# Create a ServiceAccount named `jenkins-robot` in a given namespace.
$ kubectl -n <namespace> create serviceaccount jenkins-robot

# The next line gives `jenkins-robot` administator permissions for this namespace.
# * You can make it an admin over all namespaces by creating a `ClusterRoleBinding` instead of a `RoleBinding`.
# * You can also give it different permissions by binding it to a different `(Cluster)Role`.
$ kubectl -n <namespace> create rolebinding jenkins-robot-binding --clusterrole=cluster-admin --serviceaccount=<namespace>:jenkins-robot

# Get the name of the token that was automatically generated for the ServiceAccount `jenkins-robot`.
$ kubectl -n <namespace> get serviceaccount jenkins-robot -o go-template --template='{{range .secrets}}{{.name}}{{"\n"}}{{end}}'
jenkins-robot-token-d6d8z

# Retrieve the token and decode it using base64.
$ kubectl -n <namespace> get secrets jenkins-robot-token-d6d8z -o go-template --template '{{index .data "token"}}' | base64 -d
eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2V[...]
```
{% endraw %}

[https://github.com/jenkinsci/kubernetes-cli-plugin/blob/master/README.md#using-the-plugin-from-the-web-interface](https://github.com/jenkinsci/kubernetes-cli-plugin/blob/master/README.md#using-the-plugin-from-the-web-interface)

[https://github.com/jenkinsci/kubernetes-cli-plugin/blob/master/README.md#generating-kubernetes-credentials](https://github.com/jenkinsci/kubernetes-cli-plugin/blob/master/README.md#generating-kubernetes-credentials)

完成上述操作后就可以在执行shell脚本中使用 kubectl 命令了