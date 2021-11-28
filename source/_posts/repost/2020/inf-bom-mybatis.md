---
title: MyBatis版本升级引发的线上告警回顾及原理分析
tags:
- MyBatis
categories:
- 转载
date: 2020-06-21 22:24:00
updated: 2020-06-21 22:24:00
---

## 背景

某天晚上，美团到店事业群某项系统服务正在进行常规需求的上线。因为在内部的Plus系统发布时，提示inf-bom版本需要升级，于是我们就将inf-bom版本从1.3.9.6 升级至1.4.2.1，如下图1所示：

![图1 版本升级](https://up-img.yonghong.tech/pic/2020/06/21-00-25-6e8a4a27586831fe9ee04855c2bd69ff150501-kgRRpZ.png)

图1 版本升级


不过，当服务上线后，开始陆续出现了一些更新系统交互日志方面的报警，这属于系统的辅助流程，报警如下方代码所示。我们发现都是跟MyBatis相关的报警，说明在进行类型转换的时候，系统产生了强转错误。

{% raw %}

```json
更新开票请求返回日志, id:{#######}, response:{{"code":XXX,"data":{"callType":3,"code":XXX,"msg":"XXXX","shopId":XXXXX,"taxPlateDockType":"XXXXXXX"},"msg":"XXXXX","success":XXXX}}
nested execption is org.apache.ibatis.type.TypeException: Could not set parameters for mapping: ParameterMapping{property='updateTime', mode=IN, javaType=class java.lang.String,
jdbcTyp=null,resultMapId='null',jdbcTypeName='null',expression='null'}.Cause org.apache.ibatis.type.TypeException,Error setting non null parameter #2 with JdbcType null. Try setting a
different Jdbc Type for this parameter or a different configuration property.Cause java.lang.ClassCastException:java.time.LocalDateTime cannot be cast to java.lang.String
```

{% endraw %}

因为报警这一块代码，属于历史功能，如果失败并不会影响主流程。但在定位期间，如果频繁报警的话，就会造成一定的干扰。因此，我们马上采取了回滚操作，将inf-bom的版本回滚至历史版本，直至报警消失，然后再进行问题的定位和分析。以下章节就是我们对报警原因的定位及原因详细分析的介绍，希望这些思路能够对大家有所启发和帮助。

<!--more-->

## 报警原因定位

在回滚完毕后，我们开始具体分析报警产生的主要原因，于是进行了以下几步的排查。

第一步，查看了报警的Mapper方法，如下代码段所示。这个是接收返回参数，根据主键id，更新具体响应内容和时间的代码，入参有3个，类型分别为long、String和LocalDateTime。

```
int updateResponse(@Param("id")long id, @Param("response")String response, @Param("updateTime")LocalDateTime updateTime);
```

第二步，我们查看了Mapper方法对应的XML文件，如下代码段所示，对应的parameterType类型是String，而实际参数的类型包括long、String以及LocalDateTime。

```
<update id="updateResponse" parameterType="java.lang.String">
UPDATE invoice_log
  SET response = #{response}, update_time = #{updateTime}
WHERE id = #{id}
</update>
```

第三步，我们查看了MyBatis上线前后的版本，报警的内容是：MyBatis在处理SQL语句时，发现不能将LocalDateTime转型为String，这一段逻辑在上线前是可以正常运行的，并且上线的业务逻辑对这段历史代码无改动。因此，我们猜测是因为inf-bom的升级，从而导致MyBatis的版本发生了变化，对某些历史功能不再支持了。MyBatis版本上线前后的变化如下表所示：

![表1 MyBatis版本升级前后对比](https://up-img.yonghong.tech/pic/2020/06/21-00-25-9e99c9850481a74c53f7c795d3dcc7bb23662-yaBNTv.png)

表1 MyBatis版本升级前后对比



第四步，我们通过第三步可以得到，在这次inf-bom的版本升级中，MyBatis的版本直接升了两个大版本，因此我们可以基本将原因猜测为MyBatis升级跨度较大，导致部分历史功能没有兼容支持，从而引起线上SQL的更新报错。

第五步，为了具体验证第四步的想法，我们通过UT的方式，将MyBatis的版本不断从3.4.6往下降，直至没有报错的位置。最终的定位是：当MyBatis版本为3.2.3时，线上代码是正常可用的，但只要升一个版本，也就是自3.2.4开始，就开始不兼容目前的用法。不过，我们当时的思路并不是很好，应该从小版本逐个往上升或者使用二分法，可以加速定位版本的效率。

最后，我们定位到了产生报警的根本问题。总的来说，MyBatis版本由inf-bom引入而来，inf-bom从3.2.3 升级到了3.4.6版本，而MyBatis自3.2.4开始就不支持目前系统内的SQL Mapper的用法，因此在升级后，线上就出现了频繁报警的问题。

问题已经定位，但是还有很多事情我们需要弄清楚。为什么版本升级后就不兼容历史的用法？具体是哪一块内容不兼容？背后的原理又是什么？下文，我们会详细进行分析。

## 详细分析

### MyBatis升级3.2.4版本的官方Release公告

首先，从报错的原因上来看，请注意这句话：“Caused by: java.lang.ClassCastException: java.lang.LocalDateTime cannot be cast to java.lang.String.”MyBatis在构建SQL语句时，发现时间字段类型LocalDateTime不能强制转为String类型。而这个SQL对应的XML配置在3.2.3的版本是可以正常使用的，那么我们先从MyBatis的Release Log上查看3.2.4版本到底发生了什么变化。

> An special remark about this feature. Previous versions ignored the “parameterType” attribute and used the actual parameter to calculate bindings. This version builds the binding information during startup and the “parameterType” attribute is used if present (though it is still optional), so in case you had a wrong value for it you will have to change it.

从官网的Release Log可以看到，MyBatis在3.2.4以前的版本，会忽略XML中的parameterType这个属性，并且使用真实的变量类型进行值的处理。但在3.2.4及以后的版本中，这个属性就被启用了，如果出现类型不匹配的话，就会出现转型失败的报错。这也提示我们开发者，在升级版本时，需要检查系统内的XML配置，使类型进行匹配，或者不设置该属性，让MyBatis自行进行计算。

根据以上内容，我们可以了解到，在版本升级后，MyBatis在构建SQL语句，在获取字段值时的逻辑发生了变化。接下来我们将通过一个简单的示例，来了解一下MyBatis在获取字段值这一块的具体代码流程是怎样的，以3.2.3版本为例。

### 以版本3.2.3为例，MyBatis构建SQL语句过程的原理分析

我们看一下配置，首先定义一个通过主键id获取学生信息的方法，仿造系统内的历史代码，我们将parameterType定义为java.lang.String，这和方法对应的参数int并不相同。

```
public StudentEntity getStudentById(@Param("id") int id);
<select id="getStudentById" parameterType="java.lang.String" resultType="entity.StudentEntity">
SELECT id,name,age FROM student WHERE id = #{id}
</select>
```

MyBatis框架要做的事情，就是在运行getStudentById(2)的时候，将 #{id}进行替换，使SQL语句变成SELECT id,name,age FROM student WHERE id = 2。MyBatis要将SQL语句完整替换成带参数值的版本，需要经历框架初始化以及实际运行时动态替换这两个部分。因为MyBatis的代码非常多，接下来我们主要阐释和本次案例相关的内容。

在框架初始化阶段，主要包括以下流程，如下图2所示：

![图2 框架初始化流程](https://up-img.yonghong.tech/pic/2020/06/21-00-25-d54db22f4d28d90be1013fe3572cb09240056-Z9sc3D.png)

图2 框架初始化流程



在框架初始化阶段，有一些组件会被构建，逐一做个简单的介绍：

- **SqlSession**：作为MyBatis工作的主要顶层API，表示和数据库交互的会话，完成必要的数据库增删改查功能。
- **数据库增删改查功能**：负责根据用户传递的parameterObject，动态地生成SQL语句，将信息封装到BoundSql对象中，并返回。
- **Configuration**：MyBatis所有的配置信息都维持在Configuration对象之中。

接下来，我们主要关注SqlSource，这个类会负责生成SQL语句，这也是本次案例中，3.2.3和3.2.4差异比较大的一个地方。下面，我们会介绍一些源码。

在构建Configuration的过程中，会涉及到构建对应每一条SQL语句对应的MappedStatement，parameterTypeClass就是根据我们在XML配置中写的parameterType转换而来，值为java.lang.String，在构建SqlSource时，传入这个参数。如下图3所示：

![图3 SqlSource依赖参数](https://up-img.yonghong.tech/pic/2020/06/21-00-25-ce0a3c80a1a969401afb9eee6ceec7a3449700-b3UtsT.png)

图3 SqlSource依赖参数



在SqlSource的构建中，parameterType参数其实是被忽略不用的，并没有继续往下传递，这跟官方的描述是一致的。因为3.2.4之前这个parameterType属性被忽略了，然后就创建了DynamicSqlSource，这个类主要是用于处理MyBatis动态SQL的类。如下图4所示：

![图4 SqlSource构建](https://up-img.yonghong.tech/pic/2020/06/21-00-25-52b982ff627457f57d190697ef38a883640529-ftNDJj.png)

图4 SqlSource构建



在框架初始化的阶段，需要介绍的内容，在3.2.3版本已经介绍完毕。当执行getStudentById方法时，MyBatis的流程如下图5所示。因受限于图片长度，我们对布局进行了一些调整：

![图5 运行流程](https://up-img.yonghong.tech/pic/2020/06/21-00-25-fcf12b094fe418ca9696ac5885094fe034877-NUYC90.png)

图5 运行流程



在具体执行阶段，也涉及到一些组件，我们需要做简单的了解：

- **SqlSession**：作为MyBatis工作的主要顶层API，表示和数据库交互的会话，完成必要数据库增删改查功能。
- **Executor**：MyBatis执行器，这是MyBatis调度的核心，负责SQL语句的生成和查询缓存的维护。
- **BoundSql**：表示动态生成的SQL语句以及相应的参数信息。
- **StatementHandler**：封装了JDBC Statement操作，负责对JDBC statement的操作，如设置参数、将Statement结果集转换成List集合等等。
- **ParameterHandler**：负责对用户传递的参数转换成JDBC Statement 所需要的参数。
- **TypeHandler**：负责Java数据类型和JDBC数据类型之间的映射和转换。

我们主要关注获取BoundSql以及参数化语句的流程，这也是3.2.3和3.2.4差异比较大的一个地方。在进入Executor的Query方法后，会首先通过对应的MappedStatement来获取BoundSql，用来帮助我们动态生成SQL语句，里面绑定了对应的SQL以及参数映射关系。在构建框架阶段，我们使用的SqlSource是DynamicSqlSource，通过这个类来生成获取BoundSql，如下图6所示：

![图6 获取BoundSql](https://up-img.yonghong.tech/pic/2020/06/21-00-25-a333daae043824092d8fdf4867732822476964-8xsurz.png)

图6 获取BoundSql



通过图6的代码，我们可以得知，parameterType在初始化阶段未被使用，而是在SQL执行时获取到的，但获取到的类型是parameterObject对应的类型，这个类是用来记录Mapper方法上对应的参数。如下图7所示，它并非在SQL配置文件中标注的java.lang.String。

![图7 parameterObject类型](https://up-img.yonghong.tech/pic/2020/06/21-00-25-016b41476d3306c2b0609aceed3c7d5a29377-LSD82q.png)

图7 parameterObject类型



然后我们通过SqlSourceBuilder的parse方法对SQL以及获取到的类型进行再次处理，其中的流程代码比较长。在这个过程中，我们主要去构建SQL的参数和Java类型的绑定关系，MyBatis依赖这个绑定关系，使用对应的TypeHandler去进行值的转换。

调用链路是`SqlSourceParser.parse -> 内部类 ParameterMappingTokenHandler.handleToken -> 私有方法 buildParameterMapping`，如下图8中的代码所示。因为当前的parameterType为MapperMethod$ParamMap，经过了多个if判断，判定当前property id的propertyType为Object.class类型。接下来，构建SQL的参数和Java类型的绑定关系ParameterMapping，再进行返回。

![图8 buildParameterMapping过程](https://up-img.yonghong.tech/pic/2020/06/21-00-25-4fc3e8c476ef995304001cbeb7c8364c727634-JdpGR9.png)

图8 buildParameterMapping过程



构建完成的ParameterMapping的结构如下图9中的代码所示，参数id对应的javaType类型为java.lang.Object，对应的TypeHander处理器为UnknownTypeHandler，也就是未找到合适的TypeHandler的兜底选项。

![图9 ParameterMapping结构](https://up-img.yonghong.tech/pic/2020/06/21-00-25-0f563de7db302e7498f5c5d48b0f55ab108990-khF0An.png)

图9 ParameterMapping结构



接下来，流程就会流转到Executor，在`org.apache.ibatis.executor.SimpleExecutor#doQuery`进行查询时，会根据当前的SQL类型，生成对应的StatementHandler。因为我们目前都是用的预编译SQL，因此生成的statementHandler就是PreparedStatementHandler，熟悉JDBC的小伙伴应该马上可以猜到对应的语句是什么类型了。然后，我们对这句SQL语句进行填充，如下图10中的代码所示。我们会通过PreparedStatementHandler的parameterize方法对Statement进行参数化，也就是进行填充。

![图10 PrepareStatement处理过程](https://up-img.yonghong.tech/pic/2020/06/21-00-25-53b0419dc111f5cb5785025707f173ab208427-Dagafq.png)

图10 PrepareStatement处理过程



在PreparedStatementHandler进行参数化时，会将参数化的职责交给DefaultParameterHandler处理。如下图11中的代码所示，我们主要关注红线部分，首先会获取ParameterMapping对应的TypeHander，如前文所述，获取到的是UnknownTypeHandler，然后会通过setParameter方法，将参数id替换成对应的值。

![img](https://up-img.yonghong.tech/pic/2020/06/21-00-25-ad6d78ea99d4c1a96f492d13fef7416c214168-Qr2pDy.png)

在Typehandler的流程里，首先会进入BaseTypeHandler，然后在具体设置时，会进入子类的方法。在UnknownTypeHandler，首先会再次对参数parameter进行解析，判断最正确的TypeHandler类型，如下图12中的代码所示:

![图12 获取可用TypeHandler](https://up-img.yonghong.tech/pic/2020/06/21-00-25-fa15fda92d13ba0cd2a97df576dbf429428834-qs3lt3.png)

图12 获取可用TypeHandler



在resolveTypeHandler方法中，因为已知了参数值的类型，通过Integer这个class在typeHandlerRegistry中寻找对应的TypeHandler，TypeHandlerRegistry是MyBatis启动时内置好的，代表Java对象类型和TypeHandler的映射关系，有兴趣的同学可以进入这个类详细看下。在这个例子中，我们会直接获取到IntegerHandler，如下图13中的代码所示:

![图13 获取IntegerHandler](https://up-img.yonghong.tech/pic/2020/06/21-00-25-b760df277efcda04462d2f94d168260b323127-6MHk67.png)

图13 获取IntegerHandler



在获取到IntegerHandler后，我们就可以使用IntegerTypeHandler的setInt方法，对SQL语句中的参数进行替换。如图14中的代码所示，SQL语句被成功替换：

![图14 IntegerHander值替换](https://up-img.yonghong.tech/pic/2020/06/21-00-25-3e6163357375d436fada0b275f768b65110984-lUwt1L.png)

图14 IntegerHander值替换



后续就是执行SQL并处理返回结果，这就不在本文的讨论范围内了。从上文的分析中，我们可以了解到，在3.2.3及以下版本，MyBatis会忽略parameterType，在真正进行SQL转换时，重新根据SQL方法入参类型，然后计算合适的TypeHandler处理器，所以本案例中的代码在3.2.3版本时，它在运行时是正常的。

### 以版本3.2.4为例，相比版本3.2.3，MyBatis构建SQL语句过程的变化分析

在前一章节中，我们得知MyBatis在运行SQL阶段重新计算参数对应的TypeHandler，然后进行SQL参数的替换。那么，在版本3.2.4中，MyBatis做了什么改动，从而导致了原有的使用方式变得不可用呢？从官方的Release Log来看，版本3.2.4做了这样的一个改动。

> This version builds the binding information during startup and the “parameterType” attribute is used

这个意思是说：parameterType会在框架初始化阶段阶段就被使用到。我们将分析的重点放在构建阶段，因为负责处理绑定关系的BoundSql由配置阶段的SqlSource生成，我们主要查看SqlSource的构建，在3.2.4中发生了什么变化。如图15所示，与3.2.3不同，3.2.4首先判断了是否为动态SQL，在非动态SQL情况下，才会将parameterType java.lang.String作为参数，传入SqlSource的构造方法。

![图15 生成SqlSource](https://up-img.yonghong.tech/pic/2020/06/21-00-25-1ef797f5581ce5bafd4b9019b0fbf1ea445131-jrGCbB.png)

图15 生成SqlSource



而后续流程与3.2.3一致，因为parameter类型为java.lang.String，在构建parameterMapping时，使用的类型就是java.lang.String。

![图16 构建ParameterMapping与3.2.3版本的差异](https://up-img.yonghong.tech/pic/2020/06/21-00-25-5a8a8b2e65f82266ea0f0a77b6e12b34226089-Ca77s2.png)

图16 构建ParameterMapping与3.2.3版本的差异



因为在框架初始化阶段，SqlSource的ParameterMapping中id对应的类型就是java.lang.String，这就导致在进行SQL语句的替换时，获取到的TypeHandler是StringTypeHandler，如下图17所示：

![图17  整数类型的参数获取到了StringTypeHandler](https://up-img.yonghong.tech/pic/2020/06/21-00-25-35b1a605bcaabb7aee2ef4de4378fa52637963-nyRxFf.png)

图17 整数类型的参数获取到了StringTypeHandler



后面的报错原因就比较好理解了，在调用StringTypeHandler的setString方法时，报出了`java.lang.ClassCastException: java.lang.Integer cannot be cast to java.lang.String`的错误。

## 总结

我们总结一下这个案例因：

MyBatis 3.2.3版本支持parameterType和实际参数类型不匹配，在执行SQL阶段，动态计算值处理器类型。在大版本升级2个版本号后，parameterType实际的类型开始生效，使用对应这个类型的TypeHandler对SQL进行参数替换，会导致Mapper方法中的参数和XML中的parameterType不匹配时，进而会出现类型转换报错。

这一段排查的经历，对自己后续编写代码及在系统上线时也有一些启发，主要包括以下几个方面：

- 在inf-bom升级时，需要线下进行全面回归，要避免框架存在不兼容的用法，不然的话，就容易导致线上错误。
- 开发同学可以检查自己系统内的MyBatis版本，如果是3.2.4以下，需要全面检查下现在的Mapper文件里对于parameterType的使用和Mapper方法中实际的参数类型是否一致，避免升级到3.2.4及以上版本时发生转型报错。如果有不匹配的情况存在，需要进行修正或者不使用parameterType，让MyBatis在运行SQL时自动计算对应的类型。
- 可以考虑使用MyBatis-Generator来自动生成XML和Mapper文件，毕竟是专业团队在维护，稳定性相对来说会更好一些，同时能够避免手动修改XML文件带来的误操作。
- 可以主动关注强依赖的一些开源框架的Release Log，不要错过了重要的信息。

## 参考资料

- [带你一步一步手撕 MyBatis 源码加手绘流程图——构建部分](https://juejin.im/post/5db92c41f265da4d0a68d161)
- [带你一步一步手撕 MyBatis 源码加手绘流程图——执行部分](https://juejin.im/post/5dbe35286fb9a0205d562942)
- [MyBatis源码解析（三）—缓存篇](https://juejin.im/post/5e5355f76fb9a07cd00d8066)
- [面试官问你MyBatis SQL是如何执行的？把这篇文章甩给他](https://juejin.im/post/5e350d895188254dfd43def5)
- [源码分析(1.4万字) MyBatis接口没有实现类为什么可以执行增删改查](https://juejin.im/post/5e03f7d5e51d45583615ab3e)
- [MyBatis/MyBatis-3/Comparing changes](https://github.com/mybatis/mybatis-3/compare/mybatis-3.2.3...mybatis-3.2.4#diff-788c1708d6225826f59c2344c9267f71)

## 作者简介

凯伦，2016年校招加入美团，后端开发工程师。