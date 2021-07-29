---
layout: post
title: String 类详解
categories: [Java]
tags: [Java, String]
date: 2018-08-29 00:00:00
updated: 2018-08-29 00:00:00
---

### String 类详解

- String 类对象是不可变的，字符串一旦创建，内容不能再变

<!-- more -->

#### String 类到底是什么

看下面的代码，可以看出 String 类就是一个字符数组，并且是 final 类型的。所以自然是不可变的。

```java
public final class String
    implements java.io.Serializable, Comparable<String>, CharSequence {
    /** The value is used for character storage. */
    private final char value[];
    
    public String concat(String str) {
        int otherLen = str.length();
        if (otherLen == 0) {
            return this;
        }
        int len = value.length;
        char buf[] = Arrays.copyOf(value, len + otherLen);
        str.getChars(buf, len);
        return new String(buf, true);
    }
}
```

但是为什么我们可以执行下面的操作呢？

```java
String str = "hello";
str += " world";
System.out.println(str);
// hello world
```

表面上看 str 确实变了啊

但实际上呢？`str += " world";` 到底发生了什么？

实际上是执行了 concat() 方法， str += " world";   =>  str.concat(" world");

```java
String str = "hello";
str.concat(" world");
System.out.println(str);
// hello
```

咦，为什么没有变

我们看上面 String 类中的 concat() 方法，仔细观察发现，他的返回值才是我们要的新字符串。

```java
String str = "hello";
str = str.concat(" world");
System.out.println(str);
// hello world
```

由此看来 String 类的对象确实没有变，在执行 `str += " world";`  实际上是执行了 `str = str.concat(" world");` 新的字符串地址被赋给了 str。

#### Java 中为了效率考虑

- 以 "" 包括的字符串，只要内容相同
  - 顺序、大小写相同
- 无论在程序代码中出现几次，JVM 都只会建立一个实例
- 放在字符串池（String Pool）中维护



#### 使用不同方式创建字符串

如下图所示，

name1 和 name2 是相等的，因为 name1 和 name2 都是指向字符串池的一个字符串。

name3 和 name4 是不相等的，因为有了 new 关键字，new 是什么呢？new 是动态分配内存，因此 name3 和 name4 是在内存里的两个字符串，自然指向的地址是不同的。



