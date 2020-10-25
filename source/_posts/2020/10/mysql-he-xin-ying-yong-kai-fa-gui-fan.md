---
title: MySQL核心应用开发规范
tags:
- MySQL
- 开发规范
categories:
- 学习笔记
date: 2020-10-25 17:00:00
updated: 2020-10-25 17:00:00
---

MySQL核心应用开发规范总结起来有三点：表越窄越好，表越小越好，请求够高效，接下来详细解释一下这三点。

## 表越窄越好
设计表字段的时候，选择的数据类型够用就行。

- 存储账号名（长度≤30）就没必要 varchar(255)
- Unix时间戳，可以使用无符号整型（INT UNSIGNED）
- IPv4地址，也可以使用无符号整型（INET_AOTN()和INET_NTOA()函数）

可以通过执行 show table status 来查看表的统计信息：
- Avg_row_length 值超过100字节
- Data_free 值大于0说明表存在碎片

<!-- more -->
## 表越小越好

真正“好”的架构：
- 让我们线上的业务表，它的数据量尽可能小
- 热表数据量足够小，IO操作代价更小（分库分表，冷热数据分离，窄表5000万，宽表50万）

## 请求够高效
事务要尽快的提交/回滚

修改/删除数据 ——> 锁定数据行

表锁 未释放导致其他SQL或事务被阻塞

捕获长时间未提交的SQL或事务
- 监控MySQL的线程状态
- 监控InnoDB的事务状态
- 设置时长超过5秒告警
- 设置锁表行数大于10告警
- 检查或者监控SQL注入的风险（SLEEP()函数，UNION ALL请求）

## 其他重要细节

### schema设计原则

1.尽量小的原则
2.禁止使用外键——增加行锁
3.自增INT/BIGINT主键（InnoDB引擎表如果使用char或者uuid作为主键，会导致数据存储的顺序离散随机，影响性能）
4.字符集和库表的设计要一致，MySQL实例，database，table，column，存储过程，event，都要保持一致
5.MySQL尽量高效的建议
  - 单表
    - ①单表的数据量尽量不要超过5000万
    - ②单表的物理大小尽量不要超过20G
    - ③索引的数量不要超过5个
  - 实例
    - ①总的大小不要超过500G
    - ②总表数量不要超过5000个（包含分区）
    
有一个例子是t1表是utf8mb4编码（四个字节），t2是utf8编码（三个字节）


```sql
CREATE TABLE `t1` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `c1` int(10) unsigned NOT NULL DEFAULT '0',
  `c2` varchar(270) NOT NULL DEFAULT '',
  `c3` varchar(30) NOT NULL DEFAULT '',
  `c4` varchar(40) NOT NULL DEFAULT '',
  PRIMARY KEY(`id`),
  KEY `int_col` (`c1`),
  KEY `char_col` (`c2`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `t2` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `c1` int(10) unsigned NOT NULL DEFAULT '0',
  `c2` varchar(270) NOT NULL DEFAULT '',
  `c3` varchar(30) NOT NULL DEFAULT '',
  `c4` varchar(40) NOT NULL DEFAULT '',
  PRIMARY KEY(`id`),
  KEY `int_col` (`c1`),
  KEY `char_col` (`c2`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

当两个表做join时，select t1 后c2是4个字节的编码，带入t2后，无法使用索引。

```sql
mysql> desc select * from t1 left join t2 on t1.c2 = t2.c2 where t1.id > 500;
+----+-------------+-------+------------+-------+---------------+---------+---------+------+------+----------+----------------------------------------------------+
| id | select_type | table | partitions | type  | possible_keys | key     | key_len | ref  | rows | filtered | Extra                                              |
+----+-------------+-------+------------+-------+---------------+---------+---------+------+------+----------+----------------------------------------------------+
|  1 | SIMPLE      | t1    | NULL       | range | PRIMARY       | PRIMARY | 8       | NULL |    1 |   100.00 | Using where                                        |
|  1 | SIMPLE      | t2    | NULL       | ALL   | NULL          | NULL    | NULL    | NULL |    1 |   100.00 | Using where; Using join buffer (Block Nested Loop) |
+----+-------------+-------+------------+-------+---------------+---------+---------+------+------+----------+----------------------------------------------------+
2 rows in set, 1 warning (0.01 sec)
```

当把t2的编码也改成utf8mb4后，可以正常使用索引。

```sql
mysql> desc select * from t1 left join t2 on t1.c2 = t2.c2 where t1.id > 500;                                                                                           +----+-------------+-------+------------+-------+---------------+----------+---------+------------+------+----------+-------------+
| id | select_type | table | partitions | type  | possible_keys | key      | key_len | ref        | rows | filtered | Extra       |
+----+-------------+-------+------------+-------+---------------+----------+---------+------------+------+----------+-------------+
|  1 | SIMPLE      | t1    | NULL       | range | PRIMARY       | PRIMARY  | 8       | NULL       |    1 |   100.00 | Using where |
|  1 | SIMPLE      | t2    | NULL       | ref   | char_col      | char_col | 1082    | demo.t1.c2 |    1 |   100.00 | NULL        |
+----+-------------+-------+------------+-------+---------------+----------+---------+------------+------+----------+-------------+
2 rows in set, 1 warning (0.01 sec)
```

### 库表字段设计规范

1.每个表建议不要超过50个字段
2.优先选择utf8mb4字符集
3.严谨在数据库中明文存储用户的一些核心数据（密码，身份证号等，自己定义加密算法）
4.用好INT数据类型（UNSIGNED，金额用途——扩大N倍使用bigint）
5.遇到大对象数据类型（BLOB、TEXT）字段，尽量拆出去，再用主键做关联
6.字符类型尽可能使用varchar的数据类型（同长度更新）
7.日期数据数据建议采用datetime数据类型（datetime类型 0000-9999年，timestamp类型 1970-2038）

### SQL开发的建议

1.多表JOIN时，JOIN列的数据类型要一致
2.多表JOIN时，把过滤后结果集较小的表作为驱动表（或者使用 inner join 让优化器去做优化）
3.在查询的where条件中用上函数或表达式要用8.0版本
4.不要看到where条件中出现的列就直接创建索引
5.尽可能不要去执行select *操作
6.不要执行LIKE '%x%'
7.尽可能不要用 "!=" 条件
8.如果能确定返回结果数量的话最好加上 LIMIT N，优化器通常会再进一步优化，参考[LIMIT优化](https://dev.mysql.com/doc/refman/8.0/en/limit-optimization.html)
9.优先使用UNION ALL，代替UNION
10.所有的SQL都要通过SQL审核系统检查，符合标准后才能上线





