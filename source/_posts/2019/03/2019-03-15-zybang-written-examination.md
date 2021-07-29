---
layout: post
title:  "作业帮研发笔试"
category: "interview"
tags: ["interview", "笔试", "研发"]
date: 2019-03-15 00:00:00
updated: 2018-03-15 00:00:00
---

1.将数组中的0移到后面

<!-- more -->

```java
    private static int[] func(int[] arr) {
        int length = arr.length;
        int i = 0;
        int j = 0;
        while (i < length) {
            if ((arr[i] != 0)) {
                arr[j] = arr[i];
                j++;
            }
            i++;
        }
        while (j < length) {
            arr[j] = 0;
            j++;
        }
        return arr;
    }
```

2.求 PV，UV

```
CREATE TABLE `zybang_uv_pv` (
  `url` varchar(255) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO `zybang_uv_pv` (`url`, `uid`) VALUES
('www.zybang.com', 1),
('www.zybang.com', 2),
('www.zybang.com', 3),
('www.zybang.com', 4),
('www.zybang.com', 2),
('www.zybang.com', 3),
('zhibo.zybang.com', 1),
('zhibo.zybang.com', 3),
('zhibo.zybang.com', 4),
('zhibo.zybang.com', 5);

select * from zybang_uv_pv;
+------------------+------+
| url              | uid  |
+------------------+------+
| www.zybang.com   |    1 |
| www.zybang.com   |    2 |
| www.zybang.com   |    3 |
| www.zybang.com   |    4 |
| www.zybang.com   |    2 |
| www.zybang.com   |    3 |
| zhibo.zybang.com |    1 |
| zhibo.zybang.com |    3 |
| zhibo.zybang.com |    4 |
| zhibo.zybang.com |    5 |
+------------------+------+

输出

+------------------+----+----+
| url              | uv | pv |
+------------------+----+----+
| www.zybang.com   |  4 |  6 |
| zhibo.zybang.com |  4 |  4 |
+------------------+----+----+
```

```sql
select uv.url, uv.uv, pv.pv from 
((select url, count(distinct uid) as uv from zybang_uv_pv group by url) as uv) , 
((select url, count(uid) as pv from zybang_uv_pv group by url) as pv) 
where uv.url = pv.url 
order by uv.url asc;
```

