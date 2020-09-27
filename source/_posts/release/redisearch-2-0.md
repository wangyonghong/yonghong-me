---
title: 【release】高性能全文搜索引擎 RediSearch 2.0 正式发布！
tags:
- release
- RediSearch
- Redis
- 高性能
- 全文搜索
categories:
- release
date: 2020-09-27 23:00:00
updated: 2020-09-27 23:00:00
---

RediSearch 2.0.0 的 GA 版本现已发布，此版本在 RediSearch 1.0 的性能和可用性上进行了多项改进。这些改进需要对 API 进行一些向后的更改。具体更新内容如下：

**Highlights**

此版本改变了搜索索引与数据保持同步的方式。在 RediSearch 1.x 中，用户必须使用 FT.ADD 命令手动添加数据到索引中。在 RediSearch 2.x 中，用户的数据会根据键模式自动建立索引。

这些变化旨在提高开发人员的工作效率，并确保用户的搜索索引始终与其数据保持同步。为了支持这一点，开发团队对 API 做了一些改动。

除了简化索引之外，RediSearch 2.0 还允许用户使用 Redis cluster API 在多个 Redis shards 上扩展单个索引。

最后，RediSearch 2.x 将其索引保留在 main Redis key space 之外。官方表示，其对索引代码的改进使查询性能提高了 2.4 倍。

<!-- more -->

**Details**

