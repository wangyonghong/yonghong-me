---
layout: post
title:  "Java8 从 循环（Loops） 到 流（Stream）"
category: "java"
tags: ["java"]
date: 2019-01-29 00:00:00
updated: 2019-01-29 00:00:00
---

这篇文章是是我看到的几篇文章的总结。

Java8 里函数式编程的特性被引入已经成为了这场游戏的转折点。是时候学习一下了。流是函数式编程引入的一大特性

<!-- more -->

![29-18-02-java8-g1eFWS](https://up-img.yonghong.tech/pic/2021/07/29-18-02-java8-g1eFWS.png)

下面我们来一起看一下流的引入能够给我们带来怎样的效果。

Let the coding begin!

首先我们有一个 Article 类，有属性 title，author，和 tags

```java
private class Article {

    private final String title;
    private final String author;
    private final List<String> tags;

    private Article(String title, String author, List<String> tags) {
        this.title = title;
        this.author = author;
        this.tags = tags;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public List<String> getTags() {
        return tags;
    }
}
```

下面每一个示例都包含传统的 for 循环和新的 stream 的用法

#### 1.找出集合中第一篇包含标签 "Java" 的文章

传统 for 循环

```java
public Article getFirstJavaArticle() {

    for (Article article : articles) {
        if (article.getTags().contains("Java")) {
            return article;
        }
    }

    return null;
}
```

现在我们来用 Stream Api 尝试一下

```java
public Optional<Article> getFirstJavaArticle() {  
    return articles.stream()
        .filter(article -> article.getTags().contains("Java"))
        .findFirst();
}
```

是不是很 cool，首先我们使用 filter 来筛选出 tags 中包含 "Java" 的文章，然后我们用 findFirst() 来找出第一个出现的。实际上流是很懒的，他只需要找出一个来，后面就不再处理了。

#### 2.现在我们要匹配所有的元素，而不仅仅是第一个了。

首先，传统的 for 循环

```java
public List<Article> getAllJavaArticles() {

    List<Article> result = new ArrayList<>();

    for (Article article : articles) {
        if (article.getTags().contains("Java")) {
            result.add(article);
        }
    }

    return result;
}
```

Stream 操作

```java
public List<Article> getAllJavaArticles() {  
    return articles.stream()
        .filter(article -> article.getTags().contains("Java"))
        .collect(Collectors.toList());
}
```

cool，几乎和上面一样的操作，而且我们并不需要显式的声明一个 List，并且在符合条件的时候 add。Stream 提供了一个非常优雅的收集符合条件元素的办法 collect(Collectors.toList())。

到目前为止还没有很惊艳的操作，我们来尝试一下更加惊艳的操作！

#### 3.根据作者分组

首先还是传统的办法

```java
public Map<String, List<Article>> groupByAuthor() {

    Map<String, List<Article>> result = new HashMap<>();

    for (Article article : articles) {
        if (result.containsKey(article.getAuthor())) {
            result.get(article.getAuthor()).add(article);
        } else {
            ArrayList<Article> articles = new ArrayList<>();
            articles.add(article);
            result.put(article.getAuthor(), articles);
        }
    }

    return result;
}
```

那我们能不能用 Stream 做的更简单呢

```java
public Map<String, List<Article>> groupByAuthor() {  
    return articles.stream()
        .collect(Collectors.groupingBy(Article::getAuthor));
} 
```

炒鸡棒啊，我们用了 groupingBy() 和 getAuthor 这个引用，就完成了这么复杂的操作并且简洁清晰，可读。

#### 4.获取所有的标签

for 循环

```java
public Set<String> getDistinctTags() {

    Set<String> result = new HashSet<>();

    for (Article article : articles) {
        result.addAll(article.getTags());
    }

    return result;
}
```

Stream 

```java
public Set<String> getDistinctTags() {  
    return articles.stream()
        .flatMap(article -> article.getTags().stream())
        .collect(Collectors.toSet());
}
```

flatMap 给我们提供了一种去重的简单办法。

这仅仅是表面而已，我们还有更高级的用法，比如并行等操作。

接下来我还要继续讲解一下如何改变我们以前写的 for (int i=0;... 循环

这个东西就是 IntStream 

IntStream 是原始类型 int 的 stream。这样的好处就是减少了拆箱装箱的操作。他是 java.util.stream 包里的，当然这个包里也有处理 double, long 等类型对应的 stream。他们原理是一样的不再赘述。

#### 5.创建 IntStream 

创建 IntStream 有很多中办法

其一是使用 of()

```java
IntStream.of(1, 2, 3);  
// > 1, 2, 3
```

这样创建好之后我们可以直接使用 forEach() 打印出这些数字，就像前面说到的 Stream 的用法一样。

```java
IntStream.of(1, 2, 3).forEach(System.out::println);
```


其二是使用 range() 或者 rangeClosed()

```java
IntStream.range(1, 3);  
// > 1, 2 左闭右开
IntStream.rangeClosed(1, 3);  
// > 1, 2, 3 左闭右也闭
```

那如果我们使用偶数怎么办，也简单

```java
IntStream.iterate(0, i -> i + 2).limit(3);  
// > 0, 2, 4
```

iterate(0, i -> i + 2) 创建了一个无限流，limit(3) 限制了数量是3

最后一个要介绍的是 generate()

```java
IntStream.generate(() -> ThreadLocalRandom.current().nextInt(10)).limit(3);  
// > 4, 1, 7
```

generate() 很像 iterator，但是又不根据前一个元素去计算

#### 6.关于 IntStream 更多的玩法

使用 map()

```java
IntStream.range(1, 5).map(i -> i * i);
// > 1, 4, 9, 16
```

如果我们需要得到其他类型的流怎么办

```java
Stream<Color> stream = IntStream.range(1, 5).mapToObj(i -> getColor(i));
Stream<String> stream = IntStream.range(1,10).mapToObj(i -> "" + i);
```

Java 编程思想中作者提到，原始的 foreach 中，使用 range 会降低效率

```java
public class ForEachInt {

    public static int[] range(int start,int end,int step) {
        int sz =(end - start) / step;
        int[] result = new int[sz];
        for(int i = 0; i < sz; i++) {
            result[i] = start + (i * step);
        }
        return result;
    }

    public static int[] range(int start, int end) {
        return range(start, end, 1);
    }

    public static int[] range(int end) {
        return range(0, end);
    }

    public static void main(String[] args) {
        int n = 100000;
        Long start, end;
        start = System.currentTimeMillis();
        for (int i = 0; i < n; i++) {
        }
        end = System.currentTimeMillis();
        Long s0 = end - start;

        start = System.currentTimeMillis();
        for (int i : range(n)) {
        }
        end = System.currentTimeMillis();
        Long s1 = end - start;

        start = System.currentTimeMillis();
        IntStream.range(0, n).forEach(i -> {});
        end = System.currentTimeMillis();
        Long s2 = end - start;

        System.out.println("s0 = " + s0);
        System.out.println("s1 = " + s1);
        System.out.println("s2 = " + s2);
    }
}
```

经过测试

```
n = 100000
s0 = 1
s1 = 5
s2 = 72

n = 1000000
s0 = 3
s1 = 13
s2 = 65

n = 10000000
s0 = 4
s1 = 37
s2 = 63

n = 100000000
s0 = 3
s1 = 295
s2 = 67

n = 500000000
s0 = 3
s1 = 2921
s2 = 63
```

IntStream 一直很稳定，for(int i = 0; i < n; i++ ) 比 for(int i : range(n)) 要快很多


使用 boxed() 方法 将 IntStream 转换成 Stream<Integer>，因为 IntStream 是原始类型的 int 的 Stream

```java
Stream<Integer> stream = IntStream.range(1, 5).boxed();  
```

还可以这样，DoubleStream 和 LongStream 也是原始类型的流 double 和 long

```java
DoubleStream stream = IntStream.range(1, 5).mapToDouble(i -> i);
LongStream stream = IntStream.range(1, 5).mapToLong(i -> i);  
```

使用 anyMatch() 判断至少有一个偶数

```java
IntStream.range(1, 5).anyMatch(i -> i % 2 == 0);  
// 返回 true
```

还有 

```java
IntStream.range(1, 5).allMatch(i -> i % 2 == 0);  
// > false

IntStream.range(1, 5).noneMatch(i -> i % 2 == 0);  
// > false
```

继续 filter

```java
IntStream.range(1, 5)  
    .filter(i -> i % 2 == 0)
    .allMatch(i -> i % 2 == 0);
// > true

IntStream.range(1, 5)  
    .filter(i -> i % 2 == 0)
    .noneMatch(i -> i % 2 != 0);
// > true
```

获取最大最小值

```java
IntStream.range(1, 5).max().getAsInt();  
// > 4
IntStream.range(1, 5).min().getAsInt();  
// > 1
```
返回类型是 OptionalInt，就像是 Optional 一样，可以返回 null。这个部分单独讨论

接下来，excellent reduce function

```java
IntStream.range(1, 5).reduce(1, (x, y) -> x * y)  
// > 24 连乘
```

并行

```java
IntStream.range(1, 5).parallel().forEach(i -> heavyOperation());  
```

heavyOperation() 可以是一些费时的操作，这样就可以进行并行计算了

哇，写了这么多！

无限可能。Java11 应该更厉害

---

### 参考文献 

[Java 8: No more loops](https://www.deadcoderising.com/java-8-no-more-loops/)

[Java 8: Replace traditional for loops with IntStreams](https://www.deadcoderising.com/2015-05-19-java-8-replace-traditional-for-loops-with-intstreams/)

[https://docs.oracle.com/javase/8/docs/api/java/util/stream/package-summary.html](https://docs.oracle.com/javase/8/docs/api/java/util/stream/package-summary.html)