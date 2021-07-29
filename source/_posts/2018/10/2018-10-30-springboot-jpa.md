---
layout: post
title:  "Spring Data JPA 全面解析"
category: "SpringBoot"
tags: ["Java", "SpringBoot", "spring-data-jpa"]
date: 2018-10-30 00:00:00
updated: 2018-10-30 00:00:00
---

### Spring Data JPA 是什么

JPA （The Java Persistence API）是用于访问，持久化和管理 Java 对象/类与关系型数据库之间的数据交互的 Java 规范。

> 注意，JPA 只是一个标准，只定义了一系列接口，而没有具体的实现。

<!-- more -->

很多企业级框架提供了对 JPA 的实现，如 Spring 。因此 Spring 本身与 JPA 无关，只是提供了对 JPA 的支持，因此在 Spring 中你也会看到很多注解都是属于 javax.persistence 包的。

JPA 的出现主要是为了简化现有的持久化开发工作和整合 ORM 技术，结束现在 Hibernate，TopLink，JDO 等 ORM 框架各自为营的局面。值得注意的是，JPA 是在充分吸收了现有 Hibernate，TopLink，JDO 等ORM框架的基础上发展而来的，具有易于使用，伸缩性强等优点。从目前的开发社区的反应上看，JPA 受到了极大的支持和赞扬，其中就包括了 Spring 与 EJB3.0 的开发团队。

Spring Data JPA 是 Spring 基于 ORM 框架、JPA 规范的基础上封装的一套 JPA 应用框架，底层使用了 Hibernate 的 JPA 技术实现，可使开发者用极简的代码即可实现对数据的访问和操作。它提供了包括增删改查等在内的常用功能，且易于扩展！学习并使用 Spring Data JPA 可以极大提高开发效率！

> spring data jpa 让我们解脱了 DAO 层的操作，基本上所有 CRUD 都可以依赖于它来实现

### 配置 Spring Data JPA

Maven - pom.xml

```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```

为什么这里不指定版本号呢？
- 因为 spring boot 的 pom 依赖了 parent，部分 jar 包的版本已在 parent 中指定，故不建议显示指定

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.0.6.RELEASE</version>
    <relativePath /> <!-- lookup parent from repository -->
</parent>
```

继续配置 application.yml

```yml
spring:
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    username: root
    password: 123456
    url: jdbc:mysql://localhost/sell?characterEncoding=utf-8&useSSL=false
  jpa:
    show-sql: true
```

或者是 application.properties

```
spring.datasource.url=jdbc:mysql://localhost/sell?characterEncoding=utf-8&useSSL=false
spring.datasource.username=root
spring.datasource.password=123456
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.jpa.show-sql=true
```

配置就这么简单，下面简单介绍下 spring.jpa.properties.hibernate.hbm2ddl.auto 有几种配置：

- create：每次加载Hibernate时都会删除上一次生成的表（包括数据），然后重新生成新表，即使两次没有任何修改也会这样执行。适用于每次执行单测前清空数据库的场景。
- create-drop：每次加载Hibernate时都会生成表，但当SessionFactory关闭时，所生成的表将自动删除。
- update：最常用的属性值，第一次加载Hibernate时创建数据表（前提是需要先有数据库），以后加载Hibernate时不会删除上一次生成的表，会根据实体更新，只新增字段，不会删除字段（即使实体中已经删除）。
- validate：每次加载Hibernate时都会验证数据表结构，只会和已经存在的数据表进行比较，根据model修改表结构，但不会创建新表。

不配置此项，表示禁用自动建表功能

### 开始写代码

实体类 ProductCategory.java

```java
package com.example.demo.dataobject;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

import lombok.Data;

/**
 * 用 @Entity 注解表示这是一个实体类，与数据库相对应
 * 数据库中的表格对应的是 user
 * 如果数据库中的表名和类名不对应，应该加上 @Table 注解
 * 例：@Table(name = "s_user")
 * 注解 @Data 是 Lombok 实现的一个简化的写法来代替 Getter 和 Setter 方法
 */
@Entity
@Data
public class User {

	/** id 注解 @Id 表示主键，注解 @GeneratedValue 表示自增类型 */
    @Id
    @GeneratedValue
    private long id;
    @Column(nullable = false, unique = true)
    private String userName;
    @Column(nullable = false)
    private String password;
    @Column(nullable = false)
    private int age;
}
```

> 注：Entity中不映射成列的字段得加@Transient 注解，不加注解也会映射成列


声明 UserRepository接口，继承JpaRepository，默认支持简单的 CRUD 操作，非常方便


```java
import com.example.demo.dataobject.User;

