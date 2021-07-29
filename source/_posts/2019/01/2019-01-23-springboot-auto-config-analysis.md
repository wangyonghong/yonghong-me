---
layout: post
title:  "SpringBoot 自动化配置原理"
category: "springboot"
tags: ["springboot"]
date: 2019-01-23 00:00:00
updated: 2019-01-23 00:00:00
---

springboot用来简化Spring框架带来的大量XML配置以及复杂的依赖管理，让开发人员可以更加关注业务逻辑的开发。

那么 springboot 是如何实现这些复杂的配置呢。我们以一个最小化的例子，新建一个 SpringBoot 项目，仅仅使用 spring-boot-starter-web 和 spring-boot-starter-freemarker

<!-- more -->

下面是 build.gradle 文件

```gradle
buildscript {
    ext {
        springBootVersion = '2.1.2.RELEASE'
    }
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath("org.springframework.boot:spring-boot-gradle-plugin:${springBootVersion}")
    }
}

apply plugin: 'java'
apply plugin: 'org.springframework.boot'
apply plugin: 'io.spring.dependency-management'

group = 'com.example'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '11'

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-freemarker'
    implementation 'org.springframework.boot:spring-boot-starter-web'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
}
```

我们一个一个来看，到底 SpringBoot 是怎么实现这些功能的，先来看 spring-boot-starter-web
[http://central.maven.org/maven2/org/springframework/boot/spring-boot-starter-web/2.1.2.RELEASE/spring-boot-starter-web-2.1.2.RELEASE.pom](http://central.maven.org/maven2/org/springframework/boot/spring-boot-starter-web/2.1.2.RELEASE/spring-boot-starter-web-2.1.2.RELEASE.pom)

```xml
<?xml version="1.0" encoding="utf-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">  
  <modelVersion>4.0.0</modelVersion>  
  <parent> 
    <groupId>org.springframework.boot</groupId>  
    <artifactId>spring-boot-starters</artifactId>  
    <version>2.1.2.RELEASE</version> 
  </parent>  
  <groupId>org.springframework.boot</groupId>  
  <artifactId>spring-boot-starter-web</artifactId>  
  <version>2.1.2.RELEASE</version>  
  <name>Spring Boot Web Starter</name>  
  <description>Starter for building web, including RESTful, applications using Spring MVC. Uses Tomcat as the default embedded container</description>  
  <url>https://projects.spring.io/spring-boot/#/spring-boot-parent/spring-boot-starters/spring-boot-starter-web</url>  
  <organization> 
    <name>Pivotal Software, Inc.</name>  
    <url>https://spring.io</url> 
  </organization>  
  <licenses> 
    <license> 
      <name>Apache License, Version 2.0</name>  
      <url>http://www.apache.org/licenses/LICENSE-2.0</url> 
    </license> 
  </licenses>  
  <developers> 
    <developer> 
      <name>Pivotal</name>  
      <email>info@pivotal.io</email>  
      <organization>Pivotal Software, Inc.</organization>  
      <organizationUrl>http://www.spring.io</organizationUrl> 
    </developer> 
  </developers>  
  <scm> 
    <connection>scm:git:git://github.com/spring-projects/spring-boot.git/spring-boot-starters/spring-boot-starter-web</connection>  
    <developerConnection>scm:git:ssh://git@github.com/spring-projects/spring-boot.git/spring-boot-starters/spring-boot-starter-web</developerConnection>  
    <url>http://github.com/spring-projects/spring-boot/spring-boot-starters/spring-boot-starter-web</url> 
  </scm>  
  <issueManagement> 
    <system>Github</system>  
    <url>https://github.com/spring-projects/spring-boot/issues</url> 
  </issueManagement>  
  <dependencies> 
    <dependency> 
      <groupId>org.springframework.boot</groupId>  
      <artifactId>spring-boot-starter</artifactId>  
      <version>2.1.2.RELEASE</version>  
      <scope>compile</scope> 
    </dependency>  
    <dependency> 
      <groupId>org.springframework.boot</groupId>  
      <artifactId>spring-boot-starter-json</artifactId>  
      <version>2.1.2.RELEASE</version>  
      <scope>compile</scope> 
    </dependency>  
    <dependency> 
      <groupId>org.springframework.boot</groupId>  
      <artifactId>spring-boot-starter-tomcat</artifactId>  
      <version>2.1.2.RELEASE</version>  
      <scope>compile</scope> 
    </dependency>  
    <dependency> 
      <groupId>org.hibernate.validator</groupId>  
      <artifactId>hibernate-validator</artifactId>  
      <version>6.0.14.Final</version>  
      <scope>compile</scope> 
    </dependency>  
    <dependency> 
      <groupId>org.springframework</groupId>  
      <artifactId>spring-web</artifactId>  
      <version>5.1.4.RELEASE</version>  
      <scope>compile</scope> 
    </dependency>  
    <dependency> 
      <groupId>org.springframework</groupId>  
      <artifactId>spring-webmvc</artifactId>  
      <version>5.1.4.RELEASE</version>  
      <scope>compile</scope> 
    </dependency> 
  </dependencies> 
</project>
```

从上面的文件中可以看到 spring-boot-starter-web 引入了 spring-boot-starter，spring-boot-starter-json，spring-boot-starter-tomcat，hibernate-validator，spring-web，spring-webmvc，这些东西构成了基本的 web Application 

接下来我们重点关注一下 spring-boot-starter

[http://central.maven.org/maven2/org/springframework/boot/spring-boot-starter/2.1.2.RELEASE/spring-boot-starter-2.1.2.RELEASE.pom](http://central.maven.org/maven2/org/springframework/boot/spring-boot-starter/2.1.2.RELEASE/spring-boot-starter-2.1.2.RELEASE.pom)

```xml
<?xml version="1.0" encoding="utf-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">  
  <modelVersion>4.0.0</modelVersion>  
  <parent> 
    <groupId>org.springframework.boot</groupId>  
    <artifactId>spring-boot-starters</artifactId>  
    <version>2.1.2.RELEASE</version> 
  </parent>  
  <groupId>org.springframework.boot</groupId>  
  <artifactId>spring-boot-starter</artifactId>  
  <version>2.1.2.RELEASE</version>  
  <name>Spring Boot Starter</name>  
  <description>Core starter, including auto-configuration support, logging and YAML</description>  
  <url>https://projects.spring.io/spring-boot/#/spring-boot-parent/spring-boot-starters/spring-boot-starter</url>  
  <organization> 
    <name>Pivotal Software, Inc.</name>  
    <url>https://spring.io</url> 
  </organization>  
  <licenses> 
    <license> 
      <name>Apache License, Version 2.0</name>  
      <url>http://www.apache.org/licenses/LICENSE-2.0</url> 
    </license> 
  </licenses>  
  <developers> 
    <developer> 
      <name>Pivotal</name>  
      <email>info@pivotal.io</email>  
      <organization>Pivotal Software, Inc.</organization>  
      <organizationUrl>http://www.spring.io</organizationUrl> 
    </developer> 
  </developers>  
  <scm> 
    <connection>scm:git:git://github.com/spring-projects/spring-boot.git/spring-boot-starters/spring-boot-starter</connection>  
    <developerConnection>scm:git:ssh://git@github.com/spring-projects/spring-boot.git/spring-boot-starters/spring-boot-starter</developerConnection>  
    <url>http://github.com/spring-projects/spring-boot/spring-boot-starters/spring-boot-starter</url> 
  </scm>  
  <issueManagement> 
    <system>Github</system>  
    <url>https://github.com/spring-projects/spring-boot/issues</url> 
  </issueManagement>  
  <dependencies> 
    <dependency> 
      <groupId>org.springframework.boot</groupId>  
      <artifactId>spring-boot</artifactId>  
      <version>2.1.2.RELEASE</version>  
      <scope>compile</scope> 
    </dependency>  
    <dependency> 
      <groupId>org.springframework.boot</groupId>  
      <artifactId>spring-boot-autoconfigure</artifactId>  
      <version>2.1.2.RELEASE</version>  
      <scope>compile</scope> 
    </dependency>  
    <dependency> 
      <groupId>org.springframework.boot</groupId>  
      <artifactId>spring-boot-starter-logging</artifactId>  
      <version>2.1.2.RELEASE</version>  
      <scope>compile</scope> 
    </dependency>  
    <dependency> 
      <groupId>javax.annotation</groupId>  
      <artifactId>javax.annotation-api</artifactId>  
      <version>1.3.2</version>  
      <scope>compile</scope> 
    </dependency>  
    <dependency> 
      <groupId>org.springframework</groupId>  
      <artifactId>spring-core</artifactId>  
      <version>5.1.4.RELEASE</version>  
      <scope>compile</scope> 
    </dependency>  
    <dependency> 
      <groupId>org.yaml</groupId>  
      <artifactId>snakeyaml</artifactId>  
      <version>1.23</version>  
      <scope>runtime</scope> 
    </dependency> 
  </dependencies> 
</project>
```

这里引入了 spring-boot，spring-boot-autoconfigure（这里是重点），spring-boot-starter-logging，javax.annotation-api（注解都在这里），spring-core，snakeyaml（解析 yml）

看看 spring-boot-autoconfigure 里有什么

![29-18-01-ScreenShot2019-01-23at1.06.02PM-C5WlNp](https://up-img.yonghong.tech/pic/2021/07/29-18-01-Screen%20Shot%202019-01-23%20at%201.06.02%20PM-C5WlNp.png)
![29-18-01-ScreenShot2019-01-23at1.27.08PM-HPADML](https://up-img.yonghong.tech/pic/2021/07/29-18-01-Screen%20Shot%202019-01-23%20at%201.27.08%20PM-HPADML.png)

这里写到

```java
@Configuration
@ConditionalOnClass({ freemarker.template.Configuration.class,
		FreeMarkerConfigurationFactory.class }) // 这里说明只有当满足条件时才会触发这个配置
@EnableConfigurationProperties(FreeMarkerProperties.class)
@Import({ FreeMarkerServletWebConfiguration.class,
		FreeMarkerReactiveWebConfiguration.class, FreeMarkerNonWebConfiguration.class })
public class FreeMarkerAutoConfiguration {
    // 省略。。。
}
```

接下来我们看 spring-boot-starter-freemarker 中有什么

[http://central.maven.org/maven2/org/springframework/boot/spring-boot-starter-freemarker/2.1.2.RELEASE/spring-boot-starter-freemarker-2.1.2.RELEASE.pom](http://central.maven.org/maven2/org/springframework/boot/spring-boot-starter-freemarker/2.1.2.RELEASE/spring-boot-starter-freemarker-2.1.2.RELEASE.pom)

```xml
<?xml version="1.0" encoding="utf-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">  
  <modelVersion>4.0.0</modelVersion>  
  <parent> 
    <groupId>org.springframework.boot</groupId>  
    <artifactId>spring-boot-starters</artifactId>  
    <version>2.1.2.RELEASE</version> 
  </parent>  
  <groupId>org.springframework.boot</groupId>  
  <artifactId>spring-boot-starter-freemarker</artifactId>  
  <version>2.1.2.RELEASE</version>  
  <name>Spring Boot FreeMarker Starter</name>  
  <description>Starter for building MVC web applications using FreeMarker views</description>  
  <url>https://projects.spring.io/spring-boot/#/spring-boot-parent/spring-boot-starters/spring-boot-starter-freemarker</url>  
  <organization> 
    <name>Pivotal Software, Inc.</name>  
    <url>https://spring.io</url> 
  </organization>  
  <licenses> 
    <license> 
      <name>Apache License, Version 2.0</name>  
      <url>http://www.apache.org/licenses/LICENSE-2.0</url> 
    </license> 
  </licenses>  
  <developers> 
    <developer> 
      <name>Pivotal</name>  
      <email>info@pivotal.io</email>  
      <organization>Pivotal Software, Inc.</organization>  
      <organizationUrl>http://www.spring.io</organizationUrl> 
    </developer> 
  </developers>  
  <scm> 
    <connection>scm:git:git://github.com/spring-projects/spring-boot.git/spring-boot-starters/spring-boot-starter-freemarker</connection>  
    <developerConnection>scm:git:ssh://git@github.com/spring-projects/spring-boot.git/spring-boot-starters/spring-boot-starter-freemarker</developerConnection>  
    <url>http://github.com/spring-projects/spring-boot/spring-boot-starters/spring-boot-starter-freemarker</url> 
  </scm>  
  <issueManagement> 
    <system>Github</system>  
    <url>https://github.com/spring-projects/spring-boot/issues</url> 
  </issueManagement>  
  <dependencies> 
    <dependency> 
      <groupId>org.springframework.boot</groupId>  
      <artifactId>spring-boot-starter</artifactId>  
      <version>2.1.2.RELEASE</version>  
      <scope>compile</scope> 
    </dependency>  
    <dependency> 
      <groupId>org.freemarker</groupId>  
      <artifactId>freemarker</artifactId>  
      <version>2.3.28</version>  
      <scope>compile</scope> 
    </dependency>  
    <dependency> 
      <groupId>org.springframework</groupId>  
      <artifactId>spring-context-support</artifactId>  
      <version>5.1.4.RELEASE</version>  
      <scope>compile</scope> 
    </dependency> 
  </dependencies> 
</project>
```

这里引入了 freemarker，spring-context-support，我们查找一下上面提到的两个类 freemarker.template.Configuration.class, FreeMarkerConfigurationFactory.class


freemarker中

![29-18-02-ScreenShot2019-01-23at1.35.44PM-Xwn9iV](https://up-img.yonghong.tech/pic/2021/07/29-18-02-Screen%20Shot%202019-01-23%20at%201.35.44%20PM-Xwn9iV.png)
![29-18-02-ScreenShot2019-01-23at1.37.37PM-lDimkH](https://up-img.yonghong.tech/pic/2021/07/29-18-02-Screen%20Shot%202019-01-23%20at%201.37.37%20PM-lDimkH.png)


所以说一开始我们加入了一个 spring-boot-starter-freemarker 依赖，这个依赖中存在 freemarker 和 spring-context-support 的 lib，满足了FreeMarkerAutoConfiguration 中的 ConditionalOnClass 里写的 freemarker.template.Configuration.class 这个类和 FreeMarkerConfigurationFactory.class 存在于 classpath 中。于是就可以正常的使用了。

其他依赖也同理