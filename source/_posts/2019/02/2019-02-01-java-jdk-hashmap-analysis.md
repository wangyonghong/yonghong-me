---
layout: post
title:  "JDK 分析之 Hashmap"
category: "java"
tags: ["java"]
date: 2019-02-01 00:00:00
updated: 2019-02-01 00:00:00
---

#### JDK 1.7

先看 JDK1.7，这个版本现在可能用的少了，但是这里仍然有我们可以学习的地方。

<!-- more -->

```java
static final int DEFAULT_INITIAL_CAPACITY = 1 << 4; // aka 16
// 默认的初始化容量 - 必须是 2 的整数次幂 【】

static final int MAXIMUM_CAPACITY = 1 << 30;
// 最大的容量，当指定初始化的容量大于这个数值的时候，容量就是他了 【1】

static final float DEFAULT_LOAD_FACTOR = 0.75f;
// 默认加载因子

static final Entry<?,?>[] EMPTY_TABLE = {};
// 未初始化时的 table。HashMap 底层维护这个数组，数组中的每一项都是一个Entry。我们向 HashMap 中所放置的对象实际上是存储在该数组当中；

transient Entry<K,V>[] table = (Entry<K,V>[]) EMPTY_TABLE;
// the table，必要的时候扩容，容量必须是 2 的整数次幂

transient int size;
// 表中键值对的个数

int threshold;
// 阈值（容量*加载因子），如果 size 超过这个大小，就说明需要扩容了。初始的阈值就是初始化的容量

final float loadFactor;
// 加载因子

transient int modCount;
// 记录 hash 表结构变动的次数，这个会用在 iterator 中，HashMap fail-fast 机制。

```

【1】最大容量

```java
public HashMap(int initialCapacity, float loadFactor) {
    if (initialCapacity < 0)
        throw new IllegalArgumentException("Illegal initial capacity: " +
                                            initialCapacity);
    if (initialCapacity > MAXIMUM_CAPACITY)
        initialCapacity = MAXIMUM_CAPACITY;
    // 当自定义的容量超过了最大容量，则容量为最大容量
    if (loadFactor <= 0 || Float.isNaN(loadFactor))
        throw new IllegalArgumentException("Illegal load factor: " +
                                            loadFactor);

    this.loadFactor = loadFactor;
    threshold = initialCapacity; // 初始的阈值就是初始化的容量
    init();
    // 这里的 init()是空的，很多人不理解，init()的叫法是JDK7里面的，以后的改成了 reinitialize()。作用差不多。LinkedHashMap要维持插入顺序，为此它会把所有插入的节点（键值对）用双向链表串在一起。而在它的init()实现里，它就创建并初始化了该双向链表的头节点。之所以需要这个init()钩子，是因为HashMap是可序列化的，而反序列化方法（readObject()）是一个跟构造器性质相似、但却不是构造器的奇怪的东西。为了让子类能方便规整地实现构造初始化与反序列初始化的功能，HashMap就在构造器末尾和反序列化方法末尾都埋了这个init()钩子，这样子类就不用为这两种不同的初始化需求而重复头疼了。
    // https://www.zhihu.com/question/51095396/answer/124162684
}
```

【2】计算 hashCode

Entry 应该放在数组的哪一个位置上（这个位置通常称为位桶或者 hash 桶，即 hash 值相同的 Entry 会放在同一位置，用链表相连），是通过 key 的 hashCode 来计算的。

```java
final int hash(Object k) {
    int h = hashSeed;
    if (0 != h && k instanceof String) {
        return sun.misc.Hashing.stringHash32((String) k);
    }

    h ^= k.hashCode();

    // This function ensures that hashCodes that differ only by
    // constant multiples at each bit position have a bounded
    // number of collisions (approximately 8 at default load factor).
    // 这样计算的好处是能够让 hash 的每个位都能参与计算
    h ^= (h >>> 20) ^ (h >>> 12);
    return h ^ (h >>> 7) ^ (h >>> 4);
}
```

【3】寻找下标

通过 hash 计算出来的值将会使用 indexFor 方法找到它应该所在的 table 下标

```java
static int indexFor(int h, int length) {
    // assert Integer.bitCount(length) == 1 : "length must be a non-zero power of 2";
    return h & (length-1);
    // 相当于对 table.length 取模
    // 与运算替代模运算。用 hash & (table.length-1) 替代 hash % (table.length)
}
```

【4】hash 冲突

Hashmap里面的bucket出现了单链表的形式，散列表要解决的一个问题就是散列值的冲突问题，通常是两种方法：链表法和开放地址法。链表法就是将相同hash值的对象组织成一个链表放在hash值对应的槽位；开放地址法是通过一个探测算法，当某个槽位已经被占据的情况下继续查找下一个可以使用的槽位。java.util.HashMap采用的链表法的方式，链表是单向链表。形成单链表的核心代码如下


