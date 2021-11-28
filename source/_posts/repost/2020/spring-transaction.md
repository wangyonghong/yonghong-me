---
title: Spring事务的传播特性
tags:
- Spring
categories:
- 转载
date: 2020-06-10 22:24:00
updated: 2020-06-10 22:24:00
---

> 原文链接：[Spring事务的传播特性](https://github.com/love-somnus/Spring/wiki/Spring事务的传播特性)

Spring 事务一个被讹传很广说法是：一个事务方法不应该调用另一个事务方法，否则将产生两个事务。结果造成开发人员在设计事务方法时束手束脚，生怕一不小心就踩到地雷。

其实这种是不认识 Spring 事务传播机制而造成的误解，Spring 对事务控制的支持统一在 `TransactionDefinition` 接口中描述，该接口有以下几个重要的接口方法：

![img](https://up-img.yonghong.tech/pic/2020/06/10-11-19-20181230001-dfRHHu.png)

<!--more-->

很明显，除了事务的传播行为外，事务的其它特性 Spring 是借助底层资源的功能来完成的，Spring 无非只充当个代理的角色。但是事务的传播行为却是 Spring 凭借自身的框架提供的功能，是 Spring 提供给开发者最珍贵的礼物，讹传的说法玷污了 Spring 事务框架最美丽的光环。

所谓事务传播行为就是多个事务方法相互调用时，事务如何在这些方法间传播。Spring 支持 7 种事务传播行为（Transaction Propagation Behavior）：

| 传播行为                      | 描述                                                         |
| ----------------------------- | ------------------------------------------------------------ |
| **PROPAGATION_REQUIRED**      | 如果没有，就开启一个事务；如果有，就加入当前事务（方法B看到自己已经运行在 方法A的事务内部，就不再起新的事务，直接加入方法A） |
| **RROPAGATION_REQUIRES_NEW**  | 如果没有，就开启一个事务；如果有，就将当前事务挂起。（方法A所在的事务就会挂起，方法B会起一个新的事务，等待方法B的事务完成以后，方法A才继续执行） |
| **PROPAGATION_NESTED**        | 如果没有，就开启一个事务；如果有，就在当前事务中嵌套其他事务 |
| **PROPAGATION_SUPPORTS**      | 如果没有，就以非事务方式执行；如果有，就加入当前事务（方法B看到自己已经运行在 方法A的事务内部，就不再起新的事务，直接加入方法A） |
| **PROPAGATION_NOT_SUPPORTED** | 如果没有，就以非事务方式执行；如果有，就将当前事务挂起，（方法A所在的事务就会挂起，而方法B以非事务的状态运行完，再继续方法A的事务） |
| **PROPAGATION_NEVER**         | 如果没有，就以非事务方式执行；如果有，就抛出异常。           |
| **PROPAGATION_MANDATORY**     | 如果没有，就抛出异常；如果有，就使用当前事务                 |

------

其中**前4种**是开发中用到概率比较大的，建议熟记；**后面3种**不常用，了解就行。

我们经常会提到，方法A传播到方法B，那到底是A调用B，还是B调用A，这个问题我一开始学Spring的时候犯浑过，搞反了，导致久久理解不了。其实只要仔细斟酌字面意思就不会像我那样犯傻了。

A传播到B，显而易见进入A方法执行半途中，再次进入B方法，这才叫做传播到方法B中。

还有一点初学者不要搞错的是，这里的方法A和方法B理论上不应该在一个Service中，而是在不同的Service中，这里面有个坑我们会在后面介绍。

![img](https://up-img.yonghong.tech/pic/2020/06/10-11-19-20181230003-679LqZ.png)

我们的例子使用的是`@Transactional`注解，默认使用REQUIRED传播行为。

假设事务从方法 A 传播到方法 B。

![img](https://up-img.yonghong.tech/pic/2020/06/10-11-19-2018123001-vUXmD7.png)

我们现在面对方法B，其中B会抛出异常。

```java
@Service
public class UserService01 {

    @Autowired
    private UserDao userDao;
    @Autowired
    private LogService01 logService;
    
    @Transactional
    public void A() {
        userDao.insert(new User("admin","123456"));
        logService.B();
    }
}

@Service
class LogService01 {

    @Autowired
    private LogDao logDao;
    
    @Transactional
    public void B() {
        logDao.insert(new Log("abcdefghijklmn","192.168.1.1"));
        System.out.println(1/0);
    }
}
// 方法A和方法B都不会保存数据成功 
```

我们现在面对方法B，其中A会抛出异常。

```java
@Service
public class UserService02 {

    @Autowired
    private UserDao userDao;
    @Autowired
    private LogService02 logService;
    
    @Transactional
    public void A() {
        userDao.insert(new User("admin","123456"));
        logService.B();
        System.out.println(1/0);
    }
}

@Service
class LogService02 {

    @Autowired
    private LogDao logDao;
    
    @Transactional
    public void B() {
        logDao.insert(new Log("abcdefghijklmn","192.168.1.1"));
    }
}
// 方法A和方法B都不会保存数据成功 
```

![img](https://up-img.yonghong.tech/pic/2020/06/10-11-19-2018123002-68a3Ks.png)

我们现在面对方法B，其中B会抛出异常。

```java
@Service
public class UserService03 {

    @Autowired
    private UserDao userDao;
    @Autowired
    private LogService03 logService;
    
    public void A() {
        userDao.insert(new User("admin","123456"));
        logService.B();
    }
}

@Service
class LogService03 {

    @Autowired
    private LogDao logDao;

    @Transactional
    public void B() {
        logDao.insert(new Log("abcdefghijklmn","192.168.1.1"));
        System.out.println(1/0);
    }
}
// 方法A中的数据保存成功，方法B中的数据保存失败
```

我们现在面对方法B，其中A会抛出异常。

```java
@Service
public class UserService04 {

    @Autowired
    private UserDao userDao;
    @Autowired
    private LogService04 logService;
    
    public void A() {
        userDao.insert(new User("admin","123456"));
        logService.B();
        System.out.println(1/0);
    }
}

@Service
class LogService04 {

    @Autowired
    private LogDao logDao;
    
    @Transactional
    public void B() {
        logDao.insert(new Log("abcdefghijklmn","192.168.1.1"));
    }
}
// 方法A中的数据保存成功，方法B中的数据保存成功
```

**如果没有，就开启一个事务**(方法B运行的时候发现自己没有在事务中，它就会为自己分配一个事务)；**如果有，就加入当前事务**。（方法B看到自己已经运行在 方法A的事务内部，就不再起新的事务，直接加入方法A）。这就是 **`PROPAGATION_REQUIRED`**，它也是 Spring 提供的默认事务传播行为，适合绝大多数情况。

![img](https://up-img.yonghong.tech/pic/2020/06/10-11-19-20181230004-QunABz.png)

假设事务从方法 A 传播到方法 B。

![img](https://github.com/love-somnus/interview/wiki/2018123001.png)

**我们现在面对方法B，其中B会抛出异常。**

```java
@Service
public class UserService11 {

    @Autowired
    private UserDao userDao;
    @Autowired
    private LogService11 logService;

    @Transactional
    public void A() {
        userDao.insert(new User("admin","123456"));
        logService.B();
    }
}

@Service
class LogService11 {

    @Autowired
    private LogDao logDao;

    @Transactional(propagation=Propagation.REQUIRES_NEW)
    public void B() {
        logDao.insert(new Log("abcdefghijklmn","192.168.1.1"));
        System.out.println(1/0);
    }
}
// 方法A中的数据保存失败，方法B中的数据保存失败

@Service
public class UserService11_ {
    @Autowired
    private UserDao userDao;
    @Autowired
    private LogService11_ logService;

    @Transactional(noRollbackFor=ArithmeticException.class)
    public void A() {
        userDao.insert(new User("admin","123456"));
        logService.B();
    }
}

@Service
class LogService11_ {

    @Autowired
    private LogDao logDao;

    @Transactional(propagation=Propagation.REQUIRES_NEW)
    public void B() {
        logDao.insert(new Log("abcdefghijklmn","192.168.1.1"));
        System.out.println(1/0);
    }
}
// 方法A中的数据保存成功，方法B中的数据保存失败
```

**我们现在面对方法B，其中A会抛出异常**。

```java
@Service
public class UserService12 {

    @Autowired
    private UserDao userDao;
    @Autowired
    private LogService12 logService;
    
    @Transactional
    public void A() {
        userDao.insert(new User("admin","123456"));
        logService.B();
        System.out.println(1/0);
    }
}

@Service
class LogService12 {

    @Autowired
    private LogDao logDao;

    @Transactional(propagation=Propagation.REQUIRES_NEW)
    public void B() {
        logDao.insert(new Log("abcdefghijklmn","192.168.1.1"));
    }
}
// 方法A中的数据保存失败，方法B中的数据保存成功
```

![img](https://github.com/love-somnus/interview/wiki/2018123002.png)

例子可以参考**PROPAGATION_REQUIRED**，它们都是如果A没有事务，B就为自己分配一个事务。

**如果没有，就开启一个事务**(方法B运行的时候发现自己没有在事务中，它就会为自己分配一个事务)；**如果有，就将当前事务挂起**。（方法A所在的事务就会挂起，方法B会起一个新的事务，等待方法B的事务完成以后，方法A才继续执行）。这就是 `RROPAGATION_REQUIRES_NEW`，意思就是创建了一个新事务，它和原来的事务没有任何关系了。

`RROPAGATION_REQUIRES_NEW`与 **`PROPAGATION_REQUIRED`** 的事务区别在于事务的回滚程度了。因为 方法B是新起一个事务，那么就是存在两个不同的事务。

1. 如果方法B已经提交，那么 方法A失败回滚，方法B是不会回滚的。
2. 如果方法B失败回滚，如果它抛出的异常被方法A捕获，方法A的事务仍然可能提交（主要看方法B抛出的异常是不是方法A会回滚的异常）

![img](https://up-img.yonghong.tech/pic/2020/06/10-11-19-20181230005-q9rkPU.png)

**如果没有，就开启一个事务(方法B运行的时候发现自己没有在事务中，它就会为自己分配一个事务)；如果有，就在当前事务中嵌套其他事务。**这就是PROPAGATION_NESTED，也就是传说中的“嵌套事务”了，所嵌套的子事务与主事务之间是有关联的（当主事务提交或回滚，子事务也会提交或回滚）。方法A所在的事务就会挂起，方法B会起一个新的子事务并设置savepoint，等待方法B的事务完成以后，方法A才继续执行。因为方法B是外部事务的子事务，那么

1. 如果方法B已经提交，那么方法A失败回滚，方法B也将回滚。（REQUIRES_NEW中此种情况方法B是不会回滚的，因为方法B是独立事务，提交就是提交了）
2. 如果方法B失败回滚，如果它抛出的异常被方法A捕获，方法A的事务仍然可能提交（主要看方法B抛出的异常是不是方法A会回滚的异常）

理解**NESTED**的关键是**savepoint**。他与**REQUIRES_NEW**的区别是： **REQUIRES_NEW**完全是一个新的事务,它与外部事务相互独立； 而 **NESTED** 则是外部事务的子事务, 如果外部事务commit, 嵌套事务也会被**commit**, 这个规则同样适用于**roll back**

![img](https://up-img.yonghong.tech/pic/2020/06/10-11-19-20181230006-X277O5.png)

**如果没有，就以非事务方式执行**（如果发现方法A没有开启事务，则方法B也不开启事务）；**如果有，就加入当前事务。**（方法B看到自己已经运行在方法A的事务内部，就不再起新的事务，直接加入方法A）。这就是 **PROPAGATION_SUPPORTS**，这种方式非常随意，没有就没有，有就有，有点无所谓的态度，反正我是支持你的。

![img](https://up-img.yonghong.tech/pic/2020/06/10-11-19-20181230007-PgZlzQ.png)

**如果没有，就以非事务方式执行**（如果发现方法A没有开启事务，则方法B也不开启事务）；**如果有，就将当前事务挂起**。（方法A的事务挂起，而方法B非事务的状态运行完，再继续方法A的事务。）这就是 **PROPAGATION_NOT_SUPPORTED**，这种方式非常强硬，没有就没有，有我也不支持你，把你挂起来，不鸟你。

![img](https://up-img.yonghong.tech/pic/2020/06/10-11-19-20181230008-wZZUsp.png)

**如果没有，就以非事务方式执行**（如果发现方法A没有开启事务，则方法B也不开启事务）；**如果有，就抛出异常**（如果发现方法A有开启事务，则方法B直接抛出异常）。这就是 **PROPAGATION_NEVER**，这种方式更猛，没有就没有，有了反而报错，确实够牛的，它说：我从不支持事务！

![img](https://up-img.yonghong.tech/pic/2020/06/10-11-19-20181230009-SZYqIs.png)

如果没有，就抛出异常；如果有，就使用当前事务。这就是 **`PROPAGATION_MANDATORY`**，这种方式可以说是牛逼中的牛逼了，没有事务直接就报错，确实够狠的，它说：我必须要有事务！

![img](https://up-img.yonghong.tech/pic/2020/06/10-11-19-20181230010-XCj0iS.png)

需要注意的是 **`PROPAGATION_NESTED`**，不要被它的名字所欺骗，Nested（嵌套），所以凡是在类似方法 A 调用方法 B 的时候，在方法 B 上使用了这种事务传播行为，如果您真的那样做了，那您就错了。因为您错误地以为 **`PROPAGATION_NESTED`** 就是为方法嵌套调用而准备的，其实默认的 **`PROPAGATION_REQUIRED`** 就可以帮助您，做您想要做的事情了。

Spring 给我们带来了事务传播行为，这确实是一个非常强大而又实用的功能。除此以外，也提供了一些小的附加功能，比如：

1. **事务超时（Transaction Timeout）**：为了解决事务时间太长，消耗太多的资源，所以故意给事务设置一个最大时常，如果超过了，就回滚事务。
2. **只读事务（Readonly Transaction）**：为了忽略那些不需要事务的方法，比如读取数据，这样可以有效地提高一些性能。 最后，推荐大家使用 Spring 的注解式事务配置，而放弃 XML 式事务配置。因为注解实在是太优雅了，当然这一切都取决于您自身的情况了。

在 Spring 配置文件中使用：

```
...  
<tx:annotation-driven/>  
... 
```

在需要事务的方法上使用：

```
@Transactional  
public void xxx() {  
    ...  
}  
```

可在 `@Transactional` 注解中设置：事务隔离级别、事务传播行为、事务超时时间、是否只读事务。 简直是太完美了，太优雅了！

Spring默认情况下会对运行期例外(RunTimeException)，即uncheck异常，进行事务回滚。 如果遇到checked异常就不回滚。

如何改变默认规则：

- 让checked例外也回滚：在整个方法前加上

```
@Transactional(rollbackFor=Exception.class)
```

- 让unchecked例外不回滚：

```
@Transactional(notRollbackFor=RunTimeException.class)
```

最后，有必要对本文的内容做一个总结，免费赠送一张高清无码思维导图：

![img](https://up-img.yonghong.tech/pic/2020/06/10-11-19-20181230011-Sv6pY9.png)

