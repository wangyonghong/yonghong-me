---
layout: post
title: Hibernate 原理及实战（三）
categories: [Hibernate]
tags: [Hibernate, Java]
date: 2018-07-28 00:00:00
updated: 2018-07-28 00:00:00
---

### 一对多的操作

#### 一对多映射配置

以客户和联系人为例。客户是一，联系人是多。

<!-- more -->

第一步：创建两个实体类，客户和联系人。

第二步：让两个实体类之间相互表示。

（1）在客户实体类里面表示多个联系人

- 一个客户里面有多个联系人

```java
// 在客户实体类里面表示多个联系人，一个客户有多个联系人
// Hibernate 要求使用集合表示多的数据，使用 set 集合
private Set<LinkMan> setLinkMan = new HashSet<LinkMan>();
public Set<LinkMan> getSetLinkMan() {
    return setLinkMan;
}
public void setSetLinkMan(Set<LinkMan> setLinkMan) {
    this.setLinkMan = setLinkMan;
}
```

（2）在联系人实体类里面表示所属客户

- 一个联系人只能属于一个客户

```java
// 在联系人实体类里面表示所属客户，一个联系人只能属于一个客户
private Customer customer;
public Customer getCustomer() {
    return customer;
}
public void setCustomer(Customer customer) {
    this.customer = customer;
}
```

第三步：配置映射关系

（1）一般一个实体类对应一个映射文件

（2）把映射最基本配置完成

（3）在映射文件中，配置一对多关系

- 在客户映射文件中，表示所有联系人

```xml
<!-- 在客户映射文件中，表示所有联系人
    使用 set 标签表示所有联系人
    set 标签里面有 name 属性
        属性值写在客户实体类里面表示联系人的 set 集合的名称
-->
<set name="setLinkMan">
    <!-- 一对多建表，有外键
        Hibernate 机制：双向维护外键，在一和多那一方都配置外键
        column 属性值，外键名称
    -->
    <key column="clid"></key>
    <!-- 客户所有联系人，class 里面写联系人实体类全路径 -->
    <one-to-many class="com.example.LinkMan"/>
</set>

```

- 在联系人映射文件中，表示所属客户

```xml
<!-- 表示联系人所属客户
    name 属性：因为在联系人实体类中使用 customer 对象表示，写    customer 名称
    class 属性：customer 全路径
    column 属性：外键名称
-->
<many-to-one name="customer" class="com.example.Customer" column="clid"></many-to-one>
```

第四部：创建核心配置文件，把映射文件引入核心配置文件中。


#### 一对多的级联保存

复杂写法

```java
// 添加一个客户，为这个客户添加一个联系人
// 1.创建客户和联系人对象
Customer customer = new Customer();
customer.setCustomerName("Google");
customer.setCustomerLevel("vip");
customer.setCustomerPhone("111");

LinkMan linkman = new LinkMan();
linkMan.setLinkManName("Lucy");
linkMan.setLinkManGender("女");
linkMan.setLinkManPhone("222");

// 2.在客户表示所有联系人，在联系人表示客户
// 建立客户对象和联系人对象关系
// 2.1.把联系人对象，放到客户对象的 set 集合里面
customer.getSetLinkMan().add(linkman);
// 2.2.把客户对象放到联系人里面
linkman.setCustomer(customer);

// 3.保存到数据库
session.save(customer);
session.save(linkman);
```

简化写法

一般根据客户添加来添加联系人

第一步，在客户映射文件中进行配置
- 在客户映射文件里面 set 标签进行配置 （cascade 属性）

```xml
<set name="setLinkMan" cascade="save-update">
    <!-- 一对多建表，有外键
        Hibernate 机制：双向维护外键，在一和多那一方都配置外键
        column 属性值，外键名称
    -->
    <key column="clid"></key>
    <!-- 客户所有联系人，class 里面写联系人实体类全路径 -->
    <one-to-many class="com.example.LinkMan"/>
</set>
```

第二步，创建客户和联系人对象，只需要把联系人放到客户里面就可以了，最终只需要保存客户就可以了。