```java
void createEntry(int hash, K key, V value, int bucketIndex) {
    Entry<K,V> e = table[bucketIndex];
    table[bucketIndex] = new Entry<>(hash, key, value, e);
    size++;
}
```

上面方法的代码很简单，但其中包含了一个设计：系统总是将新添加的 Entry 对象放入 table 数组的 bucketIndex 索引处——如果 bucketIndex 索引处已经有了一个 Entry 对象，那新添加的 Entry 对象指向原有的 Entry 对象（产生一个 Entry 链），如果 bucketIndex 索引处没有 Entry 对象，也就是上面程序代码的 e 变量是 null，也就是新放入的 Entry 对象指向 null，也就是没有产生 Entry 链。

JDK 1.7 中出现哈希冲突后，把新的值放在头部，然后把原来的链接在后面。在扩容的时候先从第一个开始取，得到的新表如果还有哈希冲突，顺序正好相反。【11】

这里可能还会出现一个死循环的问题，详见 [https://juejin.im/post/5a66a08d5188253dc3321da0](https://juejin.im/post/5a66a08d5188253dc3321da0)


【5】put 方法


```java
public V put(K key, V value) {
    if (table == EMPTY_TABLE) {
        inflateTable(threshold); // 空表初始化【6】
    }
    if (key == null)
        return putForNullKey(value); // key 为 null 的时候 【7】
    int hash = hash(key);
    int i = indexFor(hash, table.length);
    for (Entry<K,V> e = table[i]; e != null; e = e.next) {
        Object k;
        // 如果有相同的 key，则直接替换 value，返回 oldValue
        if (e.hash == hash && ((k = e.key) == key || key.equals(k))) {
            V oldValue = e.value;
            e.value = value;
            e.recordAccess(this);
            return oldValue;
        }
    }

    // 没有相同的 key，添加 Entry 【8】
    modCount++;
    addEntry(hash, key, value, i);
    return null;
}
```

【6】初始化 hash 表

```java
private void inflateTable(int toSize) {
    // Find a power of 2 >= toSize 找到一个大于初始大小的 2 的整数次幂
    int capacity = roundUpToPowerOf2(toSize);

    threshold = (int) Math.min(capacity * loadFactor, MAXIMUM_CAPACITY + 1); // 重新计算阈值
    table = new Entry[capacity]; // 初始化空间
    initHashSeedAsNeeded(capacity);
}

final boolean initHashSeedAsNeeded(int capacity) {
    boolean currentAltHashing = hashSeed != 0;
    boolean useAltHashing = sun.misc.VM.isBooted() &&
            (capacity >= Holder.ALTERNATIVE_HASHING_THRESHOLD);
    boolean switching = currentAltHashing ^ useAltHashing;
    if (switching) {
        hashSeed = useAltHashing
            ? sun.misc.Hashing.randomHashSeed(this)
            : 0;
    }
    return switching;
}
```

【7】key 为 null

当key为null时，放到table[0]中，只能有一个 key 为 null 的键值对放到哈希表中

```java
private V getForNullKey() {
    if (size == 0) {
        return null;
    }
    for (Entry<K,V> e = table[0]; e != null; e = e.next) {
        if (e.key == null)
            return e.value;
    }
    return null;
}
```

【8】添加 Entry

当 size 大于threshold时，会发生扩容。threshold 等于 capacity*load factor。

jdk7 中 resize，只有当 size >= threshold 并且 table 中的那个槽中已经有 Entry 时，才会发生 resize。即有可能虽然 size>=threshold，但是必须等到每个槽都至少有一个 Entry 时，才会扩容。扩容容量变成 2 倍。

```java
void addEntry(int hash, K key, V value, int bucketIndex) {
    if ((size >= threshold) && (null != table[bucketIndex])) {
        resize(2 * table.length);
        hash = (null != key) ? hash(key) : 0;
        bucketIndex = indexFor(hash, table.length);
    }

    createEntry(hash, key, value, bucketIndex);
}
```

【9】为什么容量必须是 2 的整数次幂

找下标的时候，是这样的 

```java
return h & (length-1);
```

也就是说，比如容量是 16

```
16       0001 0000
15       0000 1111
h        0001 0100
index    0000 0100
```

这样的话就相当于是每一位都和1做与运算，得到的数值正好在 0-15 之间。

【10】getEntry get

get() 调用了 getEntry()

```java
final Entry<K,V> getEntry(Object key) {
    if (size == 0) {
        return null;
    }

    int hash = (key == null) ? 0 : hash(key); // 计算 hash
    for (Entry<K,V> e = table[indexFor(hash, table.length)];
            e != null;
            e = e.next) {
        Object k;
        // 遍历
        if (e.hash == hash &&
            ((k = e.key) == key || (key != null && key.equals(k))))
            return e;
    }
    return null;
}
```

【11】resize()

```java
void resize(int newCapacity) {
    Entry[] oldTable = table;
    int oldCapacity = oldTable.length;
    if (oldCapacity == MAXIMUM_CAPACITY) {
        threshold = Integer.MAX_VALUE;
        return;
    }

    Entry[] newTable = new Entry[newCapacity];
    transfer(newTable, initHashSeedAsNeeded(newCapacity));
    table = newTable;
    threshold = (int)Math.min(newCapacity * loadFactor, MAXIMUM_CAPACITY + 1);
}

void transfer(Entry[] newTable, boolean rehash) {
    int newCapacity = newTable.length;
    for (Entry<K,V> e : table) {
        while(null != e) {
            Entry<K,V> next = e.next;
            if (rehash) {
                e.hash = null == e.key ? 0 : hash(e.key);
            }
            int i = indexFor(e.hash, newCapacity);
            e.next = newTable[i];
            newTable[i] = e;
            e = next;
        }
    }
}
```

#### JDK 1.8

接下来看 JDK 1.8


```java
static final int TREEIFY_THRESHOLD = 8;

static final int UNTREEIFY_THRESHOLD = 6;

static final int MIN_TREEIFY_CAPACITY = 64;
```

JDK 1.8 中引入了红黑树这个数据结构，当哈希冲突的链表 size 大小超过 TREEIFY_THRESHOLD 的时候，就会变成红黑树，这样查找的速度就会变快。当元素被删除，红黑树节点数量小于 UNTREEIFY_THRESHOLD 的时候，就会转换成链表。

1.8 中元素从 Entry 变成了 Node

```java

static class Node<K,V> implements Map.Entry<K,V> {
    final int hash;
    final K key;
    V value;
    Node<K,V> next;
}
```

put 的操作也复杂了很多

```java
final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
                   boolean evict) {
    Node<K,V>[] tab; Node<K,V> p; int n, i;
    if ((tab = table) == null || (n = tab.length) == 0)
        n = (tab = resize()).length;
    if ((p = tab[i = (n - 1) & hash]) == null) 
        // 跟 JDK1.7 比简化了操作，取消了 indexFor 方法，扰动改为一次，JDK 1.7 是4次
        tab[i] = newNode(hash, key, value, null);
    else {
        Node<K,V> e; K k;
        if (p.hash == hash &&
            ((k = p.key) == key || (key != null && key.equals(k))))
            e = p;
        else if (p instanceof TreeNode) // 判断是树还是链表
            e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
        else {
            for (int binCount = 0; ; ++binCount) {
                // 哈希冲突而且是链表的情况下直接放在后面，反正他也要遍历一遍
                if ((e = p.next) == null) {
                    p.next = newNode(hash, key, value, null);
                    if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                        treeifyBin(tab, hash);
                    break;
                }
                if (e.hash == hash &&
                    ((k = e.key) == key || (key != null && key.equals(k))))
                    break;
                p = e;
            }
        }
        if (e != null) { // existing mapping for key
            V oldValue = e.value;
            if (!onlyIfAbsent || oldValue == null)
                e.value = value;
            afterNodeAccess(e);
            return oldValue;
        }
    }
    ++modCount;
    if (++size > threshold)
        resize();
    afterNodeInsertion(evict);
    return null;
}
```

根据期望容量cap，返回2的n次方形式的 哈希桶的实际容量 length。 返回值一般会>=cap 

```java 
static final int tableSizeFor(int cap) {
//经过下面的 或 和 位移 运算， n最终各位都是1。
    int n = cap - 1;
    n |= n >>> 1;
    n |= n >>> 2;
    n |= n >>> 4;
    n |= n >>> 8;
    n |= n >>> 16;
    //判断n是否越界，返回 2的n次方作为 table（哈希桶）的阈值
    return (n < 0) ? 1 : (n >= MAXIMUM_CAPACITY) ? MAXIMUM_CAPACITY : n + 1;
}
```

这篇文章分析的比较全 
[https://blog.csdn.net/zxt0601/article/details/77413921](https://blog.csdn.net/zxt0601/article/details/77413921)

#### JDK 11

```java
static final int tableSizeFor(int cap) {
    int n = -1 >>> Integer.numberOfLeadingZeros(cap - 1);
    return (n < 0) ? 1 : (n >= MAXIMUM_CAPACITY) ? MAXIMUM_CAPACITY : n + 1;
}
```