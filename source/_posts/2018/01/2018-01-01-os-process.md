---
layout: post
title: 进程调度算法典型问题练习
categories: [操作系统]
tags: [操作系统, 进程调度, 算法]
date: 2018-01-01 00:00:00
updated: 2018-01-01 00:00:00
---

# 进程调度算法典型问题练习

---

> 题目：假设一个系统中有5个进程，它们的到达时间和服务时间如表所示，忽
略I/O以及其他开销时间，若分别按FCFS,SPF,SRTF,HRRN,RR,FB(第i
级队列时间片2i-1)以及Preemptive FB(第i级队列时间片2i-1)调度算法进
行CPU调度，请给出各个进程的完成时间、周转时间、带权周转时间、
平均周转时间和平均带权周转时间

| 进程 | 到达时间 | 服务时间 |
| :--: | :--:     | :--:     |
| A    | 0        | 3        |
| B    | 2        | 6        |
| C    | 4        | 4        |
| D    | 6        | 5        |
| E    | 8        | 2        |


<!-- more -->

解：甘特图，可以使用 cmd markdown 解析下面的代码

```gantt
dateFormat SSS
	title  
	section FCFS
		A :t11, 0s, 3s
		B :t12, after t11, 6s
		C :t13, after t12, 4s
		D :t14, after t13, 5s
		E :t15, after t14, 2s
```

```gantt
dateFormat SSS
	title    
	section SPF
		A :t21, 0s, 3s
		B :t22, after t21, 6s
		E :t23, after t22, 2s
		C :t24, after t23, 4s
		D :t25, after t24, 5s
```

```gantt
dateFormat SSS
	title    
	section SRTF
		A :t31, 0s, 3s
		B :t32, after t31, 1s
		C :t33, after t32, 4s
		E :t34, after t33, 2s
		B :t35, after t34, 5s
		D :t36, after t35, 5s
```

```gantt
dateFormat SSS
	title            
	section HRRN
		A :t41, 0s, 3s
		B :t42, after t41, 6s
		C :t43, after t42, 4s
		E :t44, after t43, 2s
		D :t45, after t44, 5s
```

```gantt
dateFormat SSS
	title     
	section RR（队首优先，q = 1）
		A :t51, 0s, 2s
		B :t52, after t51, 1s
		A :t53, after t52, 1s
		B :t54, after t53, 1s
		C :t55, after t54, 1s
		B :t56, after t55, 1s
		D :t57, after t56, 1s
		C :t58, after t57, 1s
		B :t59, after t58, 1s
		E :t510, after t59, 1s
		D :t511, after t510, 1s
		C :t512, after t511, 1s
		B :t513, after t512, 1s
		E :t514, after t513, 1s
		D :t515, after t514, 1s
		C :t516, after t515, 1s
		B :t517, after t516, 1s
		C :t518, after t517, 2s
```

```gantt
dateFormat SSS
	title     
	section RR（队首优先，q = 4）
		A :t61, 0s, 3s
		B :t62, after t61, 4s
		C :t63, after t62, 4s
		D :t64, after t63, 4s
		B :t65, after t64, 2s
		E :t66, after t65, 2s
		D :t67, after t66, 1s
```

```gantt
dateFormat SSS
	title    
	section RR（刚进来的进程优先，q = 1）
		 A :t71, 0s, 2s
		 B :t72, after t71, 1s
		 A :t73, after t72, 1s
		 C :t74, after t73, 1s
		 B :t75, after t74, 1s
		 D :t76, after t75, 1s
		 C :t77, after t76, 1s
		 E :t78, after t77, 1s
		 B :t79, after t78, 1s
		 D :t710, after t79, 1s
		 C :t711, after t710, 1s
		 E :t712, after t711, 1s
		 B :t713, after t712, 1s
		 D :t714, after t713, 1s
		 C :t715, after t714, 1s
		 B :t716, after t715, 1s
		 D :t717, after t716, 1s
		 B :t718, after t717, 1s
		 D :t719, after t718, 1s
``` 

```gantt
dateFormat SSS
	title    
	section RR（刚进来的进程优先，q = 4）
		 A :t81, 0s, 3s
		 B :t82, after t81, 4s
		 C :t83, after t82, 4s
		 D :t84, after t83, 4s
		 E :t85, after t84, 2s
		 B :t86, after t85, 2s
		 D :t87, after t86, 1s
```

```gantt
dateFormat SSS
	title     
	section FB（非抢占）
		A :t91, 0s, 3s
		B :t92, after t91, 1s
		C :t93, after t92, 1s
		B :t94, after t93, 2s
		D :t95, after t94, 1s
		E :t96, after t95, 1s
		C :t97, after t96, 2s
		D :t98, after t97, 2s
		E :t99, after t98, 1s
		B :t910, after t99, 3s
		C :t911, after t910, 1s
		D :t912, after t911, 2s
```

```gantt
dateFormat SSS
	title    
	section FB（抢占）
		A :t101, 0s, 2s
		B :t102, after t101, 1s
		A :t103, after t102, 1s
		C :t104, after t103, 1s
		B :t105, after t104, 1s
		D :t106, after t105, 1s
		C :t107, after t106, 1s
		E :t108, after t107, 1s
		B :t109, after t108, 2s
		D :t1010, after t109, 2s
		C :t1011, after t1010, 2s
		E :t1012, after t1011, 1s
		B :t1013, after t1012, 2s
		D :t1014, after t1013, 2s
```