```java
// 添加一个客户，为这个客户添加一个联系人
// 1.创建客户和联系人对象
Customer customer = new Customer();
customer.setCustomerName("Google");
customer.setCustomerLevel("vip");
customer.setCustomerPhone("111");

LinkMan linkman = new LinkMan();
linkMan.setLinkManName("Lucy");
linkMan.setLinkManGender("女");
linkMan.setLinkManPhone("222");

// 2.把联系人对象，放到客户对象的 set 集合里面
customer.getSetLinkMan().add(linkman);

// 3.保存到数据库
session.save(customer);
```

#### 一对多的级联删除

1.删除某个客户，把客户里面所有的联系人删除

2.具体实现

第一步，在客户映射文件 set 标签进行配置

- 使用属性 cascade 属性值 delete

```xml
<set name="setLinkMan" cascade="save-update,delete">
    ……
</set>
```

第二步，在代码中直接删除客户

- 根据 id 查询出对象，调用 session 里面的 delete 方法删除

```java
// 根据 id 查询客户对象
Customer customer = session.get(Customer.class, 2);
session.delete(customer);
```

Hibernate 内部实现：

- （1）根据 id 查询客户
- （2）根据外键查联系人
- （3）把联系人外键设置为 null
- （4）删除联系人和客户


#### 一对多的修改操作

1.让 Lucy 联系人所属客户不是 Google 而是 Baidu

```java
Customer baidu = session.get(Customer.class, 1);
LinkMan lucy = session.get(LinkMan.class, 2);

baidu.getSetLinkMan().add(lucy);
lucy.setCustomer(baidu);
```

2.inverse 属性

（1）因为 Hibernate 双向维护外键，在客户和联系人里面都需要维护外键，修改客户的时候，修改一次外键，修改联系人时候也修改一次外键。


（2）解决方式，让其中的一方不维护外键。
- 一对多的里面，可以让一的那一方放弃维护外键
- 一个国家有总统，国家有很多人，总统不能认识国家所有人，国家所有人认识总统

（3）具体实现
在放弃关系维护映射文件中，进行配置
inverse 属性默认值，false 不放弃关系维护。true 放弃关系维护

```xml
<set name="setLinkMan" cascade="save-update,delete" inverse="true">
    ……
</set>
```

### 多对多的操作

#### 多对多的映射配置

以用户和角色为例演示

第一步，创建实体类，用户和角色

第二步，两个实体类之间互相表示

（1）一个用户里面表示所有角色，使用 set 集合

（2）一个角色有多个用户，使用 set 集合



```java
public class User {
    private Integer userId;
    private String userName;
    private String userPassword;

    // 一个用户可以有多个角色
    private Set<Role> roleSet = new HashSet<Role>();

    public Integer getUserId() {
        return userId;
    }

    public void setUserId(Integer userId) {
        this.userId = userId;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getUserPassword() {
        return userPassword;
    }

    public void setUserPassword(String userPassword) {
        this.userPassword = userPassword;
    }

    public Set<Role> getRoleSet() {
        return roleSet;
    }

    public void setRoleSet(Set<Role> roleSet) {
        this.roleSet = roleSet;
    }
}
```

```java
public class Role {

    private Integer roleId;
    private String roleName;
    private String roleMemo;

    // 一个角色有多个用户
    private Set<User> userSet = new HashSet<User>();

    public Integer getRoleId() {
        return roleId;
    }

    public void setRoleId(Integer roleId) {
        this.roleId = roleId;
    }

    public String getRoleName() {
        return roleName;
    }

    public void setRoleName(String roleName) {
        this.roleName = roleName;
    }

    public String getRoleMemo() {
        return roleMemo;
    }

    public void setRoleMemo(String roleMemo) {
        this.roleMemo = roleMemo;
    }

    public Set<User> getUserSet() {
        return userSet;
    }

    public void setUserSet(Set<User> userSet) {
        this.userSet = userSet;
    }

}
```



第三步，配置映射关系

（1）基本配置
（2）配置多对多关系

```xml
<hibernate-mapping>
    <class name="com.example.manytomany.User" table="h_user">
        <id name="userId">
            <generator class="native"/>
        </id>
        <property name="userName"></property>
        <property name="userPassword"></property>

        <!-- 在用户里面表示所有角色，使用 set 标签
            name 属性：角色 set 集合的名称
            table 属性：第三张表的名称
        -->
        <set name="roleSet" table="user_role">
            <!-- key 标签里面配置
                配置当前映射文件在第三张表外键名称
            -->
            <key column="userId"></key>
            <!-- class：角色实体类全路径
                column：角色在第三张表外键名称
            -->
            <many-to-many class="com.example.manytomany.Role" column="roleId"></many-to-many>
        </set>
    </class>
</hibernate-mapping>
```


