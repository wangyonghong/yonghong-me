---
layout: post
title: Hibernate 原理及实战（四）
categories: [Hibernate]
tags: [Hibernate, Java]
date: 2018-07-30 00:00:00
updated: 2018-07-30 00:00:00
---

### 1.对象导航查询

- 根据 id 查询某个客户，再查询这个客户里面所有的联系人

<!-- more -->

### 2.OID 查询

- 根据 ID 查询某一条记录，返回对象

### 3.hql查询

HQL是Hiberante官方推荐的Hibernate检索方式，它使用类似SQL的查询语言，以面向对象的方式从数据库中查询。可以使用HQL查询具有继承、多态和关联关系的数据。在检索数据时应优先考虑使用HQL方式。

#### 3.0.方法

（1）创建 Query 对象，写HQL语句实现查询
（2）调用 Query 对象里面的方法得到结果

#### 3.1.查询所有

查询所有的客户的记录

```java
// 创建 Query 对象
Query query = session.createQuery("from Customer");
// 调用方法得到结果
List<Customer> list = query.list();
```

#### 3.2.条件查询

```java
Query query = session.createQuery("from Customer cid = ? AND customerName = ?");

query.setParameter(0,1);
query.setParameter(1,"百度");

List<Customer> list = query.list();
```

#### 3.3.排序查询

```java
Query query = session.createQuery("from Customer order by cid asc"); 
// asc 升序 desc 降序
List<Customer> list = query.list();
```

#### 3.4.分页查询


```java
// 分页
Query query = session.createQuery("from Customer");

query.setFirstResult(0);
query.setMaxResults(3);

List<Customer> list = query.list();
```

#### 3.5.投影查询

```java
Query query = session.createQuery("select customerName from Customer");
List<Object> list = query.list();
```

#### 3.6.聚合查询

count sum avg max min

```java
Query query = session.createQuery("select count(*) from Customer");
Object obj = query.uniqueResult();
Long lobj = (Long) obj;
int count = lobj.intValue();
```

### 4.QBC查询

（1）使用 HQL 查询的时候需要写 HQL 语句，使用 QBC 的时候用方法来实现。
（2）使用 QBC 的时候，操作实体类和属性。
（3）调用 Criteria 对象里面的方法得到结果

#### 4.1.查询所有

```java
// 创建 criteria 对象
Criteria criteria = session.createCriteria(Customer.class);
List<Customer> list = criteria.list();
for(Customer customer : list) {
    System.out.println(customer.getCid() + customer.getCustomerName());
}
```

#### 4.2.条件查询

使用封装的方法

```java
Criteria criteria = session.createCriteria(Customer.class);
criteria.add(Restrictions.eq("cid", 1));
criteria.add(Restrictions.eq("customerName", "百度"));
// criteria.add(Restrictions.like("customerName", "%百%"));
List<Customer> list = criteria.list();
```

#### 4.3.排序查询


```java
Criteria criteria = session.createCriteria(Customer.class);
criteria.add(Order.desc("cid"));
List<Customer> list = criteria.list();
```

#### 4.4.分页查询


```java
Criteria criteria = session.createCriteria(Customer.class);
criteria.setFirstResult(0);
criteria.setMaxResults(3);
List<Customer> list = criteria.list();
```

#### 4.5.统计查询


```java
Criteria criteria = session.createCriteria(Customer.class);
criteria.setProject(Projections.rowCount());
Object obj = criteria.uniqueResult();
Long lobj = (Long) obj;
int count = lobj.intValue();
```


#### 4.6.离线查询

离线场景：在 servlet 中拼接查询条件，传到 dao 中

```java
// 创建对象
DetachedCriteria detachedCriteria = DetachedCriteria.forClass(Customer.class);

// 最终执行的时候再需要用到 session
Criteria criteria = detachedCriteria.getExecutableCriteria(session);

List<Customer> list = criteria.list();
```

### 5.HQL 多表查询

#### 5.1.内连接

返回的是数组

from Customer c inner join c.linkManSet

```java
Query query = session.createQuery("from Customer c inner join c.linkManSet");
List<Object> list = query.list();
```

#### 5.2.左外连接

from Customer c left outer join c.linkManSet

```java
Query query = session.createQuery("from Customer c left outer join c.linkManSet");
List<Object> list = query.list();
```

#### 5.3.右外连接

from Customer c right outer join c.linkManSet

```java
Query query = session.createQuery("from Customer c right outer join c.linkManSet ");
List<Object> list = query.list();
```

#### 5.4.迫切内连接

返回的是对象

from Customer c inner join fetch c.linkManSet

```java
Query query = session.createQuery("from Customer c inner join fetch c.linkManSet");
List<Object> list = query.list();
```

#### 5.5.迫切左外连接

返回的是对象

from Customer c left outer join fetch c.linkManSet

```java
Query query = session.createQuery("from Customer c left outer join fetch c.linkManSet");
List<Object> list = query.list();
```


### 6.Hibernate 检索策略

1.Hibernate 检索策略分为两类
- （1）立即查询，根据 id 进行查询，调用 get 方法，一调用 get 方法马上发送语句查询数据库
- （2）延迟查询，根据 id 进行查询，调用 load 方法，调用 load 方法不会马上发送语句查询数据，只有得到对象里面的值的时候才会发出语句查询数据库。

2.延迟查询分为两类
- （1）类级别延迟，根据 id 查询返回实体类对象，调用 load 方法不会马上发送语句
- （2）关联级别延迟
    - 查询某个客户，再根据客户查询这个客户所有联系人，查询客户所有联系人的过程是否需要延迟，这个过程称为关联级别的延迟