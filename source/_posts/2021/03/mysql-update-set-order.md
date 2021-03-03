---
title: MySQL update 语句 set 顺序
tags:
- MySQL
- UPDATE
- 数据库
categories:
- MySQL
date: 2021-03-01 22:24:00
updated: 2021-03-01 22:24:00
---

绝大多数数据库，在执行 update 语句时，update t set a = b, b = a 便可实现 a、b 列值互换，赋值表达式右侧的值取的都是原始值。MySQL 则是例外，其单表更新是自左到右依次完成，即先完成 a = b，然后在完成 b = a (此时 a = b），所以执行结果变成 a、b 列都是 b，然后多表更新则又不尊从该更新法则。

这个问题源于业务中一次对券有效期进行延期的操作，需求是对优惠券有效期延期 35 天。

- 一部分券在生效中，直接修改过期时间即可；
- 一部分券已经过期，修改过期时间后，需要判断一下是否仍然是过期的还是生效中的，修改券的状态

<!-- more -->
所以 SQL 语句大致如下：

```sql
UPDATE coupon 
SET end_time = DATE_ADD(end_time, INTERVAL 35 DAY), 
status = (CASE WHEN end_time > NOW() THEN '生效中' ELSE '已过期' END), 
gmt_modify = NOW() 
WHERE ... ;
```

## 问题引入

这个地方就有个问题，当修改 status 的时候 end_time 到底是原始数据，还是修改后的数据。经过测试，是使用的修改后的数据，接下来去 MySQL 官网中求证一下。

## MySQL 官方文档的说明

MySQL 官网文档中是这样描述的，当你要更新一个列的时候，UPDATE 语句使用的是这列值的当前值。举个例子：下面这个语句从左到右顺序执行，先执行 col1 = col + 1，此时 col1 已经是加 1 后的值了，执行 col2 = col1 的时候，也是加 1 后的值。

```sql
UPDATE t1 SET col1 = col1 + 1, col2 = col1;
```

**但是，这个规则只适用于单表的 UPDATE，多表就不适用于这个规则了，多表更新，赋值语句不确保任何给定的顺序执行，可能是原值，也可能是新值。**

## MySQL 如何实现两列互换

编程语言中，实现两个变量互换很简单：引入临时变量 tmp，tmp = a，a = b，b = tmp 即可实现 a、b 互换，但是 SQL 中没有临时变量，又如何实现变量互换呢？解决方案还是使用临时变量（只不过临时变量是某数据列的值，然后后面再覆盖该数据列的值），假设有 a b 列，a = 100，b = 1，实现 a b 互换，我们可以使用通用手法：

```sql
a = a + b, 101
b = a - b, 100
a = a - b, 1
```

至此，a = 1, b = 100，实现 a、b 值互换，SQL 如下：

```sql
update t set a = a + b, b = a - b, a = a - b;
```

## MySQL 多表更新的例子

两张表：pur_po_bill_detail（采购单细表），wm_sh_bill_detail（收货单细表），采购后，先根据采购单细表创建收货单，然后根据收货单入库。

**pur_po_bill_detail（采购单细表）**

```sql
CREATE TABLE `pur_po_bill_detail` (
  `sid` int(32) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `bill_id` bigint(64) DEFAULT NULL COMMENT 'po单号id',
  `bill_no` varchar(100) DEFAULT NULL COMMENT '订单号',
  `pw_count` decimal(20,4) DEFAULT NULL COMMENT '已入库数量',
  `th_count` decimal(20,4) DEFAULT NULL COMMENT '不合格数量',
  `bill_status` varchar(30) DEFAULT NULL COMMENT '状态',
  ...
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='采购订单细表';
```

**wm_sh_bill_detail（收货单细表）**

```sql
CREATE TABLE `wm_sh_bill_detail` (
  `sid` int(32) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `bill_id` bigint(64) DEFAULT NULL COMMENT '收货单id',
  `bill_no` varchar(30) DEFAULT NULL,
  `ref_number` varchar(30) DEFAULT NULL '采购单号',
  `ref_detail_sid` bigint(20) DEFAULT NULL '采购单行项目sid',
  `sh_count` decimal(20,4) DEFAULT NULL,
  `in_count` decimal(20,4) DEFAULT NULL,
  `left_count` decimal(20,4) DEFAULT NULL,
  ...
   PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='收货单细表'
```

下述sql是在收货单入库时反写采购单细表入库数量、状态。

当采购单行项目：入库数量 + 不合格退货数量 >= 订单数量，状态变成已入库

```sql
UPDATE pur_po_bill_detail t0, wm_sh_bill_detail t1
set t0.pw_count = coalesce(t0.pw_count,0) + t1.in_count, 
t0.th_count = coalesce(t0.th_count,0) + coalesce(t1.left_count,0),
t0.bill_status = case when t0.pw_count + t0.th_count >= t0.goods_count then '已入库' else t0.bill_status end
WHERE t0.sid = t1.ref_detail_sid and t1.bill_no = 'SH20180001';
```

sql执行结果失败，系mysql多表更新，在case判断时，t0.pw_count, t0.th_count取到的是原值。所以mysql多表更新需要注意：

赋值语句、case语句尽量避免依赖引用，如本案case使用了赋值语句pw_count,th_count列，所以判断就出问题啦；可通过update语句拆分来实现多表复杂更新目标。

上述update语句拆分，先更新数量，然后更新状态：

```sql
UPDATE pur_po_bill_detail t0, wm_sh_bill_detail t1
set t0.pw_count = coalesce(t0.pw_count,0) + t1.in_count, 
t0.th_count = coalesce(t0.th_count,0) + coalesce(t1.left_count,0)
WHERE t0.sid = t1.ref_detail_sid and t1.bill_no = 'SH20180001';

UPDATE pur_po_bill_detail t0, wm_sh_bill_detail t1
set t0.bill_status = case when t0.pw_count + t0.th_count >= t0.goods_count then '已入库' else t0.bill_status end
WHERE t0.sid = t1.ref_detail_sid and t1.bill_no = 'SH20180001';
```

## 再次回到业务中来

再次回到业务场景中来，如果采用券的过期时间全部更新这种方式的话，先执行 end_time 延期，再去判断是否过期，这个时候使用的 end_time 已经是修改过的了。

其实这种更新方式也没有必要，如果券延期后还是过期的，那么其实也可以不更新券的有效期，那么 SQL 就变成了下面这样的。先过滤出延期后是生效状态的券，在进行更新。

```sql
UPDATE coupon 
SET end_time = DATE_ADD(end_time, INTERVAL 35 DAY), 
status = '生效中', 
gmt_modify = NOW() 
WHERE ... 
AND DATE_ADD(end_time, INTERVAL 35 DAY) > NOW() ;
```

## MySQL 官方文档原文

If you access a column from the table to be updated in an expression, [`UPDATE`](https://dev.mysql.com/doc/refman/8.0/en/update.html) uses the current value of the column. For example, the following statement sets `col1` to one more than its current value:

```sql
UPDATE t1 SET col1 = col1 + 1;
```

The second assignment in the following statement sets `col2` to the current (updated) `col1` value, not the original `col1` value. The result is that `col1` and `col2` have the same value. This behavior differs from standard SQL.

```sql
UPDATE t1 SET col1 = col1 + 1, col2 = col1;
```

Single-table [`UPDATE`](https://dev.mysql.com/doc/refman/8.0/en/update.html) assignments are generally evaluated from left to right. For multiple-table updates, there is no guarantee that assignments are carried out in any particular order.

## 参考文档

- [谈谈mysql update语句 set顺序问题、列交换sql实现及多表更新注意事项](https://blog.csdn.net/chuangxin/article/details/84558050)
- [https://dev.mysql.com/doc/refman/5.7/en/update.html](https://dev.mysql.com/doc/refman/5.7/en/update.html)
- [https://dev.mysql.com/doc/refman/8.0/en/update.html](https://dev.mysql.com/doc/refman/8.0/en/update.html)