```xml
<hibernate-mapping>
    <class name="com.example.manytomany.Role" table="h_role">
        <id name="roleId">
            <generator class="native"/>
        </id>
        <property name="roleName"></property>
        <property name="roleMemo"></property>

        <!-- 在角色里面表示所有用户，使用 set 标签 -->
        <set name="userSet" table="user_role">
            <!-- 角色在第三张表外键 -->
            <key column="roleId"></key>
            <many-to-many class="com.example.manytomany.User" column="userId"></many-to-many>
        </set>
    </class>
</hibernate-mapping>
```


第四步，在核心配置文件中引入映射文件

```xml
<mapping resource="com/example/manytomany/User.hbm.xml"></mapping>
<mapping resource="com/example/manytomany/Role.hbm.xml"></mapping>
```

测试

```sql
Hibernate: 
    
    create table h_role (
       roleId integer not null auto_increment,
        roleName varchar(255),
        roleMemo varchar(255),
        primary key (roleId)
    ) engine=InnoDB
Hibernate: 
    
    create table h_user (
       userId integer not null auto_increment,
        userName varchar(255),
        userPassword varchar(255),
        primary key (userId)
    ) engine=InnoDB
Hibernate: 
    
    create table user_role (
       userId integer not null,
        roleId integer not null,
        primary key (roleId, userId)
    ) engine=InnoDB
Hibernate: 
    
    alter table user_role 
       add constraint FKcq0a9hk8ih49tsd3k3utiudja 
       foreign key (roleId) 
       references h_role (roleId)
Hibernate: 
    
    alter table user_role 
       add constraint FKrvh8yck15ehe3j6kn5k8eoknm 
       foreign key (userId) 
       references h_user (userId)

```



#### 多对多的级联保存

根据用户保存角色

第一步，在用户配置文件中 set 标签进行配置，cascade 值 save-update

```xml
<set name="roleSet" table="user_role" cascade="save-update">
    ……
</set>
```

第二步

```java
public static void main(String[] args) {

    SessionFactory sessionFactory = HibernateUtils.getSessionFactory();

    // 使用 SessionFactory 创建 session 对象
    Session session = sessionFactory.openSession();

    // 开启事务
    Transaction transaction = session.beginTransaction();

    // 添加两个用户，为每个用户添加两个角色
    // 1.创建对象

    User user1 = new User();
    User user2 = new User();

    user1.setUserName("Tom");
    user1.setUserPassword("tom123");

    user2.setUserName("Jerry");
    user2.setUserPassword("jerry123");

    Role r1 = new Role();
    r1.setRoleName("总经理");

    Role r2 = new Role();
    r2.setRoleName("秘书");

    Role r3 = new Role();
    r3.setRoleName("保安");

    // 2.建立关系，把角色放到用户里面
    // user1 -- r1/r2
    // user2 -- r2/r3

    user1.getRoleSet().add(r1);
    user1.getRoleSet().add(r2);
    user2.getRoleSet().add(r2);
    user2.getRoleSet().add(r3);

    // 3.保存用户

    session.save(user1);
    session.save(user2);
    
    // 提交事务
    transaction.commit();

    // 关闭资源
    session.close();
    sessionFactory.close();
}
```

#### 多对多的级联删除

第一步，在 set 标签中配置 cascade 值 delete

```xml
<set name="roleSet" table="user_role" cascade="save-update, delete">
    ……
</set>
```

第二步，删除

```java
User user = session.get(User.class, 5);
session.delete(user);
```

#### 维护第三张表

用户和角色多对多关系，维护关系通过第三张表维护

让某个用户有某个角色
第一步，根据 id 查询用户和角色

第二步，把用户数放到用户里面
- 把角色对象放到用户 set 集合

```java
User user = session.get(User.class, 7);
Role role = session.get(Role.class, 11);

user.getRoleSet().add(role);
```


让某个用户没有某个角色

第一步，根据 id 查询用户和角色

第二步，从用户里面把角色去掉
- 从 set 集合里面把角色移除

```java
User user = session.get(User.class, 8);
Role role = session.get(Role.class, 11);

user.getRoleSet().remove(role);
```




