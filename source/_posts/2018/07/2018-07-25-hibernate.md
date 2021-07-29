---
layout: post
title: Hibernate 原理及实战（一）
categories: [Hibernate]
tags: [Hibernate, Java]
date: 2018-07-25 00:00:00
updated: 2018-07-25 00:00:00
---

### 1.三层架构分层

> 三层架构(3-tier architecture) 通常意义上的三层架构就是将整个业务应用划分为：**界面层（User Interface layer）、业务逻辑层（Business Logic Layer）、数据访问层（Data access layer）**。区分层次的目的即为了“**高内聚低耦合**”的思想。在软件体系架构设计中，分层式结构是最常见，也是最重要的一种结构。**微软**推荐的分层式结构一般分为三层，从下至上分别为：**数据访问层、业务逻辑层（又或称为领域层）、表示层**。
> 
> (注：层，英文是tier（物理上）、layer（逻辑上）。)

<!-- more -->

1.数据访问层：主要是对非原始数据（数据库或者文本文件等存放数据的形式）的操作层，而不是指原始数据，也就是说，是对数据库的操作，而不是数据，具体为业务逻辑层或表示层提供数据服务。

2.业务逻辑层：主要是针对具体的问题的操作，也可以理解成对数据层的操作，对数据业务逻辑处理，如果说数据层是积木，那逻辑层就是对这些积木的搭建。

3.界面层：主要表示WEB方式，也可以表示成WINFORM方式，WEB方式也可以表现成：aspx，如果逻辑层相当强大和完善，无论表现层如何定义和更改，逻辑层都能完善地提供服务。

---

表现层（Presentation layer）：表现层可以说是距离用户最近的层，主要是用于接收用户输入的数据和显示处理后用户需要的数据。一般表现为界面，用户通过界面输入查询数据和得到需要的数据。

业务逻辑层（Business Logic Layer）：业务逻辑层是处于表现层和数据访问层之间，主要是从数据库中得到数据然后对数据进行逻辑处理。

数据访问层（Data access layer）：数据访问层是直接和数据库打交道的，对数据进行“增、删、改、查”等基本的操作。

---


### 2.MVC 思想

MVC 全名是 Model View Controller，是模型(model)－视图(view)－控制器(controller)的缩写。MVC是一个设计模式，它强制性的使应用程序的输入、处理和输出分开。使用MVC应用程序被分成三个核心部件：模型（M）、视图（V）、控制器（C），它们各自处理自己的任务。

Model（模型）是应用程序中用于处理应用程序数据逻辑的部分。

通常模型对象负责在数据库中存取数据。

View（视图）是应用程序中处理数据显示的部分。

通常视图是依据模型数据创建的。

Controller（控制器）是应用程序中处理用户交互的部分。

通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据。


### 3.一些概念

#### 3.1.模型 Model

模型是MVC中的概念，指的是读取数据和改变数据的操作（业务逻辑）。一开始我们直接把和数据库相关的代码放在模型里(sql直接写在代码中)，这样就会导致以后的维护相当麻烦。业务逻辑的修改都需要开发者重新写sql，如果项目需要分库，需要将sql语句抽出来，放到单独的一层。这一层就是DAL(数据访问层)。

#### 3.2.持久层Persistence

持久层只是一个逻辑概念而已，主要任务是负责把数据保存起来，一般是指保存至数据库或者文件，也可以负责完成与之相关的行为。

持久层指的是把数据长期保存起来，如数据库把数据长期保存在硬盘里，XML也可以长期保存数据，还有如果把数据存放到指定文件中，也可以成为持久层。

持久化可以理解为动词。Java中的Hibernate做的就是持久化的操作，主要是对数据库底层的OR映射，这样我们就不必关心讨厌的关系映射了，直接操作对象就可以了。

#### 3.3.DAL Data Access Layer，数据访问层

DAL是三层架构(表现层，业务逻辑层，数据访问层)中的数据访问层，是一个概念或者说是一个方案，它由许多DAO组成，或者说由DAO具体实现，是把和数据库相关的代码封装起来，这样当我们执行分库时，便只用调整DAO的代码了，模型根本不用关心它使用的数据是放在A库还是B库。

