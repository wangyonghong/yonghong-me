---
title: Java基本数据类型以及缓存池
tags:
- Java
- 基本数据累心
- 包装类
- 封装类
- 缓存池
categories:
- 学习笔记
date: 2020-10-28 11:00:00
updated: 2020-10-28 11:00:00
---

本文主要介绍了Java的8种数据类型和他们的封装类，封装类数值范围，封装类的缓存池。

## 基本数据类型

```
byte/8
char/16
short/16
int/32
float/32
long/64
double/64
boolean/~
```

boolean 只有两个值：true、false，可以使用 1 bit 来存储，但是具体大小没有明确规定。JVM 会在编译时期将 boolean 类型的数据转换为 int，使用 1 来表示 true，0 表示 false。JVM 支持 boolean 数组，但是是通过读写 byte 数组来实现的。

<!-- more -->

## 包装类型

基本类型都有对应的包装类型，基本类型与其对应的包装类型之间的赋值使用自动装箱与拆箱完成。

```java
Integer x = 2;     // 装箱 调用了 Integer.valueOf(2)
int y = x;         // 拆箱 调用了 X.intValue()
```

## 数值范围

| 类型 | 最大/小值 | 二进制 | 十进制 |
| -- | -- | -- | -- |
| Integer   | 最大值 | 0x7fffffff | 2 147 483 647 |
| Integer   | 最小值 | 0x80000000 | -2 147 483 648 |
| Long      | 最大值 | 0x7fffffffffffffffL | 9 223 372 036 854 775 807 |
| Long      | 最小值 | 0x8000000000000000L | -9 223 372 036 854 775 808 |
| Float     | 最大值 | 0x1.fffffeP+127f | 3.4028235e+38f |
| Float     | 最小值 | 0x0.000002P-126f | 1.4e-45f |
| Double    | 最大值 | 0x1.fffffffffffffP+1023 | 1.7976931348623157e+308 |
| Double    | 最小值 | 0x0.0000000000001P-1022 | 4.9e-324 |


另外 `java.math` 包中还有 `BigInteger` 和 `BigDecimal` 类型，基本上是任意精度的，极限就是你机器的上限。


```java
// 0x7fffffff = 2147483647
System.out.println(Integer.MAX_VALUE);
// 0x80000000 = -2147483648
System.out.println(Integer.MIN_VALUE);

// 0x7fffffffffffffffL = 9223372036854775807
System.out.println(Long.MAX_VALUE);
// 0x8000000000000000L = -9223372036854775808
System.out.println(Long.MIN_VALUE);

// 0x1.fffffeP+127f = 3.4028235e+38f
System.out.println(Float.MAX_VALUE);
// 0x0.000002P-126f = 1.4e-45f
System.out.println(Float.MIN_VALUE);

// 0x1.fffffffffffffP+1023 = 1.7976931348623157e+308
System.out.println(Double.MAX_VALUE);
// 0x0.0000000000001P-1022 = 4.9e-324
System.out.println(Double.MIN_VALUE);
```

## 缓存池

基本类型对应的缓冲池如下：

- boolean values true and false
- all byte values
- short values between -128 and 127
- int values between -128 and 127
- char in the range \u0000 to \u007F

在使用这些基本类型对应的包装类型时，如果该数值范围在缓冲池范围内，就可以直接使用缓冲池中的对象。

在 jdk 1.8 所有的数值类缓冲池中，Integer 的缓冲池 IntegerCache 很特殊，这个缓冲池的下界是 - 128，上界默认是 127，但是这个上界是可调的，在启动 jvm 的时候，通过 -XX:AutoBoxCacheMax=<size> 来指定这个缓冲池的大小，该选项在 JVM 初始化的时候会设定一个名为 java.lang.IntegerCache.high 系统属性，然后 IntegerCache 初始化的时候就会读取该系统属性来决定上界。

### Byte

```java
    private static class ByteCache {
        private ByteCache(){}

        static final Byte cache[] = new Byte[-(-128) + 127 + 1];

        static {
            for(int i = 0; i < cache.length; i++)
                cache[i] = new Byte((byte)(i - 128));
        }
    }
    
    public static Byte valueOf(byte b) {
        final int offset = 128;
        return ByteCache.cache[(int)b + offset];
    }
```

### Character

```java
    private static class CharacterCache {
        private CharacterCache(){}

        static final Character cache[] = new Character[127 + 1];

        static {
            for (int i = 0; i < cache.length; i++)
                cache[i] = new Character((char)i);
        }
    }
    
    public static Character valueOf(char c) {
        if (c <= 127) { // must cache
            return CharacterCache.cache[(int)c];
        }
        return new Character(c);
    }
```

### Short

```java
    private static class ShortCache {
        private ShortCache(){}

        static final Short cache[] = new Short[-(-128) + 127 + 1];

        static {
            for(int i = 0; i < cache.length; i++)
                cache[i] = new Short((short)(i - 128));
        }
    }
    
    public static Short valueOf(short s) {
        final int offset = 128;
        int sAsInt = s;
        if (sAsInt >= -128 && sAsInt <= 127) { // must cache
            return ShortCache.cache[sAsInt + offset];
        }
        return new Short(s);
    }
```

### Integer

```java
    private static class IntegerCache {
        static final int low = -128;
        static final int high;
        static final Integer[] cache;
        static Integer[] archivedCache;

        static {
            // high value may be configured by property
            int h = 127;
            String integerCacheHighPropValue =
                VM.getSavedProperty("java.lang.Integer.IntegerCache.high");
            if (integerCacheHighPropValue != null) {
                try {
                    int i = parseInt(integerCacheHighPropValue);
                    i = Math.max(i, 127);
                    // Maximum array size is Integer.MAX_VALUE
                    h = Math.min(i, Integer.MAX_VALUE - (-low) -1);
                } catch( NumberFormatException nfe) {
                    // If the property cannot be parsed into an int, ignore it.
                }
            }
            high = h;

            // Load IntegerCache.archivedCache from archive, if possible
            VM.initializeFromArchive(IntegerCache.class);
            int size = (high - low) + 1;

            // Use the archived cache if it exists and is large enough
            if (archivedCache == null || size > archivedCache.length) {
                Integer[] c = new Integer[size];
                int j = low;
                for(int k = 0; k < c.length; k++)
                    c[k] = new Integer(j++);
                archivedCache = c;
            }
            cache = archivedCache;
            // range [-128, 127] must be interned (JLS7 5.1.7)
            assert IntegerCache.high >= 127;
        }

        private IntegerCache() {}
    }
    
    public static Integer valueOf(int i) {
        if (i >= IntegerCache.low && i <= IntegerCache.high)
            return IntegerCache.cache[i + (-IntegerCache.low)];
        return new Integer(i);
    }
```

### Long

```java
    private static class LongCache {
        private LongCache(){}

        static final Long cache[] = new Long[-(-128) + 127 + 1];

        static {
            for(int i = 0; i < cache.length; i++)
                cache[i] = new Long(i - 128);
        }
    }
    
    public static Long valueOf(long l) {
        final int offset = 128;
        if (l >= -128 && l <= 127) { // will cache
            return LongCache.cache[(int)l + offset];
        }
        return new Long(l);
    }
```