import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
    User findByUserName(String userName);
}
```

测试代码 

```java
/** 
 * 注解 @Slf4j 也是 Lombok 提供的简单写法来代替 Logger 的复杂写法
 */
@Slf4j
public class UserTest extends ApplicationTests {

    @Autowired
    private UserRepository userRepository;

    @Test
    @Transactional
    public void userTest() {
        User user = new User();
        user.setUserName("0xl2oot");
        user.setAge(30);
        user.setPassword("aaabbb");
        userRepository.save(user);
        User item = userRepository.findByUserName("0xl2oot");
        log.info(JsonUtils.toJson(item));
    }
}
```

测试运行，成功

注：[加 @Transactional 注解的原因](https://notes.0xl2oot.cn/springboot/2018/10/30/could-not-initialize-proxy-no-session.html)

### 原理

很多人会有疑问，直接声明接口不需要具体实现就能完成数据库的操作？下面就简单介绍下 spring data jpa 的实现原理。

对单测进行debug，可以发现userRepository被注入了一个动态代理，被代理的类是JpaRepository的一个实现SimpleJpaRespositry

继续往下debug,在进到findByUserName方法的时候，发现被上文提到的JdkDynamicAopProxy捕获，然后经过一系列的方法拦截，最终进到QueryExecutorMethodInterceptor.doInvoke中。这个拦截器主要做的事情就是判断方法类型，然后执行对应的操作.
我们的findByUserName属于自定义查询，于是就进入了查询策略对应的execute方法。在执行execute时，会先选取对应的JpaQueryExecution，调用AbtractJpaQuery.getExecution()

```java
protected JpaQueryExecution getExecution() {
  if (method.isStreamQuery()) {
    return new StreamExecution();
  } else if (method.isProcedureQuery()) {
    return new ProcedureExecution();
  } else if (method.isCollectionQuery()) {
    return new CollectionExecution();
  } else if (method.isSliceQuery()) {
    return new SlicedExecution(method.getParameters());
  } else if (method.isPageQuery()) {
    return new PagedExecution(method.getParameters());
  } else if (method.isModifyingQuery()) {
    return method.getClearAutomatically() ? new ModifyingExecution(method, em) : new ModifyingExecution(method, null);
  } else {
    return new SingleEntityExecution();
  }
}
```

如上述代码所示，根据method变量实例化时的查询设置方式，实例化不同的JpaQueryExecution子类实例去运行。我们的findByUserName最终落入了SingleEntityExecution —— 返回单个实例的 Execution。继续跟踪execute方法，发现底层使用了 hibernate 的 CriteriaQueryImpl 完成了sql的拼装，这里就不做赘述了。

再来看看这类的method。在 spring-data-jpa 中，JpaQueryMethod就是Repository接口中带有@Query注解方法的全部信息，包括注解，类名，实参等的存储类，所以Repository接口有多少个@Query注解方法，就会包含多少个JpaQueryMethod实例被加入监听序列。实际运行时，一个RepositoryQuery实例持有一个JpaQueryMethod实例，JpaQueryMethod又持有一个Method实例。

再来看看RepositoryQuery，在QueryExecutorMethodInterceptor中维护了一个Map<Method, RepositoryQuery> queries。RepositoryQuery的直接抽象子类是AbstractJpaQuery，可以看到，一个RepositoryQuery实例持有一个JpaQueryMethod实例，JpaQueryMethod又持有一个Method实例，所以RepositoryQuery实例的用途很明显，一个RepositoryQuery代表了Repository接口中的一个方法，根据方法头上注解不同的形态，将每个Repository接口中的方法分别映射成相对应的RepositoryQuery实例。

下面我们就来看看spring-data-jpa对RepositoryQuery实例的具体分类： 

1.SimpleJpaQuery 
方法头上@Query注解的nativeQuery属性缺省值为false，也就是使用JPQL，此时会创建SimpleJpaQuery实例，并通过两个StringQuery类实例分别持有query jpql语句和根据query jpql计算拼接出来的countQuery jpql语句；

2.NativeJpaQuery 
方法头上@Query注解的nativeQuery属性如果显式的设置为nativeQuery=true，也就是使用原生SQL，此时就会创建NativeJpaQuery实例；

3.PartTreeJpaQuery 
方法头上未进行@Query注解，将使用spring-data-jpa独创的方法名识别的方式进行sql语句拼接，此时在spring-data-jpa内部就会创建一个PartTreeJpaQuery实例；

4.NamedQuery 
使用javax.persistence.NamedQuery注解访问数据库的形式，此时在spring-data-jpa内部就会根据此注解选择创建一个NamedQuery实例；

5.StoredProcedureJpaQuery 
顾名思义，在Repository接口的方法头上使用org.springframework.data.jpa.repository.query.Procedure注解，也就是调用存储过程的方式访问数据库，此时在spring-data-jpa内部就会根据@Procedure注解而选择创建一个StoredProcedureJpaQuery实例。

那么问题来了，sql 拼接的时候怎么知道是根据userName进行查询呢？是取自方法名中的 byUsername 还是方法参数 userName 呢？ spring 具体是在什么时候知道查询参数的呢 ？

### 数据如何注入

spring 在启动的时候会实例化一个 Repositories，它会去扫描所有的 class，然后找出由我们定义的、继承自org.springframework.data.repository.Repositor的接口，然后遍历这些接口，针对每个接口依次创建如下几个实例:

1. SimpleJpaRespositry —— 用来进行默认的 DAO 操作，是所有 Repository 的默认实现
2. JpaRepositoryFactoryBean —— 装配 bean，装载了动态代理 Proxy，会以对应的 DAO 的 beanName 为 key 注册到DefaultListableBeanFactory中，在需要被注入的时候从这个 bean 中取出对应的动态代理 Proxy 注入给 DAO
3. JdkDynamicAopProxy —— 动态代理对应的InvocationHandler，负责拦截 DAO 接口的所有的方法调用，然后做相应处理，比如findByUsername被调用的时候会先经过这个类的 invoke 方法

在JpaRepositoryFactoryBean.getRepository()方法被调用的过程中，还是在实例化QueryExecutorMethodInterceptor这个拦截器的时候，spring 会去为我们的方法创建一个PartTreeJpaQuery，在它的构造方法中同时会实例化一个PartTree对象。PartTree定义了一系列的正则表达式，全部用于截取方法名，通过方法名来分解查询的条件，排序方式，查询结果等等，这个分解的步骤是在进程启动时加载 Bean 的过程中进行的，当执行查询的时候直接取方法对应的PartTree用来进行 sql 的拼装，然后进行 DB 的查询，返回结果。

到此为止，我们整个JpaRepository接口相关的链路就算走通啦，简单的总结如下：
spring 会在启动的时候扫描所有继承自 Repository 接口的 DAO 接口，然后为其实例化一个动态代理，同时根据它的方法名、参数等为其装配一系列DB操作组件，在需要注入的时候为对应的接口注入这个动态代理，在 DAO 方法被调用的时会走这个动态代理，然后经过一系列的方法拦截路由到最终的 DB 操作执行器 JpaQueryExecution，然后拼装 sql，执行相关操作，返回结果。

### 基本查询

基本查询分为两种，一种是 spring data 默认已经实现（只要继承`JpaRepository`），一种是根据查询的方法来自动解析成 SQL。

####  预先生成

```
public interface UserRepository extends JpaRepository<User, Long> {
}

