---
title: Java 进阶 - JVM 核心技术
tags:
- Java进阶
- JVM
categories:
- Java进阶
date: 2021-04-03 09:00:00
updated: 2021-04-03 09:00:00
---

## JVM 基础知识

- Java 是一种面向对象、静态类型、编译执行， 有 VM/GC 和运行时、跨平台的高级语言。

<!-- more -->

![源码跨平台和二进制跨平台](https://up-img.yonghong.tech/pic/2021/04/02-19-40-%E6%BA%90%E7%A0%81%E8%B7%A8%E5%B9%B3%E5%8F%B0%E5%92%8C%E4%BA%8C%E8%BF%9B%E5%88%B6%E8%B7%A8%E5%B9%B3%E5%8F%B0-R6Uzxy.png)

- Java、C++、Rust 的区别
  - C/C++ 完全相信而且惯着程序员，让大家自行管理内存，可以编写很自由的代码，但一 不小心就会造成内存泄漏等问题，导致程序崩溃。
  - Java/Golang 完全不相信程序员，但也惯着程序员。所有的内存生命周期都由 JVM 运行 时统一管理。 在绝大部分场景下，你可以非常自由的写代码，而且不用关心内存到底是 什么情况。 内存使用有问题的时候，我们可以通过 JVM 来进行信息相关的分析诊断和 调整。 这也是本课程的目标。
  - Rust 语言选择既不相信程序员，也不惯着程序员。 让你在写代码的时候，必须清楚明白 的用 Rust 的规则管理好你的变量，好让机器能明白高效地分析和管理内存。 但是这样 会导致代码不利于人的理解，写代码很不自由，学习成本也很高。

## Java 字节码技术

### 什么是字节码？

Java bytecode 由单字节（byte）的指令组成，理论上最多支持 256 个操作码（opcode）。 实际上 Java 只使用了200左右的操作码，还有一些操作码则保留给调试操作。详情见：[JVM 指令集对照表](https://yonghong.tech/2021/01/jvm-instruction-set/)

根据指令的性质，主要分为四个大类：

1. 栈操作指令，包括与局部变量交互的指令
2. 程序流程控制指令
3. 对象操作指令，包括方法调用指令
4. 算术运算以及类型转换指令

举个简单的例子：

```java
public class HelloByteCode {
    public static void main(String[] args) {
        HelloByteCode obj = new HelloByteCode();
    }
}
```

```shell
$ javac -g HelloByteCode.java
$ javap -c -v HelloByteCode
Classfile /Users/yonghong/Coding/code-lab/gtu-java/week01/HelloByteCode.class
  Last modified 2021-1-7; size 415 bytes
  MD5 checksum 44dd68d97fffda0bd16a524fb32b983a
  Compiled from "HelloByteCode.java"
public class HelloByteCode
  minor version: 0
  major version: 52   // 52 对应 Java 8
  flags: ACC_PUBLIC, ACC_SUPER
Constant pool:        // 常量池
   #1 = Methodref          #4.#19         // java/lang/Object."<init>":()V
   #2 = Class              #20            // HelloByteCode
   #3 = Methodref          #2.#19         // HelloByteCode."<init>":()V
   #4 = Class              #21            // java/lang/Object
   #5 = Utf8               <init>
   #6 = Utf8               ()V
   #7 = Utf8               Code
   #8 = Utf8               LineNumberTable
   #9 = Utf8               LocalVariableTable
  #10 = Utf8               this
  #11 = Utf8               LHelloByteCode;
  #12 = Utf8               main
  #13 = Utf8               ([Ljava/lang/String;)V
  #14 = Utf8               args
  #15 = Utf8               [Ljava/lang/String;
  #16 = Utf8               obj
  #17 = Utf8               SourceFile
  #18 = Utf8               HelloByteCode.java
  #19 = NameAndType        #5:#6          // "<init>":()V
  #20 = Utf8               HelloByteCode
  #21 = Utf8               java/lang/Object
{
  public HelloByteCode();
    descriptor: ()V
    flags: ACC_PUBLIC
    Code:
      stack=1, locals=1, args_size=1
         0: aload_0
         1: invokespecial #1                  // Method java/lang/Object."<init>":()V
         4: return
      LineNumberTable:
        line 1: 0
      LocalVariableTable:
        Start  Length  Slot  Name   Signature
            0       5     0  this   LHelloByteCode;

  public static void main(java.lang.String[]);
    descriptor: ([Ljava/lang/String;)V
    flags: ACC_PUBLIC, ACC_STATIC
    Code:
      stack=2, locals=2, args_size=1
         0: new           #2                  // class HelloByteCode
         3: dup
         4: invokespecial #3                  // Method "<init>":()V
         7: astore_1
         8: return
      LineNumberTable:
        line 3: 0   // new 指令在源码的第 3 行
        line 4: 8   // return 指令在源码的第 4 行
      LocalVariableTable:   // 本地变量表
        Start  Length  Slot  Name   Signature
      // 起作用的行  生效范围  槽数  变量名称  变量类型签名
            0       9     0  args   [Ljava/lang/String;
            8       1     1   obj   LHelloByteCode;
}
SourceFile: "HelloByteCode.java"
```

### javac 与 javap

javac 的用法

```shell
$ javac -help
用法: javac <options> <source files>
其中, 可能的选项包括:
  -g                         生成所有调试信息
  -g:none                    不生成任何调试信息
  -g:{lines,vars,source}     只生成某些调试信息
  -nowarn                    不生成任何警告
  -verbose                   输出有关编译器正在执行的操作的消息
  -deprecation               输出使用已过时的 API 的源位置
  -classpath <路径>            指定查找用户类文件和注释处理程序的位置
  -cp <路径>                   指定查找用户类文件和注释处理程序的位置
  -sourcepath <路径>           指定查找输入源文件的位置
  -bootclasspath <路径>        覆盖引导类文件的位置
  -extdirs <目录>              覆盖所安装扩展的位置
  -endorseddirs <目录>         覆盖签名的标准路径的位置
  -proc:{none,only}          控制是否执行注释处理和/或编译。
  -processor <class1>[,<class2>,<class3>...] 要运行的注释处理程序的名称; 绕过默认的搜索进程
  -processorpath <路径>        指定查找注释处理程序的位置
  -parameters                生成元数据以用于方法参数的反射
  -d <目录>                    指定放置生成的类文件的位置
  -s <目录>                    指定放置生成的源文件的位置
  -h <目录>                    指定放置生成的本机标头文件的位置
  -implicit:{none,class}     指定是否为隐式引用文件生成类文件
  -encoding <编码>             指定源文件使用的字符编码
  -source <发行版>              提供与指定发行版的源兼容性
  -target <发行版>              生成特定 VM 版本的类文件
  -profile <配置文件>            请确保使用的 API 在指定的配置文件中可用
  -version                   版本信息
  -help                      输出标准选项的提要
  -A关键字[=值]                  传递给注释处理程序的选项
  -X                         输出非标准选项的提要
  -J<标记>                     直接将 <标记> 传递给运行时系统
  -Werror                    出现警告时终止编译
  @<文件名>                     从文件读取选项和文件名
```

javap 的用法

```shell
$ javap -help
用法: javap <options> <classes>
其中, 可能的选项包括:
  -help  --help  -?        输出此用法消息
  -version                 版本信息
  -v  -verbose             输出附加信息
  -l                       输出行号和本地变量表
  -public                  仅显示公共类和成员
  -protected               显示受保护的/公共类和成员
  -package                 显示程序包/受保护的/公共类
                           和成员 (默认)
  -p  -private             显示所有类和成员
  -c                       对代码进行反汇编
  -s                       输出内部类型签名
  -sysinfo                 显示正在处理的类的
                           系统信息 (路径, 大小, 日期, MD5 散列)
  -constants               显示最终常量
  -classpath <path>        指定查找用户类文件的位置
  -cp <path>               指定查找用户类文件的位置
  -bootclasspath <path>    覆盖引导类文件的位置
```

### 字节码的运行时结构

JVM 是一台基于栈的计算机器。

每个线程都有一个独属于自己的线程栈（JVM Stack），用于存储 栈帧（Frame）。 每一次方法调用，JVM 都会自动创建一个栈帧。栈帧由操作数栈，局部变量数组以及一个 Class 引用组成。Class 引用指向当前方法在运行时常量池中对应的 Class。

### 从助记符到二进制

![从助记符到二进制](https://up-img.yonghong.tech/pic/2021/04/02-20-05-%E4%BB%8E%E5%8A%A9%E8%AE%B0%E7%AC%A6%E5%88%B0%E4%BA%8C%E8%BF%9B%E5%88%B6-1rl8Dp.png)

### 四则运行的例子

MovingAverage.java

```java
public class MovingAverage {
    private int count = 0;
    private double sum = 0.0D;

    public void submit(double value) {
        this.count++;
        this.sum += value;
    }

    public double getAvg() {
        if (0 == this.count) {
            return sum;
        }
        return this.sum / this.count;
    }
}
```

LocalVaribleTest.java

```java
public class LocalVaribleTest {
    public static void main(String[] args) {
        MovingAverage ma = new MovingAverage();
        int num1 = 1;
        int num2 = 2;
        ma.submit(num1);
        ma.submit(num2);
        double avg = ma.getAvg();
    }
}
```

```shell
$ javap -c MovingAverage
Compiled from "MovingAverage.java"
public class MovingAverage {
  public MovingAverage();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: aload_0
       5: iconst_0
       6: putfield      #2                  // Field count:I
       9: aload_0
      10: dconst_0
      11: putfield      #3                  // Field sum:D
      14: return

  public void submit(double);
    Code:
       0: aload_0
       1: dup
       2: getfield      #2                  // Field count:I
       5: iconst_1
       6: iadd
       7: putfield      #2                  // Field count:I
      10: aload_0
      11: dup
      12: getfield      #3                  // Field sum:D
      15: dload_1
      16: dadd
      17: putfield      #3                  // Field sum:D
      20: return

  public double getAvg();
    Code:
       0: iconst_0
       1: aload_0
       2: getfield      #2                  // Field count:I
       5: if_icmpne     13
       8: aload_0
       9: getfield      #3                  // Field sum:D
      12: dreturn
      13: aload_0
      14: getfield      #3                  // Field sum:D
      17: aload_0
      18: getfield      #2                  // Field count:I
      21: i2d
      22: ddiv
      23: dreturn
}

$ javap -c LocalVaribleTest
Compiled from "LocalVaribleTest.java"
public class LocalVaribleTest {
  public LocalVaribleTest();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public static void main(java.lang.String[]);
    Code:
       0: new           #2                  // class MovingAverage
       3: dup
       4: invokespecial #3                  // Method MovingAverage."<init>":()V
       7: astore_1
       8: iconst_1
       9: istore_2
      10: iconst_2
      11: istore_3
      12: aload_1
      13: iload_2
      14: i2d   // int 转成 double 隐式转换
      15: invokevirtual #4                  // Method MovingAverage.submit:(D)V
      18: aload_1
      19: iload_3
      20: i2d
      21: invokevirtual #4                  // Method MovingAverage.submit:(D)V
      24: aload_1
      25: invokevirtual #5                  // Method MovingAverage.getAvg:()D
      28: dstore        4
      30: return
}
```

### 算数操作与类型转换

![算数操作与类型转换](https://up-img.yonghong.tech/pic/2021/04/02-20-09-01-%E7%AE%97%E6%95%B0%E6%93%8D%E4%BD%9C%E4%B8%8E%E7%B1%BB%E5%9E%8B%E8%BD%AC%E6%8D%A2-D45qpJ.png)

### 一个完整的循环控制

```java
public class ForLoopTest {
    private static int[] nums = {1, 6, 8};
    public static void main(String[] args) {
        MovingAverage ma = new MovingAverage();
        for (int num : nums) {
            ma.submit(num);
        }
        double avg = ma.getAvg();
    }
}
```

```shell
$ javap -c ForLoopTest
Compiled from "ForLoopTest.java"
public class ForLoopTest {
  public ForLoopTest();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public static void main(java.lang.String[]);
    Code:
       0: new           #2                  // class MovingAverage
       3: dup
       4: invokespecial #3                  // Method MovingAverage."<init>":()V
       7: astore_1
       8: getstatic     #4                  // Field nums:[I
      11: astore_2
      12: aload_2
      13: arraylength
      14: istore_3
      15: iconst_0                // 初始化变量 0
      16: istore        4         // 存储到本地变量表 4 槽位
      18: iload         4         // 加载 4 槽位 到操作数栈
      20: iload_3                 // 加载 int 3 到操作数栈
      21: if_icmpge     43        // 比较，如果大于等于跳转到 43 行指令
      24: aload_2
      25: iload         4
      27: iaload
      28: istore        5
      30: aload_1
      31: iload         5
      33: i2d
      34: invokevirtual #5                  // Method MovingAverage.submit:(D)V
      37: iinc          4, 1      // 4 槽位上加 1
      40: goto          18        // goto 18 行指令
      43: aload_1
      44: invokevirtual #6                  // Method MovingAverage.getAvg:()D
      47: dstore_2
      48: return

  static {};
    Code:
       0: iconst_3
       1: newarray       int
       3: dup
       4: iconst_0
       5: iconst_1
       6: iastore
       7: dup
       8: iconst_1
       9: bipush        6
      11: iastore
      12: dup
      13: iconst_2
      14: bipush        8
      16: iastore
      17: putstatic     #4                  // Field nums:[I
      20: return
}
```

### 方法调用的指令

- invokestatic，顾名思义，这个指令用于调用某个类的静态方法，这是方法调用指令中最快的一个。
- invokespecial, 用来调用构造函数，但也可以用于调用同一个类中的 private 方法, 以及可见的超类方法。
- invokevirtual，如果是具体类型的目标对象，invokevirtual 用于调用公共，受保护和 package 级的私有方法。
- invokeinterface，当通过接口引用来调用方法时，将会编译为 invokeinterface 指令。
- invokedynamic，JDK7 新增加的指令，是实现“动态类型语言”（Dynamically Typed Language）支持而进行的升级改进，同时也是 JDK8 以后支持 lambda 表达式的实现基础。

## JVM类加载器

### 类的生命周期

![类生命周期的7个步骤](https://up-img.yonghong.tech/pic/2021/04/02-20-18-01-%E7%B1%BB%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E7%9A%847%E4%B8%AA%E6%AD%A5%E9%AA%A4-r3r8RQ.png)

1. 加载（Loading）：找Class文件
2. 验证（Verification）：验证格式、依赖
3. 准备（Preparation）：静态字段、方法表
4. 解析（Resolution）：符号解析为引用
5. 初始化（Initialization）：构造器、静态变量赋值、静态代码块
6. 使用（Using）
7. 卸载（Unloading）

### 类的加载时机

1. 当虚拟机启动时，初始化用户指定的主类，就是启动执行的main方法所在的类；
2. 当遇到用一新建目标类实例的new指令时，初始化new指令的目标类，就是new一个类的时候要初始化；
3. 当遇到调用静态方法的指令时，初始化该静态方法所在的类；
4. 当遇到访问静态字段的指令时，初始化该静态字段所在的类；
5. 子类的初始化会触发父类的初始化；
6. 如果一个接口定义了default方法，那么直接实现或者间接实现该接口的类初始化，会触发该接口的初始化；
7. 使用反射API对某个类型进行反射调用时，初始化这个类，其实跟前面一样，反射调用要么是已经有实例了，要么是静态方法，都需要初始化；
8. 当初次调用MethodHandle实例时，初始化该MethodHandle指向的方法所在的类；

### 不会初始化（可能会加载）

1. 通过子类引用父类的静态字段，只会触发父类的初始化，而不会触发子类的初始化；
2. 定义对象数组，不会触发该类的初始化；
3. 常量在编译期间会存入调用类的常量池中，本质上并没有直接引用定义常量的类，不会触发定义常量所在的类；
4. 通过类名获取Class对象，不会触发类的初始化，Hello.class不会让Hello类初始化；
5. 通过Class.forName加载指定类时，如果指定参数initialize为false时，也不会触发类初始化，其实这个参数是告诉虚拟机，是否要对类进行初始化，Class.forName("jvm.Hello") 默认会加载Hello类；
6. 通过ClassLoader默认的loadClass方法，也不会触发初始化动作（加载了，但是不会初始化）；

### 三种类加载器

![3个类加载器](https://up-img.yonghong.tech/pic/2021/04/02-20-23-01-3%E4%B8%AA%E7%B1%BB%E5%8A%A0%E8%BD%BD%E5%99%A8-pnd3RO.png)

1. 启动类加载器（BootstrapClassLoader）
2. 拓展类加载器（ExtClassLoader）
3. 应用类加载器（AppClassLoader）

类加载器可以通过getParent获取父加载器，这并不是继承关系，如果直接继承ClassLoader自己实现一个类加载器，且不指定父加载器，他的父加载器就是AppClassLoader

任何parent为null的加载器，其父加载器为 BootstrapClassLoader

![拓展类加载器和应用类加载器](https://up-img.yonghong.tech/pic/2021/04/02-20-26-01-%E6%8B%93%E5%B1%95%E7%B1%BB%E5%8A%A0%E8%BD%BD%E5%99%A8%E5%92%8C%E5%BA%94%E7%94%A8%E7%B1%BB%E5%8A%A0%E8%BD%BD%E5%99%A8-PRIfeU.png)

### 加载器特点

1.双亲委托

当某个特定的类加载器在接收到加载类的请求时，首先将该加载任务发送给父加载器，若父加载器仍有父亲，则继续向上追溯，直到最高级。如果最高级父加载器能够加载到该类，则成功返回，否则由其子加载器进行加载。以此类推，如果到最后一个子加载器还不能成功加载，则抛出一个异常。作用：可以保证java核心库或第三方库的安全（防止低一级加载器加载的类覆盖高级加载器加载的类）

默认的类加载器是 AppClassLoader，当需要加载一个类的时候，我先去自己的上一级的类加载器ExtClassLoader中找找，有没有这个类，如果有直接拿来用。同样的，如果ExtClassLoader中也没有这个类，那我继续向上去BootstrapClassLoader中找，如果有直接拿来用。所以上一级已经加载了这个类，那么我这一级就不需要再加载了。

2.负责依赖

如果一个类依赖了其他的类，那么就需要先加载依赖的类。

3.缓存加载

类加载之后，就把它缓存起来，后续从缓存中获取

### 显示当前 ClassLoader 加载了哪些 Jar ？

```java
import java.lang.reflect.Field;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.ArrayList;

public class JvmClassLoaderPrintPath {

    public static void main(String[] args) {
        // 启动类加载器
        URL[] urls = sun.misc.Launcher.getBootstrapClassPath().getURLs();
        System.out.println("启动类加载器");
        for (URL url : urls) {
            System.out.println(" ===> " + url.toExternalForm());
        }

        // 拓展类加载器
        printClassLoader("拓展类加载器", JvmClassLoaderPrintPath.class.getClassLoader().getParent());
        // 应用类加载器
        printClassLoader("应用类加载器", JvmClassLoaderPrintPath.class.getClassLoader());

    }


    public static void printClassLoader(String name, ClassLoader classLoader) {
        if (classLoader != null) {
            System.out.println(name + " ClassLoader -> " + classLoader.toString());
            printUrlForClassLoader(classLoader);
        } else {
            System.out.println(name + " ClassLoader -> null");
        }
    }

    public static void printUrlForClassLoader(ClassLoader classLoader) {
        Object ucp = insightField(classLoader, "ucp");
        Object path = insightField(ucp, "path");
        ArrayList ps = (ArrayList) path;
        for (Object p : ps) {
            System.out.println(" ===> " + p.toString());
        }
    }

    private static Object insightField(Object obj, String fName) {
        try {
            Field f = null;
            if (obj instanceof URLClassLoader) {
                f = URLClassLoader.class.getDeclaredField(fName);
            } else {
                f = obj.getClass().getDeclaredField(fName);
            }
            f.setAccessible(true);
            return f.get(obj);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
```

```shell
启动类加载器
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/resources.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/rt.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/sunrsasign.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/jsse.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/jce.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/charsets.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/jfr.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/classes
拓展类加载器 ClassLoader -> sun.misc.Launcher$ExtClassLoader@6d06d69c
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/ext/sunec.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/ext/nashorn.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/ext/cldrdata.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/ext/dnsns.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/ext/localedata.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/ext/sunjce_provider.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/ext/sunpkcs11.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/ext/jaccess.jar
 ===> file:/Users/yq/.sdkman/candidates/java/8.0.275.hs-adpt/jre/lib/ext/zipfs.jar
 ===> file:/System/Library/Java/Extensions/MRJToolkit.jar
应用类加载器 ClassLoader -> sun.misc.Launcher$AppClassLoader@659e0bfd
 ===> file:/Users/yq/code/wangyonghong/code-lab/gtu-java/out/production/gtu-java/
```

### 自定义 ClassLoader

```java
public class Hello {
    public void hello() {
        System.out.println("Hello, classLoader!");
    }
}
```

通过以下方法拿到 base64

```shell
$ javac Hello.java
$ base64 Hello.class 
yv66vgAAADQAHAoABgAOCQAPABAIABEKABIAEwcAFAcAFQEABjxpbml0PgEAAygpVgEABENvZGUBAA9MaW5lTnVtYmVyVGFibGUBAAVoZWxsbwEAClNvdXJjZUZpbGUBAApIZWxsby5qYXZhDAAHAAgHABYMABcAGAEAE0hlbGxvLCBjbGFzc0xvYWRlciEHABkMABoAGwEABUhlbGxvAQAQamF2YS9sYW5nL09iamVjdAEAEGphdmEvbGFuZy9TeXN0ZW0BAANvdXQBABVMamF2YS9pby9QcmludFN0cmVhbTsBABNqYXZhL2lvL1ByaW50U3RyZWFtAQAHcHJpbnRsbgEAFShMamF2YS9sYW5nL1N0cmluZzspVgAhAAUABgAAAAAAAgABAAcACAABAAkAAAAdAAEAAQAAAAUqtwABsQAAAAEACgAAAAYAAQAAAAQAAQALAAgAAQAJAAAAJQACAAEAAAAJsgACEgO2AASxAAAAAQAKAAAACgACAAAABgAIAAcAAQAMAAAAAgAN

```

通过以下方法可以自定义ClassLoader

```java
import java.util.Base64;

/**
 * @author yonghongwang#163.com
 * @since 2021/4/2
 */
public class HelloClassLoader extends ClassLoader {
    public static void main(String[] args) {
        try {
            new HelloClassLoader().findClass("Hello").newInstance();
        } catch (InstantiationException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    @Override
    protected Class<?> findClass(String name) throws ClassNotFoundException {
        String helloBase64 = "yv66vgAAADQAHAoABgAOCQAPABAIABEKABIAEwcAFAcAFQEABjxpbml0PgEAAygpVgEABENvZGUBAA9MaW5lTnVtYmVyVGFibGUBAAVoZWxsbwEAClNvdXJjZUZpbGUBAApIZWxsby5qYXZhDAAHAAgHABYMABcAGAEAE0hlbGxvLCBjbGFzc0xvYWRlciEHABkMABoAGwEABUhlbGxvAQAQamF2YS9sYW5nL09iamVjdAEAEGphdmEvbGFuZy9TeXN0ZW0BAANvdXQBABVMamF2YS9pby9QcmludFN0cmVhbTsBABNqYXZhL2lvL1ByaW50U3RyZWFtAQAHcHJpbnRsbgEAFShMamF2YS9sYW5nL1N0cmluZzspVgAhAAUABgAAAAAAAgABAAcACAABAAkAAAAdAAEAAQAAAAUqtwABsQAAAAEACgAAAAYAAQAAAAQAAQALAAgAAQAJAAAAJQACAAEAAAAJsgACEgO2AASxAAAAAQAKAAAACgACAAAABgAIAAcAAQAMAAAAAgAN";
        byte[] bytes = decode(helloBase64);
        return defineClass(name, bytes, 0, bytes.length);
    }

    private byte[] decode(String base64) {
        return Base64.getDecoder().decode(base64);
    }
}
```

### 添加类的几种方式？

1. 放到 JDK 的 lib/ext 下，或者 -Djava.ext.dirs=path
2. java -cp/classpath 或者 class 文件放到当前路径
3. 自定义 ClassLoader 加载
4. 拿到当前执行类的 ClassLoader，反射调用 addUrl 方法添加 Jar 或路径（JDK 9 之后平级了，可以使用 `Class.forName("xxx", new URLClassLoader("path"));`）

## JVM 内存模型

### JVM 内存结构

![JVM内存结构](https://up-img.yonghong.tech/pic/2021/04/02-20-39-01-JVM%E5%86%85%E5%AD%98%E7%BB%93%E6%9E%84-OjY1mD.png)

- 每个线程只能访问自己的线程栈。
- 每个线程都不能访问（看不见）其他线程的局部变量。
- 所有原生类型的局部变量都存储在线程栈中，因此对其他线程是不可见的。
- 线程可以将一个原生变量值的副本传给另一个线程，但不能共享原生局部变量本身。
- 堆内存中包含了 Java 代码中创建的所有对象，不管是哪个线程创建的。其中也涵盖了包装类型（例如，Byte，Integer，Long等）。
- 不管是创建一个对象并将其值赋值给局部变量，还是赋值给另一个对象的成员变量，创建的对象都会被保存到堆内存中。

---

- 如果是原生数据类型的局部变量，那么它的内容就全部保留在线程栈上。 
- 如果是对象引用，则栈中的局部变量槽位中保存着对象的引用地址，而实际的对象内容保存在堆中。
- 对象的成员变量与对象本身一起存储在堆上，不管成员变量的类型是原生数据类型，还是对象引用。
- 类的静态变量则和类定义一样都保存在堆中。

---

- 总结一下：方法中使用的原生数据类型和对象引用地址在栈上存储；对象、对象成员与类定义、静态变量在堆上。
- 堆内存又称为“共享堆”，堆中的所有对象，可以被所有线程访问，只要他们能拿到对象的引用地址。
- 如果一个线程可以访问某个对象时，也就可以访问该对象的成员变量。
- 如果两个线程同时调用某个对象的同一方法，则它们都可以访问到这个对象的成员变量，但每个线程的局部变量副本是独立的。


### JVM 内存整体结构

![JVM内存整体结构](https://up-img.yonghong.tech/pic/2021/04/02-20-41-01-JVM%E5%86%85%E5%AD%98%E6%95%B4%E4%BD%93%E7%BB%93%E6%9E%84-eSeqP8.png)

- 每启动一个线程，JVM就会在栈空间栈分配对应的线程栈，比如 1MB 空间（-Xss1m） 
- 线程栈也叫做 Java 方法栈。如果使用了 JNI 方法，则会分配一个单独的本地方法栈（Native Stack） 
- 线程执行过程中，一般会有多个方法组成调用栈（Stack Trace），比如 A 调用 B，B 调用 C 。每执行到一个方法，就会创建对应的栈帧（Frame）。


### JVM 栈内存机构

![JVM栈内存结构](https://up-img.yonghong.tech/pic/2021/04/02-20-44-01-JVM%E6%A0%88%E5%86%85%E5%AD%98%E7%BB%93%E6%9E%84-Z8QlQS.png)

- 栈帧是一个逻辑上的概念，具体的大小在一个方法编写完成后基本上就能确定。 
- 比如返回值，需要有一个空间存放吧，每个局部变量都需要对应的地址空间，此外还有给指令使用的操作数栈，以及 Class 指针（标识这个栈帧对应的是哪个类的方法，指向非堆里面的 Class 对象）。

### JVM 堆内存结构

![JVM堆内存结构](https://up-img.yonghong.tech/pic/2021/04/02-20-45-01-JVM%E5%A0%86%E5%86%85%E5%AD%98%E7%BB%93%E6%9E%84-0TRoeN.png)

![jconsole内存](https://up-img.yonghong.tech/pic/2021/04/02-20-46-01-jconsole%E5%86%85%E5%AD%98-KNrKkU.png)

- 堆内存是所有线程共用的内存空间，JVM 将 Heap 内存分为年轻代（Young generation）和老年代（Old generation，也叫 Tenured）两部分。
- 年轻代还划分为3个内存池，伊甸园区（Eden space）和存活区（Survivor space），在大部分GC算法中有两个存活区（S0，S1），在我们可以观察到的任何时刻，S0和S1总有一个是空的，但一般很小，也浪费不了多少空间。
- Non-Heap本质上还是Heap，只是一般不归GC管理，里面划分为3个内存区池。
- Metaspace 以前叫持久代（永久代，Permanent generation），Java 换了个名字叫 Metaspace
- CCS Compressed Class Space，存放 class 信息的，和 Metaspace 有交叉
- Code Cache，存放 JIT 编译器编译后的本地机器代码。

### CPU 与内存行为

![计算机硬件架构](https://up-img.yonghong.tech/pic/2021/04/02-20-47-01-%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A1%AC%E4%BB%B6%E6%9E%B6%E6%9E%84-3aWMrH.png)

- CPU 乱序执行
- volatile 关键字
- 原子性操作
- 内存屏障

### Java对象模型

![Java对象模型](https://up-img.yonghong.tech/pic/2021/04/02-20-47-01-Java%E5%AF%B9%E8%B1%A1%E6%A8%A1%E5%9E%8B-K1uNvD.png)


### Java内存模型

![Java内存模型](https://up-img.yonghong.tech/pic/2021/04/02-20-47-01-Java%E5%86%85%E5%AD%98%E6%A8%A1%E5%9E%8B-G12dzM.jpg)

JMM 规范对应的是 JSR-133 Java Memory Model and Thread Specification 《Java 语言规范》 $17.4 Memory Model 章节

JMM 规范明确定义了不同的线程之间通过哪些方式，在什么时候可以看见其他线程保存到共享变量中的值；以及在必要时，如何对共享变量的访问进行同步。这样的好处是屏蔽各种硬件平台的操作系统之间的内存访问差异，实现了Java并发程序真正的跨平台。

- 所有的对象（包括内部的实例成员变量），static 变量，以及数组，都必须存放到堆内存中。
- 局部变量，方法的形参/入参，异常处理语句的入参不允许在线程之间共享，所以不受内存模型的影响。
- 多个线程同时对一个变量访问时【读取/写入】，这时候只要有某个线程执行的是写操作，那么这种现象称之为“冲突”。
- 可以被其他线程影响或感知的操作，称为线程间的交互行为，可分为：读取、写入、同步操作、外部操作等等。其中同步操作包括：对 volatile 变量的读写，对管程（monitor）的锁定与解锁，线程的起始操作与结尾操作，线程启动和结束等等。外部操作则是指对线程执行环境之外的操作，比如停止其他线程等等。
- JMM 规范的是线程间的交互操作，而不管线程内部对局部变量进行的操作。


## JVM 启动参数

- 以 - 开头为标准参数，所有的 JVM 都要实现这些参数，并且向后兼容。例，`-server`
- -D 设置系统属性。例，`-Dfile.encoding=UTF-8`
- 以 -X 开头为非标准参数，基本都是传给 JVM 的，默认 JVM 实现这些参数的功能，但是并不保证所有 JVM 实现都满足，且不保证向后兼容。可以使用 `java -X` 命令来查看当前 JVM 支持的非标准参数。例，`-Xmx8g`
- 以 -XX: 开头为非稳定参数，专门用于控制 JVM 的行为，跟具体的 JVM 实现有关，随时可能会在下个版本取消。
  - -XX: +-Flags 形式，+-是对布尔值进行开关。例，`-XX:+UseG1GC`
  - -XX: key=value 形式，指定某个选项的值。例，`-XX:MaxPermSize=256m`

1.系统属性参数

```java
-Dfile.encoding=UTF-8
-Duser.timezone=GMT+08
-Dmaven.test.skip=true
-Dio.netty.eventLoopThreads=8

// 还可以这样
System.setProperty("a", "A100");
String a = System.getProperty("a");
```

2.运行模式参数

- -server: 设置 JVM 使用 server 模式，特点是启动速度比较慢，但运行时性能和内存管理效率很高，适用于生产环境。在具有 64 位能力的 JDK 环境下将默认启用该模式，而忽略 -client 参数。
- -client: JDK1.7 之前在32位的 x86 机器上的默认值是 -client 选项。设置 JVM 使用 client 模式，特点是启动速度比较快，但运行时性能和内存管理效率不高，通常用于客户端应用程序或者 PC 应用开发和调试。此外，我们知道 JVM 加载字节码后，可以解释执行，也可以编译成本地代码再执行，所以可以配置 JVM 对字节码的处理模式。
- -Xint: 在解释模式(interpreted mode)下运行，-Xint 标记会强制 JVM 解释执行所有的字节码，这当然会降低运行速度，通常低10倍或更多。
- -Xcomp: -Xcomp 参数与 -Xint 正好相反，JVM 在第一次使用时会把所有的字节码编译成本地代码，从而带来最大程度的优化。【注意预热】
- -Xmixed: -Xmixed 是混合模式，将解释模式和编译模式进行混合使用，有 JVM 自己决定，这是 JVM 的默认模式，也是推荐模式。 我们使用 java -version 可以看到 mixed mode 等信息。

3.堆内存设置参数

- -Xmx, 指定最大堆内存。 如 -Xmx4g. 这只是限制了 Heap 部分的最大值为4g。这个内存不包括栈内存，也不包括堆外使用的内存。
- -Xms, 指定堆内存空间的初始大小。 如 -Xms4g。 而且指定的内存大小，并不是操作系统实际分配的初始值，而是GC先规划好，用到才分配。专用服务器上需要保持 –Xms 和 –Xmx 一致，否则应用刚启动可能就有好几个 FullGC。 当两者配置不一致时，堆内存扩容可能会导致性能抖动。
- -Xmn, 等价于 -XX:NewSize，使用 G1 垃圾收集器 不应该 设置该选项，在其他的某些业务场景下可以设置。官方建议设置为 -Xmx 的 1/2 ~ 1/4.
- -XX:MaxPermSize=size, 这是 JDK1.7 之前使用的。Java8 默认允许的 Meta空间无限大，此参数无效。
- -XX:MaxMetaspaceSize=size, Java8 默认不限制 Meta 空间, 一般不允许设置该选项。
- -XX:MaxDirectMemorySize=size，系统可以使用的最大堆外内存，这个参数跟 -Dsun.nio.MaxDirectMemorySize 效果相同。
- -Xss, 设置每个线程栈的字节数，影响栈的深度。 例如 -Xss1m 指定线程栈为 1MB，与-XX:ThreadStackSize=1m 等价

1. 如果什么都不配置会如何?
2. Xmx 是否与 Xms 设置相等?
3. Xmx 设置为机器内存的什么比例合适?
4. 作业: 画一下 Xmx、Xms、Xmn、Meta、DirectMemory、Xss 这些内存参数的关系

4.GC设置参数

- -XX:+UseG1GC:使用 G1 垃圾回收器 
- -XX:+UseConcMarkSweepGC:使用 CMS 垃圾回收器 
- -XX:+UseSerialGC:使用串行垃圾回收器 
- -XX:+UseParallelGC:使用并行垃圾回收器
- -XX:+UnlockExperimentalVMOptions -XX:+UseZGC // Java 11+
- -XX:+UnlockExperimentalVMOptions -XX:+UseShenandoahGC // Java 12+

各个 JVM 版本的默认 GC 是什么?

5.分析诊断参数

- -XX:+-HeapDumpOnOutOfMemoryError 选项, 当 OutOfMemoryError 产生，即内存溢出(堆内存或持久代)时，自动 Dump 堆内存。
  - 示例用法: java -XX:+HeapDumpOnOutOfMemoryError -Xmx256m ConsumeHeap
- -XX:HeapDumpPath 选项, 与 HeapDumpOnOutOfMemoryError 搭配使用, 指定内存溢出时 Dump 文件的目 录。如果没有指定则默认为启动 Java 程序的工作目录。
  - 示例用法: java -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/usr/local/ ConsumeHeap 
  - 自动 Dump 的 hprof 文件会存储到 /usr/local/ 目录下
- -XX:OnError 选项, 发生致命错误时(fatal error)执行的脚本。
  - 例如, 写一个脚本来记录出错时间, 执行一些命令, 或者 curl 一下某个在线报警的 url. 示例用法:java -XX:OnError="gdb - %p" MyApp
  - 可以发现有一个 %p 的格式化字符串，表示进程 PID。
- -XX:OnOutOfMemoryError 选项, 抛出 OutOfMemoryError 错误时执行的脚本。 
- -XX:ErrorFile=filename 选项, 致命错误的日志文件名,绝对路径或者相对路径。
- -Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=1506，远程调试

6.JavaAgent参数

Agent 是 JVM 中的一项黑科技, 可以通过无侵入方式来做很多事情，比如注入 AOP 代码，执行统计等等，权限非常大。这里简单介绍一下配置选项，详细功能需要专门来讲。

设置 agent 的语法如下:

- -agentlib:libname[=options] 启用 native 方式的 agent, 参考 LD_LIBRARY_PATH 路径。
- -agentpath:pathname[=options] 启用 native 方式的 agent。
- -javaagent:jarpath[=options] 启用外部的 agent 库, 比如 pinpoint.jar 等等。
- -Xnoagent 则是禁用所有 agent。 以下示例开启 CPU 使用时间抽样分析:
  - JAVA_OPTS="-agentlib:hprof=cpu=samples,file=cpu.samples.log"

## 第1课作业实践

1(可选)、自己写一个简单的 Hello.java，里面需要涉及基本类型，四则运行，if 和for，然后自己分析一下对应的字节码，有问题群里讨论。

2(必做)、自定义一个 Classloader，加载一个 Hello.xlass 文件，执行 hello 方法， 此文件内容是一个 Hello.class 文件所有字节(x=255-x)处理后的文件。文件群里提供。

题解

```java
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.URLDecoder;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;

/**
 * @author yonghongwang#163.com
 */
public class MyClassloader extends ClassLoader {
    public static void main(String[] args) {
        Class<?> helloClass = new MyClassloader().findClass("Hello");
        Method helloMethod = null;
        try {
            helloMethod = helloClass.getMethod("hello");
        } catch (NoSuchMethodException e) {
            e.printStackTrace();
        }
        try {
            helloMethod.invoke(helloClass.newInstance());
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        } catch (InstantiationException e) {
            e.printStackTrace();
        }
    }

    @Override
    protected Class<?> findClass(String name) {
        String path = this.getClass().getResource("Hello.xlass").getPath();
        File file;
        try {
            file = new File(URLDecoder.decode(path, "UTF-8"));
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException("failed to find path: " + path);
        }
        byte[] bytes;
        if (file.isFile() && file.exists()) {
            try (FileChannel channel = new FileInputStream(file).getChannel()) {
                ByteBuffer byteBuffer = ByteBuffer.allocate((int) channel.size());
                channel.read(byteBuffer);
                bytes = byteBuffer.array();
            } catch (IOException e) {
                throw new RuntimeException("failed to find path: " + path);
            }
        } else {
            throw new RuntimeException("failed to find path: " + path);
        }
        return defineClass(name, decode(bytes), 0, bytes.length);
    }

    /**
     * replace each byte with x->255-x
     */
    private byte[] decode(byte[] bytes) {
        for (int i = 0; i < bytes.length; i++) {
//            bytes[i] = (byte) (255 - bytes[i]);
            bytes[i] = (byte) ~bytes[i];
        }
        return bytes;
    }
}

```

3(必做)、画一张图，展示 Xmx、Xms、Xmn、Metaspache、DirectMemory、Xss 这些内存参数的关系。

4(可选)、检查一下自己维护的业务系统的 JVM 参数配置，用 jstat 和 jstack、jmap 查看一下详情，并且自己独立分析一下大概情况，思考有没有不合理的地方，如何改进。

注意:

- 1、对于线上有流量的系统，慎重使用jmap命令。
- 2、如果没有线上系统，可以自己 run 一个 web/java 项目。或者直接查看idea进程。

课堂重点知识笔记和答疑链接，请在群里找或者向班主任索要。