---
title: PostgresSQL 13 正式发布！
tags:
- release
- PostgresSQL
categories:
- release
date: 2020-09-25 20:00:00
updated: 2020-09-25 20:00:00
---

PostgreSQL 全球开发组今天宣布PostgreSQL 13正式发布，作为世界上最先进的开源数据库，PostgresSQL 13是目前的最新版本。

PostgreSQL 13 在索引和查找方面进行了重大改进，有利于大型数据库系统，同时包括索引的空间节省和性能提高，使用聚合或分区的查询时的更快响应，使用增强的统计信息时更优化的查询计划，以及很多其他改进。

<!-- more -->
PostgreSQL 13除了具有强烈要求的功能（如并行清理和增量排序）外，还为不同大小的负载提供了更好的数据管理体验。此版本针对日常管理进行了优化，为应用程序开发人员提供了更多便利，并增强了安全性。

"PostgreSQL 13展示了我们全球社区在增强世界上最先进的开源关系数据库功能方面的协作和奉献精神。"，PostgreSQL核心团队成员Peter Eisentraut说， "每个发行版所带来的创新以及其在可靠性和稳定性方面的声誉，这是为什么越来越多的人选择在其应用程序中使用PostgreSQL的原因"。

PostgreSQL是一种创新的数据管理系统，以其可靠性和健壮性著称，得益于全球开发者社区 超过25年的开源开发，它已成为各种规模组织首选的开源关系型数据库。

### 持续的性能提升

在先前PostgreSQL版本的基础上，PostgreSQL 13可以有效地处理标准数据库索引B-tree中的重复数据。这降低了B-tree索引所需的总体使用空间，同时提高了整体查询性能。

PostgreSQL 13引入了增量排序，其中查询中来自较早步骤的已排序数据可以加快后续步骤的排序。此外，PostgreSQL现在可以使用扩展的统计信息（通过CREATE STATISTICS访问）来创建增强带有OR子句和列表中的IN/ANY查找的查询计划。

在PostgreSQL 13中，更多类型的聚合和分组可以利用PostgreSQL的高效哈希聚合功能，因为具有大聚合的查询不必完全放在内存中。带有分区表的查询性能得到了提高，因为现在有更多情况可以修剪分区并且可以直接连接分区。

### 管理优化

清理(Vacuuming)是PostgreSQL管理的重要部分，它使数据库能够在更新和删除行之后回收存储空间。尽管之前的PostgreSQL版本已经完成了减轻清理开销的工作，但是清理过程也可能带来管理上的挑战。

PostgreSQL 13通过引入索引的并行清理来继续改进清理系统。除了它提供的清理性能优势外，由于管理员可以选择要运行的并行Worker进程的数量，因此可以针对特定工作负载调整此新功能的使用。除了这些性能带来的好处之外，数据插入现在还可以触发自动清理过程。

复制槽(Replication slots)用于防止预写日志（WAL）在备库收到之前被删除，可以在PostgreSQL 13中进行调整以指定要保留的WAL文件的最大数量，并有助于避免磁盘空间不足的错误。
PostgreSQL 13还增加了更多管理员可以监视数据库活动的方式，包括从EXPLAIN查看WAL使用情况的统计信息，基于流的备份进度，以及ANALYZE命令的进度。另外，还可以使用新的pg_verifybackup命令来检查pg_basebackup命令输出的完整性。

### 便利的应用程序开发

PostgreSQL 13让使用来自不同数据源的PostgreSQL数据类型更加容易。此版本在SQL/JSON路径支持中添加了datetime()函数，该函数将有效的时间格式（例如ISO 8601字符串）转换为PostgreSQL本地类型。此外，UUID v4 生成函数gen_random_uuid()现在可以直接使用而无需安装任何扩展。
PostgreSQL的分区系统更加灵活，因为分区表完全支持逻辑复制和BEFORE行级触发器。

PostgreSQL 13中的FETCH FIRST语法现已扩展为可包含WITH TIES子句。指定时，WITH TIES包括基于ORDER BY子句的结果集中最后一行相匹配的任何其他行。

### 安全增强

PostgreSQL的扩展系统是其强大功能的关键组成部分，因为它允许开发人员扩展其功能。在以前的版本中，新的扩展只能由数据库超级用户安装。为了更轻松地利用PostgreSQL的可扩展性，PostgreSQL 13添加了"可信扩展"的概念，该概念允许数据库用户使用安装超级用户标记为"受信任"的扩展。某些内置扩展默认情况下标记为受信任，包括 pgcrypto， tablefunc， hstore等。

对于需要安全身份验证方法的应用程序，PostgreSQL 13允许客户端在使用SCRAM身份验证时要求通道绑定，并且PostgreSQL外部数据包装器(postgres_fdw)现在可以使用基于证书的身份验证。

### 关于PostgreSQL

PostgreSQL是世界上最先进的开源数据库，它的全球社区是一个由成千上万的用户、开发人员、公司或其他组织组成的。PostgreSQL起源于加利福尼亚大学伯克利分校，已经有30多年的历史，并且以无与伦比的开发速度继续发展。PostgreSQL的成熟功能不仅与顶级商业数据库系统匹配，而且在高级数据库功能、可扩展性、安全性和稳定性方面超过了它们。

### 相关链接

- [PostgreSQL 13 Released!](https://www.postgresql.org/about/news/2077/)
- [PostgreSQL 13 正式发布](http://www.postgres.cn/v2/news/viewone/1/637)