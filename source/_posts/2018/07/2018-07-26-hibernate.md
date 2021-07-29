---
layout: post
title: Hibernate 原理及实战（二）
categories: [Hibernate]
tags: [Hibernate, Java]
date: 2018-07-26 00:00:00
updated: 2018-07-26 00:00:00
---

### 1.实体类的编写规则

推荐使用包装类

1 实体类（称为 持久化类）

有类和数据库表进行对应关系，不需要直接操作数据库表，操作实体类对象就可以了，这个类称为实体类

<!-- more -->

2 实体类编写规则  
（1）实体类属性私有的  
（2）私有属性有公开的get和set方法  
（3）有公开无参构造方法  
（4）要求实体类里面有一个属性和表里面主键对应  
（5）建议：不要使用final修饰  
（6）建议：要使用基本数据类型对应包装类  

3 为什么使用包装类

（1）使用包装类之后更准确表示数据

（2）

| 基本数据类型 | 对应包装类 |
| ------------ | ---------- |
| int          | Integer    |
| char         | Character  |
| boolean      | Boolean    |
| float        | Float      |
| double       | Double     |
| short        | Short      |
| long         | Long       |
| byte         | Byte       |

 

（3）举例说明
* 比如表示学生分数 int score = 5;  表示学生得了0分int score = 0;
** 表示学生没有参加考试int score = -1;
* 使用包装类 Integer score = 5;   学生得了0分Integer score = 0;
** 表示学生没有参加考试Integer score = null;

### 2.主键生成策略


1、Hibernate要求在一个实体中必须要有一个属性作为唯一值，这个唯一值一般都对应表中的主键。

2、主键分类

自然主键:把具有业务含义的字段作为主键，称之为自然主键。

代理主键:把不具有业务含义的字段作为主键，称之为代理主键。

3、主键的常见生成策略有七种
　　　　
　　

|名称 | 描述 |
| -- | -- |
|increment | 用于long、short或int类型的，由Hibernate自动由递增的方式生成唯一标识符，每次增长1.只有当没有其他线程向同一张表中插入数据时使用。不能在集群情况下使用，适用于代理主键。 |
|identity | 采用底层数据库提供的本身提供的主键生成标识符，前提是数据库必须支持自增长的数据类型。在DB2、mysql、MS SQL SERVER、Sybase和HypersonicSQL数据库中可以使用该策略，该策略要求在数据库中把主键定义为自增长，适用于代理主键。|
|sequence |Hibernate根据底层数据库序列生成标识符。条件是数据库要支持序列，Oracle数据库可以使用该策略适用于代理主键。|
|hilo | 通过hi/lo 算法实现的主键生成机制，需要额外的数据库表保存主键生成历史状态。|
|native |根据底层数据库对自动生成表示符的能力来自动选择identity、sequence和hilo三种生成器中的一种。适合跨数据库平台开发，适用于代理主键。 |
|uuid |Hibernate采用128位的UUID来生成字符，使用16进制表示，使用该策略时主键必须定义为String类型，由于其所占的空间较多，使用较少，适用于代理主键。|
|assigned |由Java程序负责生成标识符，如果在配置文件中不配置<generator></generator>标签，则默认为该策略，适用于自然主键。|


1 在映射配置文件中，配置实体类唯一属性值和表主键对应，class属性中有值，这个值表示生成策略，使用 native

2 使用最多的native，

（1）根据使用的数据库类型，自动选择使用的值

（2）实体类属性类型int类型（包装类）

3 经常使用值 uuid

如果使用uuid值时候，实体类属性类型不能是int类型，是String类型


### 3..对实体类的 CRUD 操作

#### 3.1.添加操作

前面写过了，不再重复

```java
Teacher teacher = new Teacher();
teacher.setName("赵三三");
teacher.setSex("女");
teacher.setAddress("北京市海淀区");
teacher.setPassword("654321");
```

#### 3.2.根据 id 进行查询

```java
public void testGet() {
    // 1.调用工具类得到 sessionFactory
    SessionFactory sessionFactory = HibernateUtils.getSessionFactory();
    // 2.获取 Session
    Session session = sessionFactory.openSession();
    // 3.开启事务
    Transaction transaction = session.beginTransaction();

    // 4.根据 id 查询
    // 调用 session 里面的 get
    // 第一个参数：实体类的 class
    // 第二个参数：id 值
    Student student = session.get(Student.class, 1);
    System.out.println(student);

    // 5.提交事务
    transaction.commit();
    // 6.关闭资源
    session.close();
}
```

