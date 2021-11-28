---
title: Kubernetes 调整 nodePort 端口范围
tags:
- Kubernetes
- k8s
categories:
- Kubernetes
date: 2020-05-20 22:24:00
updated: 2020-05-20 22:24:00
---

### 问题

默认情况下，k8s 集群 nodePort 分配的端口范围为：30000-32767，如果我们指定的端口不在这个范围就会报类似下面这样的错误：
> Error: release kong failed: Service “kong-kong-admin” is invalid: spec.ports[0].nodePort: Invalid value: 8444: provided port is not in the valid range. The range of valid ports is 30000-32767

<!--more-->

### 解决

解决方法就是调整 kube-apiserver 组件启动参数，指定 nodePort 范围。如果是用 kubeadm 安装的集群，那么 apiserver 是以静态 pod 的形式运行，pod 文件定义在 /etc/kubernetes/manifests/kube-apiserver.yaml。/etc/kubernetes/manifests 目录下是所有静态 pod 文件的定义，kubelet 会监控该目录下文件的变动，只要发生变化，pod 就会重建，响应相应的改动。所以我们修改 /etc/kubernetes/manifests/kube-apiserver.yaml 文件，添加 nodePort 范围参数后会自动生效，无需进行其他操作：<br />vim /etc/kubernetes/manifests/kube-apiserver.yaml<br />在 command 下添加 `--service-node-port-range=1-65535` 参数，修改后会自动生效，无需其他操作:<br />

```yaml
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    component: kube-apiserver
    tier: control-plane
  name: kube-apiserver
  namespace: kube-system
spec:
  containers:
  - command:
    - kube-apiserver
    - --service-node-port-range=1-65535
    - --advertise-address=192.168.26.10
    - --allow-privileged=true
    - --authorization-mode=Node,RBAC
    - --client-ca-file=/etc/kubernetes/pki/ca.crt
    - --enable-admission-plugins=NodeRestriction
    - --enable-bootstrap-token-auth=true
    - --etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt
    - --etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt
    - --etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key
    - --etcd-servers=https://127.0.0.1:2379
    - --insecure-port=0
    - --kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt
    - --kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key
    - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
    - --proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.crt
    - --proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client.key
    - --requestheader-allowed-names=front-proxy-client
    - --requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-ca.crt
    - --requestheader-extra-headers-prefix=X-Remote-Extra-
    - --requestheader-group-headers=X-Remote-Group
    - --requestheader-username-headers=X-Remote-User
    - --secure-port=6443
    - --service-account-key-file=/etc/kubernetes/pki/sa.pub
    - --service-cluster-ip-range=10.96.0.0/12
    - --tls-cert-file=/etc/kubernetes/pki/apiserver.crt
    - --tls-private-key-file=/etc/kubernetes/pki/apiserver.key
    image: registry.aliyuncs.com/google_containers/kube-apiserver:v1.15.2
    imagePullPolicy: IfNotPresent
    livenessProbe:
      failureThreshold: 8
      httpGet:
        host: 192.168.26.10
        path: /healthz
        port: 6443
        scheme: HTTPS
      initialDelaySeconds: 15
      timeoutSeconds: 15
    name: kube-apiserver
    resources:
      requests:
        cpu: 250m
    volumeMounts:
    - mountPath: /etc/ssl/certs
      name: ca-certs
      readOnly: true
    - mountPath: /etc/pki
      name: etc-pki
      readOnly: true
    - mountPath: /etc/kubernetes/pki
      name: k8s-certs
      readOnly: true
  hostNetwork: true
  priorityClassName: system-cluster-critical
  volumes:
  - hostPath:
      path: /etc/ssl/certs
      type: DirectoryOrCreate
    name: ca-certs
  - hostPath:
      path: /etc/pki
      type: DirectoryOrCreate
    name: etc-pki
  - hostPath:
      path: /etc/kubernetes/pki
      type: DirectoryOrCreate
    name: k8s-certs
status: {}
```

### 相关文档

- [http://www.thinkcode.se/blog/2019/02/20/kubernetes-service-node-port-range](http://www.thinkcode.se/blog/2019/02/20/kubernetes-service-node-port-range)