- 创建索引时，必须指定前缀条件和/或过滤器。这决定了 RediSearch 将为哪些 hash 建立索引。
- 现在，有几个 RediSearch 命令可以映射到它们的 Redis  equivalents：`FT.ADD`-> `HSET`、`FT.DEL`-> `DEL`（相当于 RediSearch 1.x 中带有 DD 标志的[`FT.DEL`](https://oss.redislabs.com/redisearch/Commands/#ftdel)）、`FT.GET`-> `HGETALL`、`FT.MGET`-> `HGETALL`。
- RediSearch 索引不再驻留在 key space 中，并且索引不再保存到 RDB 中。
- 用户可以[从 RediSearch 1.x 升级到 RediSearch2.x](https://oss.redislabs.com/redisearch/master/Upgrade_to_2.0/)。

**Noteworthy changes**

- [＃1246](https://github.com/RediSearch/RediSearch/pull/1246) 适用于 `FT.AGGREGATE` APPLY 操作的 [`geodistance`](https://oss.redislabs.com/redisearch/master/Aggregations/#list_of_geo_apply_functions) 函数。
- [＃1394](https://github.com/RediSearch/RediSearch/pull/1394)：过期的文档（TTL）将从索引中删除。
- [＃1394](https://github.com/RediSearch/RediSearch/pull/1394): 进行优化，以避免在更新非索引字段时重新索引文件。
- [＃1384](https://github.com/RediSearch/RediSearch/pull/1384)：[`FT.DROPINDEX`](https://oss.redislabs.com/redisearch/Commands/#ftdropindex)，默认情况下不会删除该索引下的文档（请参见已弃用的`FT.DROP`）。
- [＃1385](https://github.com/RediSearch/RediSearch/pull/1385)：在[`FT.INFO`](https://oss.redislabs.com/redisearch/master/Commands/#ftinfo)response 中添加索引定义。
- [＃1097](https://github.com/RediSearch/RediSearch/pull/1097)：添加 Hindi snowball stemmer。
- RediSearch 2.x 需要 Redis 6.0 或更高版本。
- ......

---

## This is the GA release for RedisSearch 2.0.

This is the GA release for RedisSearch 2.0. This release includes several improvements in performance and usability over RediSearch 1.0. These improvements necessitate a few backward-breaking changes to the API.

### Highlights

For this release, we changed the way in which the search indexes are kept in sync with your data. In RediSearch 1.x, you had to manually add data to your indexes using the `FT.ADD` command. In RediSearch 2.x, your data is indexed automatically based on a key pattern.

These changes are designed to enhance developer productivity, and to ensure that
your search indexes are always kept in sync with your data. To support this, we've
made a few changes to the API.

In addition to simplifying indexing, RediSearch 2.0 allows you to scale a single index over multiple Redis shards using the Redis cluster API.

Finally, RediSearch 2.x keeps its indexes outside of the main Redis key space. Improvements to the indexing code have increased query performance 2.4x.

You can read more details in [the RediSearch 2.0 announcement blog post](https://redislabs.com/blog/introducing-redisearch-2-0/), and you can get started by checking out this [quick start blog post](https://redislabs.com/blog/getting-started-with-redisearch-2-0/).
[![architecture](https://up-img.yonghong.tech/pic/2020/09/27-16-08-newarchitecture-jhGq6x.png)](https://github.com/RediSearch/RediSearch/blob/master/docs/img/newarchitecture.png)

### Details

- When you create an index, you must specify a prefix condition and/or a filter. This determines which hashes RediSearch will index.
- Several RediSearch commands now map to their Redis equivalents: `FT.ADD` -> `HSET`, `FT.DEL` -> `DEL` (equivalent to [`FT.DEL` with the DD flag in RediSearch 1.x](https://oss.redislabs.com/redisearch/Commands/#ftdel)), `FT.GET` -> `HGETALL`, `FT.MGET` -> `HGETALL`.
- RediSearch indexes no longer reside within the key space, and the indexes are no longer saved to the RDB.
- You can [upgrade from RediSearch 1.x to RediSearch 2.x](https://oss.redislabs.com/redisearch/master/Upgrade_to_2.0/).

### Noteworthy changes

- [#1246](https://github.com/RediSearch/RediSearch/pull/1246): [`geodistance`](https://oss.redislabs.com/redisearch/master/Aggregations/#list_of_geo_apply_functions) function for `FT.AGGREGATE` APPLY operation.
- [#1394](https://github.com/RediSearch/RediSearch/pull/1394): Expired documents (TTL) will be removed from the index.
- [#1394](https://github.com/RediSearch/RediSearch/pull/1394): [Optimization](https://oss.redislabs.com/redisearch/master/Configuring/#partial_indexed_docs) to avoid reindexing documents when non-indexed fields are updated.
- After [index creation](https://oss.redislabs.com/redisearch/Commands/#ftcreate), an initial scan starts for existing documents. You can check the status of this scan by calling [`FT.INFO`](https://oss.redislabs.com/redisearch/Commands/#ftinfo) and looking at the `indexing` and `percent_indexed` values. While `indexing` is true, queries return partial results.
- [#1435](https://github.com/RediSearch/RediSearch/pull/1435): `NOINITIALINDEX` flag on [`FT.CREATE`](https://oss.redislabs.com/redisearch/Commands/#ftcreate) to skip the initial scan of documents on index creation.
- [#1401](https://github.com/RediSearch/RediSearch/pull/1401): Support upgrade from v1.x and for reading RDB's created by RediSearch 1.x ([more information](https://oss.redislabs.com/redisearch/master/Upgrade_to_2.0/)).
- [#1445](https://github.com/RediSearch/RediSearch/pull/1445): Support for load event. This event indexes documents when they are loaded from RDB, ensuring that indexes are fully available when RDB loading is complete (available from Redis 6.0.7 and above).
- [#1384](https://github.com/RediSearch/RediSearch/pull/1384): [`FT.DROPINDEX`](https://oss.redislabs.com/redisearch/Commands/#ftdropindex), which by default does not delete documents underlying the index (see deprecated `FT.DROP`).
- [#1385](https://github.com/RediSearch/RediSearch/pull/1385): Add index definition to [`FT.INFO`](https://oss.redislabs.com/redisearch/master/Commands/#ftinfo) response.
- [#1097](https://github.com/RediSearch/RediSearch/pull/1097): Add Hindi snowball stemmer.
- The `FT._LIST` command returns a list of all available indices. Note that this is a temporary command, as indicated by the `_` in the name, so it's not documented. We're working on a [`SCAN`](https://redis.io/commands/scan)-like command for databases with many indexes.
- The RediSearch version will appear in Redis as `20000`, which is equivalent to 2.0.0 in semantic versioning. Since the version of a module in Redis is numeric, we cannot explicitly add an GA flag.
- RediSearch 2.x requires Redis 6.0 or later.

### Behavior changes

Please familiarize yourself with these changes before upgrading to RediSearch 2.0:

- [#1381](https://github.com/RediSearch/RediSearch/pull/1381): `FT.SYNADD` is removed; use [`FT.SYNUPDATE`](https://oss.redislabs.com/redisearch/Commands/#ftsynupdate) instead. `FT.SYNUPDATE` requires both
  and index name and a synonym group ID. This ID can be any ASCII string.

- [#1437](https://github.com/RediSearch/RediSearch/pull/1437): Documents that expire during query execution time will not appear in the results (but might have been counted in the number of produced documents).

- [#1221](https://github.com/RediSearch/RediSearch/pull/1221): Synonyms support for lower case. This can result in a different result set on FT.SEARCH when using synonyms.

- RediSearch will not index hashes whose fields do not match an existing index schema. You can see the number of hashes not indexed using [`FT.INFO`](https://oss.redislabs.com/redisearch/Commands/#ftinfo) - `hash_indexing_failures `. The requirement for adding support for partially indexing and blocking is captured here: [#1455](https://github.com/RediSearch/RediSearch/pull/1455).

- Removed support for `NOSAVE` (for details see [v1.6 docs](https://oss.redislabs.com/redisearch/1.6/Commands/#ftadd)).

- RDB loading will take longer due to the index not being persisted.

- Field names in the [query syntax](https://oss.redislabs.com/redisearch/Query_Syntax/) are now case-sensitive.

- Deprecated commands:

  - `FT.DROP` (replaced by `FT.DROPINDEX`, which by default keeps the documents)
  - `FT.ADD` (mapped to `HSET` for backward compatibility)
  - `FT.DEL` (mapped to `DEL` for backward compatibility)
  - `FT.GET` (mapped to `HGETALL` for backward compatibility)
  - `FT.MGET` (mapped to `HGETALL` for backward compatibility)

- Removed commands:

  - `FT.ADDHASH` (no longer makes sense)
  - `FT.SYNADD` (see [#1381](https://github.com/RediSearch/RediSearch/pull/1381))
  - `FT.OPTIMIZE` (see [v1.6 docs](https://oss.redislabs.com/redisearch/1.6/Commands/#ftoptimize))

### Scaling a single index over multiple shards with the open source Redis cluster API

Previously, a single RediSearch index, and its documents, had to reside on a single shard. This meant that dataset size and throughput was bound to what a single Redis process could handle.

Redis Enterprise offered the ability to distribute documents in a clustered database and aggregate the results at query time. This fan-out and aggregation is handled by a component called the “coordinator” that is now also available under the same [Redis Source Available License] for all Redis OSS users in it's own repository [RSCoordinator](https://github.com/RediSearch/RSCoordinator).

Notes:

- The version inside Redis will be 20000 or 2.0.0 in semantic versioning. Since the version of a module in Redis is numeric, we could not add an GA flag.
- Requires Redis v6 or above.

---

## Introducing RediSearch 2.0

> RediSearch 2.0 is designed to improve the developer experience and be the most scalable version of RediSearch. Plus: it’s 2.4x faster than the previous version.

RediSearch, a real-time secondary index with full-text search capabilities for Redis, is one of the most mature and feature-rich Redis modules. It is also becoming even more popular every day—in the past few months RediSearch Docker pulls have jumped 500%! That soaring popularity has led customers to come up with a wide variety of interesting use cases ranging from [real-time inventory management](https://redislabs.com/solutions/use-cases/real-time-inventory/) to [ephemeral search](https://redislabs.com/blog/the-case-for-ephemeral-search/).

To extend that momentum, we’re now introducing the public preview of RediSearch 2.0, designed to **improve the developer experience** and be **the most scalable version of Redisearch**. RediSearch 2.0 supports Redis Labs’ [Active-Active geo-distribution](https://redislabs.com/redis-enterprise/technology/active-active-geo-distribution/) technology, is [scalable](https://redislabs.com/redis-enterprise/technology/linear-scaling-redis-enterprise/) without downtime, and includes [Redis on Flash](https://redislabs.com/redis-enterprise/technology/redis-on-flash/) support (currently in private preview). To meet those goals without negatively impacting performance, we created a brand new architecture for RediSearch 2.0—and it worked: **RediSearch 2.0 is 2.4x faster** than RediSearch 1.6. 

### Inside RediSearch 2.0’s new architecture 

Having a rich query-and-aggregation engine in your Redis database enables a wide variety of new use cases that extend well beyond caching. RediSearch lets you use Redis as your primary database in situations where you need to access data using complex queries. Even better, it preserves Redis’ world-class speed, reliability, and scalability, and doesn’t require you to add complexity to the code to let you update and index data. 

For RediSearch 2.0 we re-architected the way indices are kept in sync with the data. Instead of having to write data through the index (using the FT.ADD command), RediSearch now follows the data written in hashes and synchronously indexes it. This re-architecture comes with several changes in the API, which we discussed in a previous post when [RediSearch 2.0 Hit Its First Milestone](https://redislabs.com/blog/redisearch-2-0-hits-its-first-milestone/).

![img](https://up-img.yonghong.tech/pic/2020/09/27-16-10-redisearch-architecture-1-hBkQjU.png)

This new architecture brings two main benefits. First, it’s now easier than ever to create a secondary index on top of your existing data. You can just **add RediSearch to your existing Redis database, create an index, and start querying it**, without having to migrate your data or use new commands for adding data to the index. This drastically lowers the learning curve for new RediSearch users and lets you create indexes on your existing Redis databases—without even having to restart them.

In addition to implementing a new way to index data, we also took the index out of the keyspace. This enables Redis Enterprise’s [Active-Active technology](https://redislabs.com/redis-enterprise/technology/active-active-geo-distribution/), which is based on [conflict-free replicated data types (CRDTs)](https://redislabs.com/blog/diving-into-crdts/). Merging two inverted indices conflict-free is difficult, but Redis Labs already has [a proven](https://redislabs.com/case-studies/mutualink/) [CRDTs implementation](https://redislabs.com/videos/active-active-geo-distribution-redis-enterprise/) of Hashes. So the second big benefit of **this new architecture is making RediSearch 2.0 even more scalable**. Because RediSearch now follows Hashes and the index was moved out of the keyspace, you can now run RediSearch in an Active-Active geo-distributed database.

![img](https://up-img.yonghong.tech/pic/2020/09/27-16-10-redisearch-active-active-1-Aor8lj.png)*Active-Active technology seamlessly resolves conflicts between documents, and RediSearch updates local indices accordingly.*

A document will be replicated to all databases in the replication set in a [strongly eventual consistent manner](https://redislabs.com/docs/under-the-hood/). In each replica, RediSearch will simply follow all the updates on the Hashes, which means all indices are strongly eventual consistent as well.

### OSS cluster support for open source Redis

We didn’t want to limit increasing the scalability capabilities to only Redis Enterprise users, so we added support for scaling a single index over multiple shards with the open source Redis cluster API. Previously, a single RediSearch index, and its documents, had to reside on a single shard. This meant that dataset size and throughput for OSS Redis was bound to what a single Redis process could handle. Redis Enterprise offered the ability to distribute documents in a clustered database and aggregate the results at query time. This fan-out and aggregation is handled by a component called the “coordinator” that is now also [publicly available ](https://github.com/RedisLabsModules/RSCoordinator)under the [Redis Source Available License](https://redislabs.com/legal/licenses/) so it will work with open source Redis clusters as well as Redis Enterprise. The result is the most scalable version of RediSearch yet. 

### Show me the numbers!

To assess RediSearch 2.0’s ingestion performance, we extended our full-text search benchmark ([FTSB](https://github.com/RediSearch/ftsb)) suite with [the publicly available NYC Taxi dataset](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page). This dataset is used across the industry due to its rich set of data types (text, tag, geographic, and numeric), and a large number of documents. 

This benchmark focuses on write performance, using trip-record data of rides in yellow cabs in New York City. Specifically for this benchmark we used the January 2015 dataset, which loads more than 12 million documents with an average size of 500 bytes per document. For the full benchmark specification please refer to the [FTSB on GitHub](https://github.com/RediSearch/ftsb/blob/master/docs/nyc_taxis-benchmark/description.md).

All benchmark variations were run on Amazon Web Services instances, provisioned through our benchmark-testing infrastructure. The tests were executed on a 3-node cluster with 15 shards, with RediSearch Enterprise versions 1.6 and 2.0. Both the benchmarking client and the 3 nodes comprising the database with RediSearch enabled were running on separate c5.9xlarge instances.

Given that RediSearch 2.0 comes with the ability to follow changes in Hashes in Redis and automatically index them, we’ve added variants for the [FT.ADD](https://oss.redislabs.com/redisearch/Commands/#ftadd) and [HSET](https://redis.io/commands/hset) commands. To make upgrades easier, we remapped the now deprecated FT.ADD command to the HSET commands in RediSearch 2.0. The two charts below display overall ingestion rate and latency for both RediSearch 1.6 and RediSearch 2.0, while retaining sub-millisecond latencies.

![img](https://up-img.yonghong.tech/pic/2020/09/27-16-10-redisearch-2.0-graph-1-1024x639-pz1WCV.png)

![img](https://up-img.yonghong.tech/pic/2020/09/27-16-10-redisearch-2.0-graph-2-1024x658-EArYyF.png)

[RediSearch has always been fast](https://redislabs.com/blog/redisearch-1-6-boosts-performance-up-to-64/), but with this architectural change we’ve moved from indexing 96K documents per second to 132K docs/sec at an overall p50 ingestion latency of 0.4ms, drastically improving write scaling. 

Not only will you benefit from the boost in the throughput, but each ingestion also becomes faster. Apart from the overall ingestion improvement due to the changes in architecture, you can now also rely on the OSS Redis Cluster API capabilities to linearly scale the ingestion of your search database. 

Combining throughput and latency improvements, **RediSearch 2.0 delivers up to a 2.4X speedup** compared to the RediSearch 1.6.

### What’s next for RediSearch 2.0

To sum up, **RediSearch 2.0 is the fastest and most scalable version for all Redis users that we have ever released.** In addition, RediSearch 2.0’s new architecture improves the developer experience of creating indices for existing data within Redis in a seamless manner and removes the need to migrate your Redis data to another RediSearch-enabled database. This new architecture allows RediSearch to follow and auto-index other data structures, such as Streams or Strings. In upcoming releases, it will let you work with additional data structures such as the nested data structure in [RedisJSON](https://redislabs.com/modules/redis-json/). 

We plan to keep on adding more features to further enhance the developer experience. Coming next, look for a new command that allows you to profile your search queries to better understand where performance bottlenecks occur during query execution.

Ready to get started? Check out Tug Grall’s blog on …[ Getting Started with RediSearch 2.0](https://redislabs.com/blog/getting-started-with-redisearch-2-0/)! Then follow the steps in this [tutorial on GitHub](https://github.com/RediSearch/redisearch-getting-started) or create a free database in [Redis Enterprise Cloud Essentials](https://redislabs.com/try-free/). (Note that the public preview of RediSearch 2.0 is available in two Redis Enterprise Cloud Essentials regions: Mumbai and Oregon.)