#### 3.3.修改操作

```java
public void testUpdate() {
    // 1.调用工具类得到 sessionFactory
    SessionFactory sessionFactory = HibernateUtils.getSessionFactory();
    // 2.获取 Session
    Session session = sessionFactory.openSession();
    // 3.开启事务
    Transaction transaction = session.beginTransaction();

    // 4.修改操作
    // 修改 id = 1 记录的 name 的值
    // 先查
    Student student = session.get(Student.class, 1);
    System.out.println(student);
    // 再改
    student.setName("哈哈");
    // 调用 session 里的 update 方法修改(save 也可以)
    session.update(student);

    // 5.提交事务
    transaction.commit();
    // 6.关闭资源
    session.close();
}
```

#### 3.4.删除操作


```java
public void testDelete() {
    // 1.调用工具类得到 sessionFactory
    SessionFactory sessionFactory = HibernateUtils.getSessionFactory();
    // 2.获取 Session
    Session session = sessionFactory.openSession();
    // 3.开启事务
    Transaction transaction = session.beginTransaction();

    // 4.删除操作
    // 第一种方式，根据 ID 查询出对象(建议)
//        Student student = session.get(Student.class, 4);
//        session.delete(student);
    // 第二种方法
    Student student = new Student();
    student.setId(4);
    session.delete(student);

    // 5.提交事务
    transaction.commit();
    // 6.关闭资源
    session.close();
}
```

### 4.实体类对象状态介绍（了解）


1 实体类对象有三种状态

（0）区分状态的方式  
实体类对象里面是否id值  
实体类对象是否与session有关联  

（1）瞬时态：没有id值，与session没有关系

```java
Teacher teacher = new Teacher();
teacher.setName("赵三三");
teacher.setSex("女");
teacher.setAddress("北京市海淀区");
teacher.setPassword("654321");
```

（2）持久态：有id值，与session有关系

```java
Student student = session.get(Student.class, 4);
```

（3）托管态：有id值，与session没有关系

```java
Student student = new Student();
student.setId(4);
```

2 状态直接的转换  

（1）瞬时态 转换 持久态 ： 调用save方法实现  
（2）托管态 转换 持久态 ： 调用update方法实现  

3 saveOrUpdate() 方法

```java
// 瞬时态，添加操作
Student student = new Student();
student.setName("Jack");
student.setSex("男");
student.setAddress("河北唐山");
student.setPassword("hhhhhhh");

session.saveOrUpdate(student);
```

```java
// 实体类对象是托管态，做修改
Student student = new Student();
student.setId(5);
student.setName("Marry");
student.setSex("女");
student.setAddress("爱尔兰");
student.setPassword("gggg");

session.saveOrUpdate(student);
```

```java
// 持久态，执行更新操作
Student student = session.get(Student.class, 5);
student.setName("李雷");

session.saveOrUpdate(student);
```

### 5.Hibernate 的一级缓存

#### 5.1.Hibernate提供两种缓存

第一种 一级缓存

（1）一级缓存特点：
- 特点1： 一级缓存在hibernate操作中默认打开的，直接使用
- 特点2： 一级缓存使用范围，是session范围，在session创建和session关闭的范围中使用一级缓存，session关闭一级缓存没有了
- 特点3： 一级**缓存中缓存持久态数据**

第二种 二级缓存（不用，替代技术 redis）
- 不是默认开启，需要配置
- 使用范围，SessionFactory

#### 5.2.验证一级缓存的存在

1.验证方式
(1)根据 id = 1 查询，返回对象
(2)再次根据 id = 1 查询，返回对象（不会查询数据库）

#### 5.3.一级缓存的执行过程


