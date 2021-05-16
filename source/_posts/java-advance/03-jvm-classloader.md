---
title: Java 进阶 03 - 类加载器和双亲委派到底是什么？
tags:
- Java进阶
- JVM
categories:
- Java进阶
date: 2021-05-15 21:00:00
updated: 2021-05-15 21:00:00
---

## 类加载子系统作用

- 类加载子系统负责从文件系统或者网络中加载 Class 文件，Class 文件在文件开头有特定的文件标识（cafebabe）
- ClassLoader 只负责 Class 文件的加载，至于它是否能够运行，则由 Execution Engine 决定
- 加载的类信息存放于一块称为方法区的内存空间。除了类的信息外，方法区还存放运行时常量池信息，可能还包含字符串字面值和数字常量（这部分常量信息是 Class 文件中常量池部分的内存映射）

<!-- more -->

## 类加载器的角色

![类加载器的角色](https://up-img.yonghong.tech/pic/2021/04/03-20-16-U6ND22-TgTnLm.png)

- class file 存放于本地硬盘上，可以理解成设计师画在纸上的模板，最终这个模板在执行的时候要加载到 JVM 中来，根据这个文件实例化出 n 个一模一样的实例
- class file 加载到 JVM 中，被称为 DNA 原数据模板，放在方法区
- 在 class 文件 -> JVM -> 最终成为原数据模板，此过程需要一个运输工具，即类加载器 Class Loader，扮演一个快递员的角色


## 类的生命周期

![类生命周期的7个步骤](https://up-img.yonghong.tech/pic/2021/04/02-20-18-01-%E7%B1%BB%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E7%9A%847%E4%B8%AA%E6%AD%A5%E9%AA%A4-r3r8RQ.png)

1. 加载（Loading）：找Class文件
2. 验证（Verification）：验证格式、依赖
3. 准备（Preparation）：静态字段、方法表
4. 解析（Resolution）：符号解析为引用
5. 初始化（Initialization）：构造器、静态变量赋值、静态代码块
6. 使用（Using）
7. 卸载（Unloading）

### Loading 阶段

1. 通过一个类的全限定名获取定义此类的二进制字节流

2. 将这个字节流所代表的的静态存储结构转化为方法区的运行时数据区

3. **在内存中生成一个代表这个类的 java.lang.Class 对象**，作为方法区这个类的各种数据的访问入口

补充：加载 class 文件的方式

- 从本地系统中直接加载
- 通过网络获取，典型场景：Web Applet
- 从 zip 压缩包中读取，成为日后 jar、war 格式的基础
- 运行时计算生成，使用最多的是：动态代理技术
- 由其他文件生成，典型场景：JSP 应用
- 从专有数据库中提取 class 文件，比较少见
- 从加密文件中获取，典型的防 class 文件被反编译的保护措施

### Linking 阶段

1.验证（Verify）：
- 目的在于确保 class 文件的字节流中包含信息符合当前虚拟机要求，保证被加载类的正确性，不会危害虚拟机的自身安全
- 主要包括四种验证：文件格式验证，元数据验证，字节码验证，符号引用验证

2.准备（Prepare）：

- 为类变量分配内存并且设置该类变量的默认初始值，即零值
- 这里不包含用 final 修饰的 static，因为 final 在编译的时候就会分配了，准备阶段会显示初始化
- 这里不会为实例变量分配初始值，类变量会分配在方法区中，而实例变量是会随着对象一起分配到 Java 堆中

3.解析（Resolve）：

- 将常量池内的符号引用转换为直接引用的过程
- 事实上，解析操作往往会伴随着 JVM 在执行完初始化之后再执行
- 符号引用就是一组符号来描述所引用的目标。符号引用的字面量形式明确定义在《Java 虚拟机规范》的 class 文件格式中。直接引用就是直接指向目标的指针、相对偏移量或者一个间接定位到目标的句柄
- 解析动作主要针对类或接口、字段、类方法、接口方法、方法类型等。对应常量池中的 CONSTANT_Class_info、CONSTANT_Fieldref_info、CONSTANT_Methodref_info 等。

### Initialization 阶段

- 初始化阶段就是执行类构造器方法 `<clinit>()` 的过程
- 此方法不需要定义，是 javac 编译器自动收集类中所有类变量的赋值动作和静态代码块中的语句合并而来
- 构造器方法中指令按语句在源文件中出现的顺序执行
- `<clinit>()` 不同于类的构造器。（关联：构造器是虚拟机视角下的 `<init>()`）
- 若该类具有父类，JVM 会保证子类的 `<clinit>()` 执行前，父类的 `clinit()` 已经执行完毕
- 虚拟机必须保证一个类的 `clinit()` 方法在多线程下被同步加载


## 类的加载时机

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

## 虚拟机自带的加载器

![3个类加载器](https://up-img.yonghong.tech/pic/2021/04/02-20-23-01-3%E4%B8%AA%E7%B1%BB%E5%8A%A0%E8%BD%BD%E5%99%A8-pnd3RO.png)

- 启动类加载器（引导类加载器，Bootstrap ClassLoader）
  - 这个类加载器使用 C/C++ 语言实现的，嵌套在 JVM 内部
  - 它用来加载 Java 的核心库（JAVA_HOME/jre/lib/rt.jar、resources.jar 或 sun.boot.class.path 路径下的内容），用于提供 JVM 自身需要的类
  - 并不继承自 java.lang.ClassLoader，没有父加载器。
  - 加载拓展类和应用程序类加载器，并指定为他们的父类加载器
  - 出于安全考虑，Bootstrap 启动类加载器只加载包名为 java、javax、sun 等开头的类
- 拓展类加载器（Extension ClassLoader）
  - Java 语言编写，由 sun.misc.Launcher$ExtClassLoader 实现
  - 派生于 ClassLoader 类
  - 父类加载器为启动类加载器
  - 从 java.ext.dirs 系统属性所指定的目录中加载类库，或从 JDK 的安装目录的 jre/lib/ext 子目录（拓展目录）下加载类库。如果用户创建的 JAR 放在此目录下，也会自动由拓展类加载器加载
- 应用程序类加载器（系统类加载器，AppClassLoader）
  - java 语言编写，由 sun.misc.Launcher$AppClassLoader 实现
  - 派生于 ClassLoader 类
  - 父类加载器为拓展类加载器
  - 他负责加载环境变量 classpath 或系统属性 java.class.path 指定路径下的类库
  - 该类加载是程序中默认的类加载器，一般来说，Java 应用的类都是由它来完成加载
  - 通过 ClassLoader$getSystemClassLoader() 方法可以获取到该类加载器


类加载器可以通过getParent获取父加载器，这并不是继承关系，如果直接继承ClassLoader自己实现一个类加载器，且不指定父加载器，他的父加载器就是AppClassLoader

任何parent为null的加载器，其父加载器为 BootstrapClassLoader

![拓展类加载器和应用类加载器](https://up-img.yonghong.tech/pic/2021/04/02-20-26-01-%E6%8B%93%E5%B1%95%E7%B1%BB%E5%8A%A0%E8%BD%BD%E5%99%A8%E5%92%8C%E5%BA%94%E7%94%A8%E7%B1%BB%E5%8A%A0%E8%BD%BD%E5%99%A8-PRIfeU.png)

## 加载器特点

### 双亲委托

Java 虚拟机对 class 文件采用的是按需加载的方式，也就是说当需要使用该类时才会将它的 class 文件加载到内存生成 class 对象。而且加载某个类的 class 文件时，Java 虚拟机采用的是双亲委派模式，即把请求交由父类处理，它是一种任务委派模式。

- 如果一个类加载器收到了类加载的请求，它并不会自己先去加载，而是把这个请求委托给父类的加载器去执行
- 如果父类加载器还存在其他父类加载器，则进一步向上委托，依次递归请求最终将到达顶层的启动类加载器
- 如果父类加载器可以完成类的加载任务，就成功返回，倘若父类加载器无法完成此加载任务，子加载器才会尝试自己去加载，这就是双亲委派机制

**优势**

- 避免类的重复加载
- 保护程序安全，防止核心 API 被随意篡改

**沙箱安全机制**

自定义 String 类，但是在加载自定义 String 类的时候会率先使用引导类加载器加载，而引导类加载器在加载过程中会率先加载 JDK 自带的文件（rt.jar 包中 java/lang/String.class），报错信息说没有 main 方法，就是因为加载的是rt.jar 包中的 String 类。这样可以保证对 Java 核心源代码的保护，这就是沙箱安全机制。

在 JVM 中表示两个 class 对象是否为同一个类存在两个必要条件：

- 类的完整类名必须一致，包括包名
- 加载这个类的 ClassLoader （指 ClassLoader 实例对象）必须相同

换句话说，在 JVM 中，即使这两个类对象（class 对象）来源于同一个 Class 文件，被同一个虚拟机所加载，但只要加载它们的 ClassLoader 实例对象不同，那么这两个类对象也是不相等的。

JVM 必须知道一个类型是由启动加载器加载的还是由用户类加载器加载的。如果一个类型是由用户类加载器加载的，那么 JVM 会将这个类加载器的一个引用作为类型信息的一部分保存在方法区中。当解析一个类型到另一个类型的引用的时候，JVM 需要保证这两个类型的类加载器是相同的。


### 负责依赖

如果一个类依赖了其他的类，那么就需要先加载依赖的类。

### 缓存加载

类加载之后，就把它缓存起来，后续从缓存中获取

## 关于 ClassLoader

ClassLoader 类，它是一个抽象类，其后所有的类加载器都继承自 ClassLoader （不包括启动类加载器）

| 方法名称                                             | 描述                                                         |
| ---------------------------------------------------- | ------------------------------------------------------------ |
| getParent()                                          | 返回该类加载器的超类加载器                                   |
| loadClass(String name)                               | 加载名称为 name 的类，返回结果为 java.lang.Class 类的实例    |
| findClass(String name)                               | 查找名称为 name 的类，返回结果为 java.lang.Class 类的实例    |
| findLoadedClass(String name)                         | 查找名称为 name 的已经被加载过的类，返回结果为 java.lang.Class 类的实例 |
| defineClass(String name, byte[] b, int off, int len) | 把字节数组 b 中的内存转换成为一个 Java 类，返回结果为 java.lang.Class 类的实例 |
| resolveClass(Class<?> c)                             | 连接指定的一个 Java 类                                       |

## 获取 ClassLoader 的途径

方式一：获取当前类的 ClassLoader

clazz.getClassLoader()

方式二：获取当前线程上下文的 ClassLoader

Thread.currentThread().getContextClassLoader()

方式三：获取系统的ClassLoader

ClassLoader.getSystemClassLoader()

方式四：获取调用者的 CLassLoader

DriverManager.getCallerClassLoader()

## 显示当前 ClassLoader 加载了哪些 Jar ？

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

## 用户自定义类加载器

- 在 Java 的日常应用程序开发中，类的加载几乎是由上述 3 种类加载器相互配合执行的，在必要时，我们还可以自定义类加载器，来定制类的加载方式
- 为什么要自定义类加载器
  - 隔离加载类
  - 修改类加载方式
  - 拓展加载源
  - 防止源码泄露

- 开发人员可以通过继承抽象类 java.lang.ClassLoader 类的方式，实现自己的类加载器，以满足一些特殊需求
- 在 JDK 1.2 之前，在自定义类加载器时，总会去继承 ClassLoader 类并重写 loadClass() 方法，从而实现自定义的类加载器类，但是在 JDK 1.2 之后已不再建议用户去覆盖 loadClass() 方法，而是建议把自定义的类加载逻辑写在 findClass() 方法中
- 在编写自定义类加载器时，如果没有太过于复杂的需求，可以直接继承 URLClassLoader 类，这样就可以避免自己去编写 findClass() 方法以及获取字节码流的方式，使自定义类加载器编写更加简单


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

## 添加类的几种方式？

1. 放到 JDK 的 lib/ext 下，或者 -Djava.ext.dirs=path
2. java -cp/classpath 或者 class 文件放到当前路径
3. 自定义 ClassLoader 加载
4. 拿到当前执行类的 ClassLoader，反射调用 addUrl 方法添加 Jar 或路径（JDK 9 之后平级了，可以使用 `Class.forName("xxx", new URLClassLoader("path"));`）

## 练习

自定义一个 Classloader，加载一个 Hello.xlass 文件，执行 hello 方法， 此文件内容是一个 Hello.class 文件所有字节(x=255-x)处理后的文件。

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