@Test
public void testBaseQuery() throws Exception {
    User user=new User();
    userRepository.findAll();
    userRepository.findOne(1l);
    userRepository.save(user);
    userRepository.delete(user);
    userRepository.count();
    userRepository.exists(1l);
    // ...
}
```

####  自定义简单查询

自定义的简单查询就是根据方法名来自动生成SQL，主要的语法是`findXXBy,readAXXBy,queryXXBy,countXXBy, getXXBy`后面跟属性名称，举几个例子：

```
User findByUserName(String userName);

User findByUserNameOrEmail(String username, String email);

Long deleteById(Long id);

Long countByUserName(String userName);

List<User> findByEmailLike(String email);

User findByUserNameIgnoreCase(String userName);

List<User> findByUserNameOrderByEmailDesc(String email);
```

具体的关键字，使用方法和生产成 SQL 如下表所示

| Keyword           | Sample                                    | JPQL snippet                                                 |
| ----------------- | ----------------------------------------- | ------------------------------------------------------------ |
| And               | findByLastnameAndFirstname                | … where x.lastname = ?1 and x.firstname = ?2                 |
| Or                | findByLastnameOrFirstname                 | … where x.lastname = ?1 or x.firstname = ?2                  |
| Is,Equals         | findByFirstnameIs,findByFirstnameEquals   | … where x.firstname = ?1                                     |
| Between           | findByStartDateBetween                    | … where x.startDate between ?1 and ?2                        |
| LessThan          | findByAgeLessThan                         | … where x.age < ?1                                           |
| LessThanEqual     | findByAgeLessThanEqual                    | … where x.age ⇐ ?1                                           |
| GreaterThan       | findByAgeGreaterThan                      | … where x.age > ?1                                           |
| GreaterThanEqual  | findByAgeGreaterThanEqual                 | … where x.age >= ?1                                          |
| After             | findByStartDateAfter                      | … where x.startDate > ?1                                     |
| Before            | findByStartDateBefore                     | … where x.startDate < ?1                                     |
| IsNull            | findByAgeIsNull                           | … where x.age is null                                        |
| IsNotNull,NotNull | findByAge(Is)NotNull                      | … where x.age not null                                       |
| Like              | findByFirstnameLike                       | … where x.firstname like ?1                                  |
| NotLike           | findByFirstnameNotLike                    | … where x.firstname not like ?1                              |
| StartingWith      | findByFirstnameStartingWith               | … where x.firstname like ?1 (parameter bound with appended %) |
| EndingWith        | findByFirstnameEndingWith                 | … where x.firstname like ?1 (parameter bound with prepended %) |
| Containing        | findByFirstnameContaining                 | … where x.firstname like ?1 (parameter bound wrapped in %)   |
| OrderBy           | findByAgeOrderByLastnameDesc              | … where x.age = ?1 order by x.lastname desc                  |
| Not               | findByLastnameNot                         | … where x.lastname <> ?1                                     |
| In                | findByAgeIn(Collection<age> ages)</age>   | … where x.age in ?1                                          |
| NotIn             | findByAgeNotIn(Collection<age> age)</age> | … where x.age not in ?1                                      |
| TRUE              | findByActiveTrue()                        | … where x.active = true                                      |
| FALSE             | findByActiveFalse()                       | … where x.active = false                                     |
| IgnoreCase        | findByFirstnameIgnoreCase                 | … where UPPER(x.firstame) = UPPER(?1)                        |

###  复杂查询

在实际的开发中我们需要用到分页、删选、连表等查询的时候就需要特殊的方法或者自定义 SQL

####  分页查询

分页查询在实际使用中非常普遍了，spring data jpa已经帮我们实现了分页的功能，在查询的方法中，需要传入参数`Pageable`
，当查询中有多个参数的时候`Pageable`建议做为最后一个参数传入。`Pageable`是 spring 封装的分页实现类，使用的时候需要传入页数、每页条数和排序规则

```
Page<User> findALL(Pageable pageable);

