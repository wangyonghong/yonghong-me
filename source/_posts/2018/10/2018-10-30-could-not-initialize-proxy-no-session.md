---
layout: post
title:  "could not initialize proxy - no Session"
category: "SpringBoot"
tags: ["Java", "SpringBoot", "spring-data-jpa"]
date: 2018-10-30 00:00:00
updated: 2018-10-30 00:00:00
---

### 报错

org.hibernate.LazyInitializationException: could not initialize proxy [com.example.demo.dataobject.User#1] - no Session

<!-- more -->

### 解决 

解决LazyInitializationException异常大概有这么几种方式

1.关闭LazyInitialization, 将fetch设成eager

2.在spring boot的配置文件application.properties添加spring.jpa.open-in-view=true

3.用spring 的OpenSessionInViewFilter

第一种方式显然不好，无法使用到延迟加载的特性，会带来性能问题

后面两种方式只能用在Servlet容器下,而当我们在spring boot环境下运行单元测试的时候是无法启用OpenSessionInViewFilter的

其实要解决这种情况下的问题也很简单，只需要在单元测试方法@Transactional注解即可解决

```java
    @Test
    @Transactional
    public void getOneTest() {
        User user = repository.getOne(1);
        System.out.println(user.toString());
    }
```


### 参考文献

- [解决Spring Data JPA延迟加载could not initialize proxy - no Session 错误](https://www.cnblogs.com/onone/articles/8962914.html)