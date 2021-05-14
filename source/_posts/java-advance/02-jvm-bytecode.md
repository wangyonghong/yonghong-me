---
title: Java 进阶 02 - 是时候了解一下 Java 字节码了
tags:
- Java进阶
- JVM
categories:
- Java进阶
date: 2021-05-14 22:00:00
updated: 2021-05-14 22:00:00
---

## 什么是字节码？

- 我们平时所说的 Java 字节码，指的是用 Java 语言编译成的字节码。准确的说能在 JVM 平台上执行的字节码格式都是一样的。所以应该统称为 JVM 字节码。
- 不同的编译器，可以编译出相同的字节码文件，字节码文件也可以在不同的 JVM 上运行。
- Java 虚拟机与 Java 语言并没有必然的联系，它只与特定的二进制文件格式 .class 文件格式所关联，.class 文件中包含了 Java 虚拟机指令集（或者称为字节码、Bytecodes）和符号表，还有一些其他的辅助信息。
- Java bytecode 由单字节（byte）的指令组成，理论上最多支持 256 个操作码（opcode）。 实际上 Java 只使用了200左右的操作码，还有一些操作码则保留给调试操作。详情见：

- [JVM 指令集对照表](https://yonghong.tech/2021/01/jvm-instruction-set/)

<!-- more -->

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

## 字节码的运行时结构

JVM 是一台基于栈的计算机器。

每个线程都有一个独属于自己的线程栈（JVM Stack），用于存储 栈帧（Frame）。 每一次方法调用，JVM 都会自动创建一个栈帧。栈帧由操作数栈，局部变量数组以及一个 Class 引用组成。Class 引用指向当前方法在运行时常量池中对应的 Class。

## 从助记符到二进制

![从助记符到二进制](https://up-img.yonghong.tech/pic/2021/04/02-20-05-%E4%BB%8E%E5%8A%A9%E8%AE%B0%E7%AC%A6%E5%88%B0%E4%BA%8C%E8%BF%9B%E5%88%B6-1rl8Dp.png)

## 四则运行的例子

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

## 算数操作与类型转换

![算数操作与类型转换](https://up-img.yonghong.tech/pic/2021/04/02-20-09-01-%E7%AE%97%E6%95%B0%E6%93%8D%E4%BD%9C%E4%B8%8E%E7%B1%BB%E5%9E%8B%E8%BD%AC%E6%8D%A2-D45qpJ.png)

## 一个完整的循环控制

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

## 方法调用的指令

- invokestatic，顾名思义，这个指令用于调用某个类的静态方法，这是方法调用指令中最快的一个。
- invokespecial, 用来调用构造函数，但也可以用于调用同一个类中的 private 方法, 以及可见的超类方法。
- invokevirtual，如果是具体类型的目标对象，invokevirtual 用于调用公共，受保护和 package 级的私有方法。
- invokeinterface，当通过接口引用来调用方法时，将会编译为 invokeinterface 指令。
- invokedynamic，JDK7 新增加的指令，是实现“动态类型语言”（Dynamically Typed Language）支持而进行的升级改进，同时也是 JDK8 以后支持 lambda 表达式的实现基础。
