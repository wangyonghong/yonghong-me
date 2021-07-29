---
layout: post
title:  "org.hibernate.HibernateException: Access to ..."
category: "SpringBoot"
tags: ["Java", "SpringBoot"]
date: 2018-10-30 00:00:00
updated: 2018-10-30 00:00:00
---

### 报错

org.hibernate.HibernateException: Access to DialectResolutionInfo cannot be null when 'hibernate.dialect' not set

在配置 SpringBoot Jpa 时，觉得已经配置好了，当运行的时候，却报了这个错。

<!-- more -->

### 原因

有可能是选用的数据库不正确，或者数据库的用户名密码错了。还有可能是因为没有设置 Hibernate 的 Dialect。
但是经过我测试，一般情况下是不用配置 Dialect 的，因为默认已经配置好了。主要原因可能是数据库配置不正确，而不是 Dialect。

Hibernate SQL 方言

如果需要配置的话，是这样配置的

1.采用 application.properties 文件

```
spring.jpa.database-platform=org.hibernate.dialect.MySQL5Dialect
```

2.采用 application.yml

```xml
database-platform: org.hibernate.dialect.MySQL5Dialect
```

常见的 Dialect


| RDBMS                | Dialect                                     |
| -------------------- | ------------------------------------------- |
| Oracle (any version) | org.hibernate.dialect.OracleDialect         |
| Oracle9i             | org.hibernate.dialect.Oracle9iDialect       |
| Oracle10g            | org.hibernate.dialect.Oracle10gDialect      |
| MySQL                | org.hibernate.dialect.MySQLDialect          |
| MySQL with InnoDB    | org.hibernate.dialect.MySQLInnoDBDialect    |
| MySQL with MyISAM    | org.hibernate.dialect.MySQLMyISAMDialect    |
| DB2                  | org.hibernate.dialect.DB2Dialect            |
| DB2 AS/400           | org.hibernate.dialect.DB2400Dialect         |
| DB2 OS390            | org.hibernate.dialect.DB2390Dialect         |
| Microsoft SQL Server | org.hibernate.dialect.SQLServerDialect      |
| Sybase               | org.hibernate.dialect.SybaseDialect         |
| Sybase Anywhere      | org.hibernate.dialect.SybaseAnywhereDialect |
| PostgreSQL           | org.hibernate.dialect.PostgreSQLDialect     |
| SAP DB               | org.hibernate.dialect.SAPDBDialect          |
| Informix             | org.hibernate.dialect.InformixDialect       |
| HypersonicSQL        | org.hibernate.dialect.HSQLDialect           |
| Ingres               | org.hibernate.dialect.IngresDialect         |
| Progress             | org.hibernate.dialect.ProgressDialect       |
| Mckoi SQL            | org.hibernate.dialect.MckoiDialect          |
| Interbase            | org.hibernate.dialect.InterbaseDialect      |
| Pointbase            | org.hibernate.dialect.PointbaseDialect      |
| FrontBase            | org.hibernate.dialect.FrontbaseDialect      |
| Firebird             | org.hibernate.dialect.FirebirdDialect       |

### 参考文献

- [GitHub - Hibernate Dialect](https://github.com/hibernate/hibernate-orm/tree/master/hibernate-core/src/main/java/org/hibernate/dialect)
- [SQL Dialects in Hibernate](https://www.javatpoint.com/dialects-in-hibernate)
- [Hibernate Doc](http://docs.jboss.org/hibernate/orm/5.3/javadocs/)
- [Spring Boot下使用JPA报错：'hibernate.dialect' not set的解决办法](https://blog.csdn.net/BeauXie/article/details/75948457)