![](https://up-img.yonghong.tech/pic/2021/07/29-17-18-sRnvsp-RINwDc.jpg)



#### 在 Java 中 String 是引用类型

- String 是 Java 库中预定义的类：java.lang.String
- String 对象有很多构造方法，这里列举几个常用的构造方法。

| 构造器                                         | 说明                                 | 示例                                                         |
| ---------------------------------------------- | ------------------------------------ | ------------------------------------------------------------ |
| String()                                       | 创建一个空字符串对象                 | String str = new String();                                   |
| String(String original)                        | 用字符串直接创建新字符串对象         | String str = new String("hello");                            |
| String(char value[])                           | 用字符数组创建一个字符串             | char[] charArray = {'h', 'e', 'l', 'l', 'o'};<br />String str = new String(charArray); |
| String(byte bytes[])                           | 用字节数组创建一个字符串             | byte[] byteArray = {104, 101, 108, 108, 111};<br />String str = new String(byteArray); |
| String(byte bytes[], <br />String charsetName) | 用字节数组和指定字符集创建一个字符串 | String str = <br />new String(str.getBytes("gbk"), "gb2312"); |

#### 字符串常用方法

| 方法                       | 说明                                                         |
| -------------------------- | ------------------------------------------------------------ |
| length()                   | 获取字符串中的字符个数                                       |
| charAt(index)              | 返回字符串中指定下标的字符                                   |
| concat(str)                | 拼接字符串，返回一个**新**字符串对象                         |
| toUpperCase()              | 返回一个**新**字符串，所有字母大写                           |
| toLowerCase()              | 返回一个**新**字符串，所有字母小写                           |
| trim()                     | 返回一个**新**字符串，去掉两边空格                           |
| char[] toCharArray()       | 将此字符串转换为一个**新**的字符数组                         |
| equals(str)                | 逐字符比较，相等返回 true，不相等返回 false                  |
| equalsIgnoewCase(str)      | 忽略大小写比较                                               |
| compareTo(str)             | 根据比较大小分别返回小于0，0，大于0的整数                    |
| compareToIgnoreCase(str)   | 忽略大小写比较                                               |
| startsWith(prefix)         | 如果字符以特定前缀开始，返回 true                            |
| endsWith(suffix)           | 如果字符以特定后缀结束，返回 true                            |
| contains(str)              | 如果 str 是字符串的子字符串，返回 true                       |
| indexOf(ch)                | 返回字符串中出现的第一个字符 ch 下标，没有匹配返回 -1        |
| indexOf(ch, fromIndex)     | 返回字符串中 fromIndex 之后出现的第一个 ch 下标，无匹配返回 -1 |
| indexOf(s)                 | 返回字符串中出现的第一个字符串 s 的下标，无匹配返回 -1       |
| indexOf(s, fromIndex)      | 返回字符串中 fromIndex 之后出现的第一个字符串 s 的下标，无匹配返回 -1 |
| lastIndexOf(ch)            | 返回字符串中出现的最后一个字符 ch 下标，没有匹配返回 -1      |
| lastIndexOf(ch, fromIndex) | 返回字符串中 fromIndex 之前出现的最后一个字符 ch 下标，没有匹配返回 -1 |
| lastIndexOf(s)             | 返回字符串中出现的最后一个字符串 s 下标，没有匹配返回 -1     |
| lastIndexOf(s, fromIndex)  | 返回字符串中 fromIndex 之前出现的最后一个字符串 s 下标，没有匹配返回 -1 |
| substring(begin)           | 返回该字符串的子字符串，从 begin 下标到字符串的结尾          |
| substring(begin, end)      | 返回该字符串的子字符串，从 begin 下标到 end-1 下标之间（左闭右开） |



#### 增强版的字符串 StringBuffer、StringBuilder

我们再来重新看这个例子

```java
String str1 = "a";
String str2 = "b";
String str3 = str1 + str2;
```

之前说过是 concat() 方法实现的，但是 concat() 效率太低了，实际上呢是这样的底层实现

```java
String str3 = new StringBuffer(String.valueOf(str1)).append(str2).toString;
```

对比一下效率

```java
public class StringDemo {

    private static long startTime, endTime;

    public static void main(String[] args) {

        final int N = 100000;

        startTime = System.currentTimeMillis();
        String str = "";
        for (int i = 0; i < N; i++) {
            str += "*";
        }
        endTime = System.currentTimeMillis();
        System.out.println(endTime - startTime + "毫秒");

        startTime = System.currentTimeMillis();
        StringBuffer stringBuffer = new StringBuffer("");
        for (int i = 0; i < N; i++) {
            stringBuffer.append("*");
        }
        endTime = System.currentTimeMillis();
        System.out.println(endTime - startTime + "毫秒");
    }
}

// N = 100000
// 5324毫秒
// 2毫秒
// N = 500000
// 49577毫秒
// 9毫秒
```

####StringBuffer、StringBuilder

StringBuffer、StringBuilder 用法上几乎是相同的。

- 与 String 类不同的是，StringBuffer 和 StringBuilder 类的对象能够被多次的修改，并且不产生新的未使用对象。
- StringBuilder 类在 Java 5 中被提出，它和 StringBuffer 之间的最大不同在于 StringBuilder 的方法不是线程安全的（不能同步访问）。

| 构造方法                   | 说明                                     |
| -------------------------- | ---------------------------------------- |
| StringBuffer()             | 构建一个默认缓存为16的 StringBuffer 对象 |
| StringBuffer(int capacity) | 构建一个指定缓存容量的 StringBuffer 对象 |
| StringBuffer(String str)   | 构建一个指定字符串值的 StringBuffer 对象 |