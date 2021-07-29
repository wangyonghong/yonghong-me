---
layout: post
title:  "MySQL 高级用法"
category: "MySQL"
tags: ["MySQL"]
date: 2018-11-23 00:00:00
updated: 2018-11-23 00:00:00
---

> 所有数据均来源于 [https://www.yiibai.com/mysql/stored-procedure.html](https://www.yiibai.com/mysql/stored-procedure.html)

<!-- more -->

### desc

```sql
desc table_name;
```

查看表的结构，`desc` 是 `description` 的缩写

### 存储过程

```sql
DELIMITER $$

CREATE PROCEDURE get_order_by_cust(
 IN cust_no INT,
 OUT shipped INT,
 OUT canceled INT,
 OUT resolved INT,
 OUT disputed INT)
BEGIN
 -- shipped
 SELECT
            count(*) INTO shipped
        FROM
            orders
        WHERE
            customerNumber = cust_no
                AND status = 'Shipped';

 -- canceled
 SELECT
            count(*) INTO canceled
        FROM
            orders
        WHERE
            customerNumber = cust_no
                AND status = 'Canceled';

 -- resolved
 SELECT
            count(*) INTO resolved
        FROM
            orders
        WHERE
            customerNumber = cust_no
                AND status = 'Resolved';

 -- disputed
 SELECT
            count(*) INTO disputed
        FROM
            orders
        WHERE
            customerNumber = cust_no
                AND status = 'Disputed';

END $$
DELIMITER ;
```

```sql
select @shipped, @canceled, @resolved, @disputed;
```

```
+----------+-----------+-----------+-----------+
| @shipped | @canceled | @resolved | @disputed |
+----------+-----------+-----------+-----------+
|       22 |         0 |         1 |         1 |
+----------+-----------+-----------+-----------+
1 row in set (0.00 sec)
```

```sql
-- 列出您有权访问的数据库的所有存储过程
SHOW PROCEDURE STATUS;
```


```sql
-- 在特定数据库中显示存储过程
SHOW PROCEDURE STATUS WHERE db = 'yiibaidb';
```


```sql
-- 显示具有特定模式的存储过程
SHOW PROCEDURE STATUS WHERE name LIKE '%product%'
```

```sql
-- 显示特定存储过程的源代码
SHOW CREATE PROCEDURE stored_procedure_name
```

例如

```sql
SHOW CREATE PROCEDURE GetAllProducts\G
*************************** 1. row ***************************
           Procedure: GetAllProducts
            sql_mode: NO_AUTO_VALUE_ON_ZERO
    Create Procedure: CREATE DEFINER=`root`@`%` PROCEDURE `GetAllProducts`()
BEGIN
   SELECT *  FROM products;
   END
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: utf8_general_ci
1 row in set (0.00 sec)
```

### 存储函数

与存储过程不同，您可以在SQL语句中使用存储的函数，也可以在表达式中使用。 这有助于提高程序代码的可读性和可维护性。

```sql
DELIMITER $$

CREATE FUNCTION CustomerLevel(p_creditLimit double) RETURNS VARCHAR(10)
    DETERMINISTIC
BEGIN
    DECLARE lvl varchar(10);

    IF p_creditLimit > 50000 THEN
 SET lvl = 'PLATINUM';
    ELSEIF (p_creditLimit <= 50000 AND p_creditLimit >= 10000) THEN
        SET lvl = 'GOLD';
    ELSEIF p_creditLimit < 10000 THEN
        SET lvl = 'SILVER';
    END IF;

 RETURN (lvl);
END $$
DELIMITER ;


SELECT 
    customerName, CustomerLevel(creditLimit)
FROM
    customers
ORDER BY customerName LIMIT 10;


+------------------------------+----------------------------+
| customerName                 | CustomerLevel(creditLimit) |
+------------------------------+----------------------------+
| Alpha Cognac                 | PLATINUM                   |
| American Souvenirs Inc       | SILVER                     |
| Amica Models & Co.           | PLATINUM                   |
| ANG Resellers                | SILVER                     |
| Anna's Decorations, Ltd      | PLATINUM                   |
| Anton Designs, Ltd.          | SILVER                     |
| Asian Shopping Network, Co   | SILVER                     |
| Asian Treasures, Inc.        | SILVER                     |
| Atelier graphique            | GOLD                       |
| Australian Collectables, Ltd | PLATINUM                   |
+------------------------------+----------------------------+
10 rows in set (0.00 sec)

```

在存储过程中使用存储函数，提高可读性

```sql
DELIMITER $$

CREATE PROCEDURE GetCustomerLevel(
    IN  p_customerNumber INT(11),
    OUT p_customerLevel  varchar(10)
)
BEGIN
    DECLARE creditlim DOUBLE;

    SELECT creditlimit INTO creditlim
    FROM customers
    WHERE customerNumber = p_customerNumber;

    SELECT CUSTOMERLEVEL(creditlim) 
    INTO p_customerLevel;
END $$
DELIMITER ;
```