Page<User> findByUserName(String userName,Pageable pageable);
@Test
public void testPageQuery() throws Exception {
    int page=1,size=10;
    Sort sort = new Sort(Direction.DESC, "id");
    Pageable pageable = new PageRequest(page, size, sort);
    userRepository.findALL(pageable);
    userRepository.findByUserName("testName", pageable);
}
```

有时候我们只需要查询前N个元素，或者支取前一个实体。

```
User findFirstByOrderByLastnameAsc();

User findTopByOrderByAgeDesc();

Page<User> queryFirst10ByLastname(String lastname, Pageable pageable);

List<User> findFirst10ByLastname(String lastname, Sort sort);

List<User> findTop10ByLastname(String lastname, Pageable pageable);
```

####  自定义SQL查询

其实 Spring data 大部分的 SQL 都可以根据方法名定义的方式来实现，但是由于某些原因我们想使用自定义的 SQL 来查询，spring data 也是完美支持的；在 SQL 的查询方法上面使用 @Query 注解，如涉及到删除和修改在需要加上 @Modifying 。也可以根据需要添加 @Transactional 对事物的支持，查询超时的设置等

```
@Modifying
@Query("update User u set u.userName = ?1 where c.id = ?2")
int modifyByIdAndUserId(String  userName, Long id);

@Transactional
@Modifying
@Query("delete from User where id = ?1")
void deleteByUserId(Long id);

@Transactional(timeout = 10)
@Query("select u from User u where u.emailAddress = ?1")
User findByEmailAddress(String emailAddress);
```

####  多表查询

多表查询在 spring data jpa 中有两种实现方式，第一种是利用 hibernate 的级联查询来实现，第二种是创建一个结果集的接口来接收连表查询后的结果，这里介绍第二种方式。

首先需要定义一个结果集的接口类。

```
public interface HotelSummary {

