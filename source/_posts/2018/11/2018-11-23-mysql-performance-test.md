---
layout: post
title:  "MySQL 性能测试"
category: "MySQL"
tags: ["MySQL"]
date: 2018-11-23 00:00:00
updated: 2018-11-23 00:00:00
---

磁盘性能测试

<!-- more -->

```shell
<!-- 读性能 -->
$ sudo hdparm -Tt /dev/sda

/dev/sda:
 Timing cached reads:   31426 MB in  1.99 seconds = 15775.74 MB/sec
 Timing buffered disk reads: 540 MB in  3.01 seconds = 179.61 MB/sec

<!-- 写性能 -->
$ sync;/usr/bin/time -p bash -c "(dd if=/dev/zero of=test.dd  bs=1000K count=20000;sync)"
20000+0 records in
20000+0 records out
20480000000 bytes (20 GB, 19 GiB) copied, 103.692 s, 198 MB/s
real 111.08
user 0.02
sys 31.16

<!-- 读性能 -->
$ sudo echo 3 > /proc/sys/vm/drop_caches ; /usr/bin/time -p dd if=test.dd of=/dev/null  bs=1M 
-bash: /proc/sys/vm/drop_caches: Permission denied
19531+1 records in
19531+1 records out
20480000000 bytes (20 GB, 19 GiB) copied, 83.2042 s, 246 MB/s
real 83.20
user 0.09
sys 12.90

```


```
create database performance default charset utf8mb4;
user performance;

create table user1(
    id int not null,
    name varchar(20) not null,
    sex tinyint(1) not null,
    email varchar(255) not null,
    company varchar(255) not null,
    address varchar(255) not null
) engine=InnoDB;

create table user2(
    id int not null,
    name varchar(20) not null,
    sex tinyint(1) not null,
    email varchar(255) not null,
    company varchar(255) not null,
    address varchar(255) not null
) engine=InnoDB;

create table user3(
    id int not null,
    name varchar(20) not null,
    sex tinyint(1) not null,
    email varchar(255) not null,
    company varchar(255) not null,
    address varchar(255) not null
);

create table user4(
    id int not null,
    name varchar(20) not null,
    sex tinyint(1) not null,
    email varchar(255) not null,
    company varchar(255) not null,
    address varchar(255) not null
)engine=MyISAM;

create table user5(
    id int not null,
    name varchar(20) not null,
    sex tinyint(1) not null,
    email varchar(255) not null,
    company varchar(255) not null,
    address varchar(255) not null
)engine=MyISAM;

create table user6(
    id int not null,
    name varchar(20) not null,
    sex tinyint(1) not null,
    email1 varchar(255) not null,
    email2 varchar(255) not null,
    email3 varchar(255) not null,
    email4 varchar(255) not null,
    email5 varchar(255) not null,
    email6 varchar(255) not null,
    email7 varchar(255) not null,
    email8 varchar(255) not null,
    company varchar(255) not null,
    address varchar(255) not null
)engine=MyISAM;

create table user7(
    id int not null,
    name varchar(20) not null,
    sex tinyint(1) not null,
    email1 varchar(255) not null,
    email2 varchar(255) not null,
    email3 varchar(255) not null,
    email4 varchar(255) not null,
    email5 varchar(255) not null,
    email6 varchar(255) not null,
    email7 varchar(255) not null,
    email8 varchar(255) not null,
    email9 varchar(255) not null,
    email10 varchar(255) not null,
    email11 varchar(255) not null,
    email12 varchar(255) not null,
    email13 varchar(255) not null,
    email14 varchar(255) not null,
    email15 varchar(255) not null,
    email16 varchar(255) not null,
    company varchar(255) not null,
    address varchar(255) not null
)engine=MyISAM;

create table user8(
    id int not null,
    name varchar(20) not null,
    sex tinyint(1) not null,
    email1 varchar(255) not null,
    email2 varchar(255) not null,
    email3 varchar(255) not null,
    email4 varchar(255) not null,
    email5 varchar(255) not null,
    email6 varchar(255) not null,
    email7 varchar(255) not null,
    email8 varchar(255) not null,
    email9 varchar(255) not null,
    email10 varchar(255) not null,
    email11 varchar(255) not null,
    email12 varchar(255) not null,
    email13 varchar(255) not null,
    email14 varchar(255) not null,
    email15 varchar(255) not null,
    email16 varchar(255) not null,
    company varchar(255) not null,
    address varchar(255) not null
)engine=InnoDB;
```