设计数据访问层接口的目的是让业务逻辑层不去调用具体的数据访问层的实现（不依赖于数据访问层具体的实现技术），这样的好处是，业务逻辑不必管数据访问层具体是什么技术来实现的，接口是不变的。

使用DAL的优势如下：

1、开发人员可以只关注整个结构中的其中某一层；

2、可以很容易的用新的实现来替换原有层次的实现；

3、可以降低层与层之间的依赖；

4、有利于标准化；

5、利于各层逻辑的复用。

概括来说，分层式设计可以达至如下目的：分散关注、松散耦合、逻辑复用、标准定义。

降低耦合性的实际应用如下：

业务逻辑不必管数据访问层具体是什么技术来实现的，接口是不变的，数据访问层可以用jdbc来实现，也可以用hibernate来实现，而且更换起来不是非常麻烦，这样耦合就降低了

#### 3.4.DAO data access object，数据访问对象

DAO是一个软件设计的指导原则，在核心J2EE模式中是这样介绍DAO模式的：为了建立一个健壮的J2EE应用，应该将所有对数据源的访问操作抽象封装在一个公共API中。用程序设计的语言来说，就是建立一个接口，接口中定义了此应用程序中将会用到的所有事务方法。在这个应用程序中，当需要和数据源进行交互的时候则使用这个接口，并且编写一个单独的类来实现这个接口在逻辑上对应这个特定的数据存储。

顾名思义就是与数据库打交道，夹在业务逻辑与数据库资源中间，是DAL的具体实现。

简单的说 dao层 就是对数据库中数据的增删改查等操作封装在专门的类里面，在业务逻辑层中如果要访问数据的时候，直接调用该dao类（包括了如何访问数据库和数据的增删改查等等代码），就可以返回数据，而不需要再在业务逻辑层中写这些代码。

#### 3.5.ORM object-relational mapping，对象关系映射

ORM也是一种对数据库访问的封装，然而ORM不像DAO只是一种软件设计的指导原则，强调的是系统应该层次分明，更像是一种工具，有着成熟的产品，比如JAVA界非常有名的Hibernate，以及很多PHP框架里自带的ORM库。他们的好处在于能将你程序中的数据对象自动地转化为关系型数据库中对应的表和列，数据对象间的引用也可以通过这个工具转化为表之间的JOIN。使用ORM的好处就是使得你的开发几乎不用接触到SQL语句。创建一张表，声明一个对应的类，然后你就只用和这个类的实例进行交互了，至于这个对象里的数据该怎么存储又该怎么获取，通通不用关心。

#### 3.6.Active Record

Active Record则是随着ruby on rails的流行而火起来的一种ORM模式，它是把负责持久化的代码也集成到数据对象中，即这个数据对象知道怎样把自己存到数据库里。这与以往的ORM有不同，传统的ORM会把数据对象和负责持久化的代码分开，数据对象只是一个单纯包含数据的结构体，在模型层和ORM层中传递。而在Active Record中，模型层集成了ORM的功能，他们既代表实体，包含业务逻辑，又是数据对象，并负责把自己存储到数据库中，当然，存储的这一部分代码是早已在模型的父类中实现好了的，属于框架的一部分，模型只需简单的调用父类的方法来完成持久化而已。


### 4.什么是 Hibernate