![cache](https://up-img.yonghong.tech/pic/2021/07/29-17-11-cache-m9VJIj.png)


#### 5.4.特性(持久态自动更新数据库)

不执行 session.update(user) 也可以更新。

![auto-update](https://up-img.yonghong.tech/pic/2021/07/29-17-10-auto-update-BufMmO.png)


### 6.事务代码规范写法

#### 6.1.事务相关概念

事务特性

原子性，一致性，隔离性，持久性

脏读
不可重复读
虚读

设置事务隔离级别

MySQL 默认的隔离级别 repeatable read

Hibernate 事务隔离级别

```xml
<property name="hibernate.connection.isolation">4</property>
```


#### 6.2.Hibernate 事务代码规范写法


```java
try {
    // 开启事务
    // 提交事务
} catch () {
    // 回滚事务
} finally {
    // 关闭操作
}
```

```java
public void testTx() {
    SessionFactory sessionFactory = null;
    Session session = null;
    Transaction transaction = null;
    try {
        // 开启事务
        // 1.调用工具类得到 sessionFactory
        sessionFactory = HibernateUtils.getSessionFactory();
        // 2.获取 Session
        session = sessionFactory.openSession();
        // 3.开启事务
        transaction = session.beginTransaction();

        // 实体类对象是托管态，做修改
        Student student = new Student();
        student.setId(5);
        student.setName("Marry");
        student.setSex("女");
        student.setAddress("爱尔兰");
        student.setPassword("gggg");

        session.saveOrUpdate(student);

        // 提交事务
        transaction.commit();

    } catch (Exception e) {
        e.printStackTrace();
        // 回滚事务
        transaction.rollback();
    } finally {
        // 关闭操作
        session.close();
    }
}
```

#### 6.3.Hibernate 绑定session

（1）在hibernate核心配置文件中，配置打开与本地线程绑定的session

```xml
<property name="hibernate.current_session_context_class">thread</property>
```


（2）调用sessionFactory里面的方法得到与本地线程绑定的session

```java
public static Session getSessionObject() {
    return sessionFactory.getCurrentSession();
}
```

```java
Session session = getSessionObject();
```

（3）不需要手动关闭 session

### 7.Hibernate API 的使用

#### 7.1.Query 对象

1 写 HQL 语句：Hibernate Query Language，hibernate提供查询语言，和普通sql很相似

- （1）区别： 
    - 使用普通sql操作表和字段。
    - 使用hql **操作实体类和属性**
- （2）查询所有语句： from 实体类名称


```java
// 使用 Query 对象
@Test
public void testTx() {
    SessionFactory sessionFactory = null;
    Session session = null;
    Transaction transaction = null;
    try {
        // 开启事务
        // 1.调用工具类得到 sessionFactory
        sessionFactory = HibernateUtils.getSessionFactory();
        // 2.获取 Session
        session = sessionFactory.openSession();
        // 3.开启事务
        transaction = session.beginTransaction();

        // 创建一个 Query 对象
        // 方法里面写 HQL 语句
        Query query = session.createQuery("from Student");
        // 调用 Query 对象里面的方法得到结果
        List<Student> list = query.list();

        for(Student student : list) {
            System.out.println(student);
        }

        // 提交事务
        transaction.commit();

    } catch (Exception e) {
        e.printStackTrace();
        // 回滚事务
        transaction.rollback();
    } finally {
        // 关闭操作
        session.close();
        sessionFactory.close();
    }
}
```


#### 7.2.Criteria 对象

1 使用这种方式，不需要写任何语句，都是调用方法实现

2 具体实现
- 第一步 创建critica对象
- 第二步 调用critica对象里面的方法得到结果

```java
// 创建 criteria 对象
Criteria criteria = session.createCriteria(Student.class);
List<Student> list = criteria.list();
for(Student student : list) {
    System.out.println(student);
}
```


#### 7.3.SQLquery 对象

1 这种方式可以使用普通sql实现

2 实现步骤
- 第一步 创建对象
- 第二步 调用方法得到结果

返回 list 集合每部分是数组形式

```java
SQLQuery sqlQuery = session.createSQLQuery("select * from h_student");
List<Object[]> list = sqlQuery.list();
for(Object[] objects : list) {
    System.out.println(Arrays.toString(objects));
}
```

返回 list 集合每部分是对象形式

```java
SQLQuery sqlQuery = session.createSQLQuery("select * from h_student");
sqlQuery.addEntity(Student.class);
List<Student> list = sqlQuery.list();
for(Student student : list) {
    System.out.println(student);
}
```

### 参考文献


[Hibernate实体类编写规则和主键策略](http://www.cnblogs.com/jack1995/p/6937235.html)

[Hibernate【缓存】知识要点](https://juejin.im/post/5aa148126fb9a028d4442a46)

[缓存-极客学院](http://wiki.jikexueyuan.com/project/hibernate/caching.html)

[Hibernate：缓存机制的学习](http://tracylihui.github.io/2015/07/20/Hibernate%EF%BC%9A%E7%BC%93%E5%AD%98%E6%9C%BA%E5%88%B6%E7%9A%84%E5%AD%A6%E4%B9%A0/)