```sql
delimiter $$
CREATE PROCEDURE user1_insert(IN count int)
begin
DECLARE x int;
SET x = 1;
SET count = count + 1;
START TRANSACTION; 
REPEAT
    insert into `user1` values(x, "abc", 1, "abc@abc.com", "abc.com", "New York");
    set x = x + 1;
until x = count END REPEAT;
COMMIT;
END$$
delimiter ;
-- 34kb

delimiter $$
CREATE PROCEDURE user2_insert(IN count int)
begin
DECLARE x int;
SET x = 1;
SET count = count + 1;
START TRANSACTION; 
REPEAT
    insert into `user2` values(x, "abcdefghijklmnopqrst", 1, "abcdefghijklm@abcdefghijkl.com", "abcdefghijklmnopqrstuvwxyz.com", "New York, American");
    set x = x + 1;
until x = count END REPEAT;
COMMIT;
END$$
delimiter ;
-- 103kb 实际是112kb

delimiter $$
CREATE PROCEDURE user2_insert(IN count int)
begin
DECLARE x int;
SET x = 1;
SET count = count + 1;
START TRANSACTION; 
REPEAT
    insert into `user2` values(x, "abcdefghijklmnopqrst", 1, "abcdefghijklm@abcdefghijkl.com", "abcdefghijklmnopqrstuvwxyz.com", "New York, American");
    set x = x + 1;
until x = count END REPEAT;
COMMIT;
END$$
delimiter ;


delimiter $$
CREATE PROCEDURE user4_insert(IN count int)
begin
DECLARE x int;
SET x = 1;
SET count = count + 1;
START TRANSACTION; 
REPEAT
    insert into `user4` values(x, "abcdefghijklmnopqrst", 1, "abcdefghijklm@abcdefghijkl.com", "abcdefghijklmnopqrstuvwxyz.com", "New York, American");
    set x = x + 1;
until x = count END REPEAT;
COMMIT;
END$$
delimiter ;


delimiter $$
CREATE PROCEDURE user6_insert(IN count int)
begin
DECLARE x int;
SET x = 1;
SET count = count + 1;
START TRANSACTION; 
REPEAT
    insert into `user6` values(x, "abcdefghijklmnopqrst", 1, 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.com", 
    	"New York, American");
    set x = x + 1;
until x = count END REPEAT;
COMMIT;
END$$
delimiter ;

delimiter $$
CREATE PROCEDURE user7_insert(IN count int)
begin
DECLARE x int;
SET x = 1;
SET count = count + 1;
START TRANSACTION; 
REPEAT
    insert into `user7` values(x, "abcdefghijklmnopqrst", 1, 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.com", 
    	"New York, American");
    set x = x + 1;
until x = count END REPEAT;
COMMIT;
END$$
delimiter ;

delimiter $$
CREATE PROCEDURE user8_insert(IN count int)
begin
DECLARE x int;
SET x = 1;
SET count = count + 1;
START TRANSACTION; 
REPEAT
    insert into `user8` values(x, "abcdefghijklmnopqrst", 1, 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.com", 
    	"abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.com", 
    	"New York, American");
    set x = x + 1;
until x = count END REPEAT;
COMMIT;
END$$
delimiter ;

```

查看 MySQL 数据存放位置

```
show global variables like "%datadir%";
```

查看磁盘 io 性能


```
iostat -d -k 1 |grep sda

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn

```


| 引擎   | 数据大小/条 | 索引 | 数据条数  | 总数据大小     | 时间             | 备注             | 硬盘速度            |
| ------ | ----------- | ---- | --------- | -------------- | ---------------- | ---------------- | ------------------- |
| InnoDB | 4136B       | 无   | 5,000,000 | 27,728,543,744 | 45 min 58.50 sec | REPEATABLE-READ  | 10,052,037=9.57M/s  |
| MyISAM | 4136B       | 无   | 5,000,000 | 20,680,000,000 | 2 min 55.91 sec  |                  | 117,560,116=112M/s  |
| MyISAM | 2216B       | 无   | 5,000,000 | 11,080,000,000 | 1 min 49.14 sec  |                  | 101,520,982=96.8M/s |
| InnoDB | 4136B       | 无   | 5,000,000 | 27,715,960,832 | 45 min 21.71 sec | READ-UNCOMMITTED | 10,183,289=9.71M/s   |
| MyISAM | 112B        | 无   | 5,000,000 | 560,000,000    | 50.24 sec        |                  | 11,146,496=10.63M/s |
| MyISAM | 536B        | 无   | 5,000,000 | 2,680,000,000  | 1 min 2.56 sec   |                  | 42,838,874=40.85M/s |
|        |             |      |           |                |                  |                  |                     |