> [http://hibernate.org/](http://hibernate.org/)

从不同的角度有不同的理解：

它是连接java应用程序与关系数据库的中间件；

它对JDBC API进行了封装，负责Java对象的持久化；

在分层软件框架中它位于持久化层，封装了所有数据访问细节，使业务逻辑层可以专注实现业务逻辑；

它是一种ORM映射工具，能够建立面向对象模型与关系数据模型的映射。

Hibernate 将 Java 类映射到数据库表中，从 Java 数据类型中映射到 SQL 数据类型中，并把开发人员从 95% 的公共数据持续性编程工作中解放出来。

### 5.实战（IntelliJ IDEA）

#### 5.1.创建一个 Hibernate Project

使用 IDEA Ultimate 版本新建一个 Java Project，勾选上 Hibernate 选项和下面的 第一个选项 Create default hibernate configuration and main class 选项(可以根据需求选择版本，这里我选择的是当前最新的版本，Hibernate5.3.2)。Next 下一步即可。

![new-project](https://up-img.yonghong.tech/pic/2021/07/29-17-01-new-project-Wr12C9.png)

这样的话就会自动将 Hibernate 添加到自己的项目中，并且自动生成了一部分 Hibernate 配置文件。

如图：
![project-structure](https://up-img.yonghong.tech/pic/2021/07/29-17-08-project-structure-I86YpX.png)

#### 5.2.引入 MySQL JDBC Driver

在项目上右键 Open Module Settings -> Libraries

点击加号 From Maven 

![mysql-jdbc-driver](https://up-img.yonghong.tech/pic/2021/07/29-17-08-mysql-jdbc-driver-C5L45d.png)

输入 mysql:mysql-connector-java:8.0.11 (当前最新版本，可以根据需求选择合适的版本) 勾选 Download to (path to lib)

#### 5.3.创建一个实体类 Student.java

```java
package com.example;

public class Student {
    private int id;
    private String name;
    private String sex;
    private String address;
    private String password;

    public Student() {}

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
```

#### 5.4.创建映射文件 Student.hbm.xml

```xml
<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE hibernate-mapping PUBLIC
        "-//Hibernate/Hibernate Mapping DTD//EN"
        "http://www.hibernate.org/dtd/hibernate-mapping-3.0.dtd">

<hibernate-mapping>
    <class name="com.example.Student" table="h_student">
        <meta attribute="class-description">
            This class contains the student detail.
        </meta>
        <id name="id">
            <generator class="native"/>
        </id>
        <property name="name"></property>
        <property name="sex"></property>
        <property name="address"></property>
        <property name="password"></property>
    </class>
</hibernate-mapping>
```

#### 5.5.配置 hibernate.cfg.xml

```xml
<?xml version='1.0' encoding='utf-8'?>
<!DOCTYPE hibernate-configuration PUBLIC
        "-//Hibernate/Hibernate Configuration DTD//EN"
        "http://www.hibernate.org/dtd/hibernate-configuration-3.0.dtd">
<hibernate-configuration>
    <session-factory>
        <property name="hibernate.dialect">
            org.hibernate.dialect.MariaDB10Dialect
        </property>
        <property name="hibernate.connection.driver_class">
            com.mysql.jdbc.Driver
        </property>

        <property name="hibernate.connection.url">
            jdbc:mysql:///hibernate?useUnicode=true&amp;characterEncoding=UTF-8
        </property>
        <property name="hibernate.connection.username">wyh</property>
        <property name="hibernate.connection.password">123456</property>

        <property name="hibernate.hbm2ddl.auto">update</property>

        <property name="hibernate.show_sql">true</property>
        <property name="hibernate.format_sql">true</property>
        <mapping resource="com/example/Student.hbm.xml"></mapping>
    </session-factory>
</hibernate-configuration>
```

#### 5.6.在数据库中创建一个数据库 hibernate

#### 5.7.写一个测试用例

```java
package com.test;

import com.example.Student;
import org.hibernate.*;
import org.hibernate.cfg.Configuration;

public class Test {

    public static void main(String[] args) {

        // 加载 Hibernate 核心配置文件
        Configuration configuration = new Configuration();
        configuration.configure();

        // 创建 SessionFactory 对象
        SessionFactory sessionFactory = configuration.buildSessionFactory();

        // 使用 SessionFactory 创建 Session 对象
        Session session = sessionFactory.openSession();

        // 开启事务
        Transaction transaction = session.beginTransaction();

        // 具体 crud 操作
        Student student = new Student();
        student.setName("张三三");
        student.setSex("男");
        student.setAddress("北京市朝阳区");
        student.setPassword("123456");

        // 提交事务
        session.save(student);
        transaction.commit();

        // 关闭资源
        session.close();
        sessionFactory.close();
    }
}

```

#### 5.8.执行结果

![h_student](https://up-img.yonghong.tech/pic/2021/07/29-17-09-h_student-tLuSPA.png)

![h_student_item](https://up-img.yonghong.tech/pic/2021/07/29-17-09-h_student_item-4L1LsN.png)

#### 5.9.下载示例

<a href="/assets/zip/Hibernate001.zip" download>下载 Hibernate 示例</a>

### 6.HibernateUtils 类

由于 SessionFactory 是在每次执行时都会检查是否已经建表，因此开销很大，解决办法是用一个 HibernateUtils 类，程序只需执行一次初始化即可。（初始化采用 static 代码块）

```java
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class HibernateUtils {

    private static final SessionFactory sessionFactory;

    static {
        try {
            // 加载 Hibernate 核心配置文件
            Configuration configuration = new Configuration();
            configuration.configure();
            sessionFactory = configuration.buildSessionFactory();
        } catch (Throwable ex) {
            throw new ExceptionInInitializerError(ex);
        }
    }

    public static SessionFactory getSessionFactory() {
        return sessionFactory;
    }
}
```

这样写好之后就只需要用 getSessionFactory() 方法就可以了。

```java
SessionFactory sessionFactory = HibernateUtils.getSessionFactory();
```


### 7.使用 Hibernate 的注解模式

新建一个 Teacher.java 类，Hibernate的注解是什么？ 简单的说，本来放在hbm.xml文件里的映射信息，现在不用配置文件做了，改由注解来完成。


```java
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "h_teacher")
public class Teacher {

    @Id
    private int id;
    private String name;
    private String sex;
    private String address;
    private String password;

    public Teacher() {}

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
```

这样写完之后还不能直接用，要在 Hibernate 配置文件(hibernate.cfg.xml) 中声明持久化类。

```xml
<mapping class="com.example.Teacher"></mapping>
```

测试结果与上述 Student 类似，不再展示。

### 8.在Intellij IDEA下通过 Hibernate 逆向生成实体类

参考 [在Intellij IDEA下通过Hibernate逆向生成实体类](https://www.cnblogs.com/morewindows0/p/8577351.html)

创建好数据库之后，打开 Persistence 视图，在  Hibernate 上右键，Generate Persistence Mapping -> By Database Schema 

![import-database-schema](https://up-img.yonghong.tech/pic/2021/07/29-17-09-import-database-schema-6atflh.png)

这样就自动生成了实体类。如图：

![SC](https://up-img.yonghong.tech/pic/2021/07/29-17-09-SC-P0o8Nv.png)


### 参考文献

[DAL、DAO、ORM、Active Record辨析](https://blog.csdn.net/suiye/article/details/7824943)

[理解java三层架构：持久层、业务层、表现层](https://blog.csdn.net/m0_38021128/article/details/69372109)

[百度百科-三层架构](https://baike.baidu.com/item/%E4%B8%89%E5%B1%82%E6%9E%B6%E6%9E%84)

[Java web 中的 三层架构](https://zhuanlan.zhihu.com/p/30832759)

[极客学院-hibernate 教程](http://wiki.jikexueyuan.com/project/hibernate/)

[Hibernate是什么？](https://www.cnblogs.com/talo/articles/1647830.html)

[Intellij IDEA下的第一个Hibernate项目](https://blog.csdn.net/qq_15096707/article/details/51419304)

[IDEA添加hibernate配置文件（包括cfg和hbm）](https://blog.csdn.net/sinat_18538231/article/details/77986020)

[Intellij IDEA创建第一个hibernate项目](https://blog.csdn.net/chensanwa/article/details/79103569)

[在Intellij IDEA下通过Hibernate逆向生成实体类](https://www.cnblogs.com/morewindows0/p/8577351.html)

[Hibernate注解-使用注解示例](https://blog.csdn.net/wo_shi_LTB/article/details/79157243)