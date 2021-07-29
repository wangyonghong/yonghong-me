---
layout: post
title:  "MySQL 的 xml 和 json 支持"
category: "MySQL"
tags: ["MySQL", "xml", "json", "Java", "Python"]
date: 2018-11-20 00:00:00
updated: 2018-11-20 00:00:00
---

MySQL 的 xml 和 json 支持

<!-- more -->

```sql
-- 测试 MySQL 5.6 MySQL 8.0 通过
create table xml(
	id int not null auto_increment,
	xml varchar(255) not null,
	primary key(id)
);

insert into xml(xml) values('<sucess>100</sucess>');
insert into xml(xml) values('<sucess>100</sucess><failure>200</failure>');

select id, extractvalue(xml, 'sucess') as sucess from xml;

+----+--------+
| id | sucess |
+----+--------+
|  1 | 100    |
|  2 | 100    |
+----+--------+
1 row in set (0.00 sec)

select id, extractvalue(xml, 'sucess') as sucess, extractvalue(xml, 'failure') as failure from xml;
+----+--------+---------+
| id | sucess | failure |
+----+--------+---------+
|  1 | 100    |         |
|  2 | 100    | 200     |
+----+--------+---------+
2 rows in set (0.00 sec)

```



```sql
-- 测试 MySQL 8.0 通过
create table json(
	id int not null auto_increment,
	json varchar(255) not null,
	primary key(id)
);


insert into json(json) values('{"name": "Alice", "sex": "female", "age": 23}');
insert into json(json) values('{"name": "Bob", "sex": "male", "age": 20}');

select json_extract(json, '$.name') as name, json_extract(json, '$.sex') as sex, json_extract(json, '$.age') as age from json;
+---------+----------+------+
| name    | sex      | age  |
+---------+----------+------+
| "Alice" | "female" | 23   |
| "Bob"   | "male"   | 20   |
+---------+----------+------+
2 rows in set (0.00 sec)
```

















