---
layout: post
title:  "SpringBoot Util 工具类读取 application.properties 文件中的值"
category: "springboot"
tags: ["springboot"]
date: 2019-01-17 00:00:00
updated: 2019-01-17 00:00:00
---

实际开发中会遇到不同的生产环境的参数不一样，要根据生产环境来选择实际的参数。

比如我后端需要有一个 url 请求，这个 url 请求在不同的环境下（dev,test,alpha,beta,product）需要访问相应的链接。那么我可以在 application.properties 或者 application.yml 文件中写不同的 url, 根据环境变量判断使用哪一个。

<!-- more -->

所以，看我的，下面是解决办法

```properties
# application.properties
url.auth.prefix.dev=http://dev.xx.com
url.auth.prefix.test=http://test.xx.com
url.auth.prefix.alpha=http://alpha.xx.com
url.auth.prefix.beta=http://beta.xx.com
url.auth.prefix.prod=http://xx.com

url.api.login=/auth/login
```


ENVUtil.java

```java
// 要有这个注解，如果不是 Bean，也不会自动加载
@Component
public class ENVUtil {

    private static String env;

    // 注意这里不能是 static 静态方法，否则会失效
    @Value("${env}")
    public void setEnv(String env) {
        ENVUtil.env = env;
    }

    public static ENV getENV() {
        try {
            // string 转 enum 的方法
            return ENV.valueOf(env.toUpperCase());
        } catch (Exception e) {
            return ENV.DEV;
        }
    }
}
```

ENV.java

```java
public enum  ENV {
    // 环境 dev, test, alpha, beta, prod
    DEV,
    TEST,
    ALPHA,
    BETA,
    PROD
}
```


URLUtil.java

```java
@Component
public class URLUtil {

    private static String loginUrl;

    private static ENV env = ENVUtil.getENV();

    private static String authDevPrefix;

    private static String authTestPrefix;

    private static String authAlphaPrefix;

    private static String authBetaPrefix;

    private static String authProdPrefix;

    private static String loginApi;

    @Value("${url.auth.prefix.dev}")
    public void setAuthDevPrefix(String authDevPrefix) {
        URLUtil.authDevPrefix = authDevPrefix;
    }

    @Value("${url.auth.prefix.test}")
    public void setAuthTestPrefix(String authTestPrefix) {
        URLUtil.authTestPrefix = authTestPrefix;
    }

    @Value("${url.auth.prefix.alpha}")
    public void setAuthAlphaPrefix(String authAlphaPrefix) {
        URLUtil.authAlphaPrefix = authAlphaPrefix;
    }

    @Value("${url.auth.prefix.beta}")
    public void setAuthBetaPrefix(String authBetaPrefix) {
        URLUtil.authBetaPrefix = authBetaPrefix;
    }

    @Value("${url.auth.prefix.prod}")
    public void setAuthProdPrefix(String authProdPrefix) {
        URLUtil.authProdPrefix = authProdPrefix;
    }

    @Value("${url.api.login}")
    public void setLoginApi(String loginApi) {
        URLUtil.loginApi = loginApi;
    }

    // 初始化 Bean 之后会执行这个注解的方法，前提是这个类是 Bean
    @PostConstruct
    public void init() {
        switch (env) {
            case DEV:
                loginUrl = authDevPrefix + loginApi;
                break;
            case TEST:
                loginUrl = authTestPrefix + loginApi;
                break;
            case ALPHA:
                loginUrl = authAlphaPrefix + loginApi;
                break;
            case BETA:
                loginUrl = authBetaPrefix + loginApi;
                break;
            case PROD:
                loginUrl = authProdPrefix + loginApi;
                break;
            default:
                loginUrl = authDevPrefix + loginApi;
        }
    }

    public static String getLoginUrl() {
        return loginUrl;
    }
}
```