    City getCity();

    String getName();

    Double getAverageRating();

    default Integer getAverageRatingRounded() {
        return getAverageRating() == null ? null : (int) Math.round(getAverageRating());
    }

}
```

查询的方法返回类型设置为新创建的接口

```
@Query("select h.city as city, h.name as name, avg(r.rating) as averageRating from Hotel h left outer join h.reviews r where h.city = ?1 group by h")
Page<HotelSummary> findByCity(City city, Pageable pageable);

@Query("select h.name as name, avg(r.rating) as averageRating from Hotel h left outer join h.reviews r group by h")
Page<HotelSummary> findByCity(Pageable pageable);
Page<HotelSummary> hotels = this.hotelRepository.findByCity(new PageRequest(0, 10, Direction.ASC, "name"));
for(HotelSummary summay:hotels){
    System.out.println("Name" +summay.getName());
}
```

在运行中 Spring 会给接口（`HotelSummary`）自动生产一个代理类来接收返回的结果，代码会使用 getXX 的形式来获取

### 和 mybatis 的比较

spring data jpa 底层采用 hibernate 做为 ORM 框架，所以 spring data jpa 和 mybatis 的比较其实就是 hibernate 和 mybatis 的比较。下面从几个方面来对比下两者

#### 基本概念

从基本概念和框架目标上看，两个框架差别还是很大的。hibernate 是一个自动化更强、更高级的框架，毕竟在java代码层面上，省去了绝大部分 sql 编写，取而代之的是用面向对象的方式操作关系型数据库的数据。而 MyBatis 则是一个能够灵活编写 sql 语句，并将 sql 的入参和查询结果映射成 POJOs 的一个持久层框架。所以，从表面上看，hibernate 能方便、自动化更强，而 MyBatis 在 Sql 语句编写方面则更灵活自由。

#### 性能

正如上面介绍的， Hibernate 比 MyBatis 抽象封装的程度更高，理论上单个语句之心的性能会低一点（所有的框架都是一样，排除算法上的差异，越是底层，执行效率越高）。

但 Hibernate 会设置缓存，对于重复查询有一定的优化，而且从编码效率来说，Hibernate 的编码效果肯定是会高一点的。所以，从整体的角度来看性能的话，其实两者不能完全说谁胜谁劣。

####  ORM

Hibernate 是完备的 ORM 框架，是符合 JPA 规范的， MyBatis 没有按照JPA那套规范实现。目前 Spring 以及 Spring Boot 官方都没有针对 MyBatis 有具体的支持，但对 Hibernate 的集成一直是有的。但这并不是说 mybatis 和 spring 无法集成，MyBatis 官方社区自身也是有 对 Spring，Spring boot 集成做支持的，所以在技术上，两者都不存在问题。

#### 总结

总结下 mybatis 的优点：

- 简单易学
- 灵活，MyBatis不会对应用程序或者数据库的现有设计强加任何影响。 注解或者使用 SQL 写在 XML 里，便于统一管理和优化。通过 SQL 基本上可以实现我们不使用数据访问框架可以实现的所有功能，或许更多。
- 解除 SQL 与程序代码的耦合，SQL 和代码的分离，提高了可维护性。
- 提供映射标签，支持对象与数据库的 ORM 字段关系映射。
- 提供对象关系映射标签，支持对象关系组建维护。
- 提供XML标签，支持编写动态SQL。

hibernate 的优点：
JPA 的宗旨是为 POJO 提供持久化标准规范，实现使用的 Hibernate，Hibernate 是一个全自动的持久层框架，并且提供了面向对象的 SQL 支持，不需要编写复杂的 SQL 语句，直接操作 Java 对象即可，从而大大降低了代码量，让即使不懂 SQL 的开发人员，也使程序员更加专注于业务逻辑的实现。对于关联查询，也仅仅是使用一些注解即可完成一些复杂的 SQL功能。

### 参考文献
- [org.springframework.data.jpa.repository](https://docs.spring.io/spring-data/jpa/docs/2.1.2.RELEASE/api/org/springframework/data/jpa/repository/JpaRepository.html)
- [【spring boot 系列】spring data jpa 全面解析（实践 + 源码分析）](https://segmentfault.com/a/1190000015047290)