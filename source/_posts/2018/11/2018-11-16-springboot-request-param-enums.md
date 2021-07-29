---
layout: post
title:  "SpringBoot 请求参数为枚举类型"
category: "SpringBoot"
tags: ["SpringBoot"]
date: 2018-11-16 00:00:00
updated: 2018-11-16 00:00:00
---

### 情景

在一个请求中有一个参数 range ，可以选择的有 week month quarter year 四个。为了不让 magic 变量漫天飞，我把他变成了一个枚举类型。

<!-- more -->


```java
@Getter
public enum RangeEnum{

    /**
     * 查询的 range，周，月，季度，年
     */
    WEEK("week"),
    MONTH("month"),
    QUARTER("quarter"),
    YEAR("year");

    private String value;

    RangeEnum(String value) {
        this.value = value;
    }

}
```

Controller 中

```java
@GetMapping(value = "/list")
public GenericResponse getXXList(
	@RequestParam(value = "range") RangeEnum range) {
	// do something
}
```

但是这样写，这个 controller 只能接收 WEEK，MONTH 等等，一旦出现 week 这样的参数是无法处理的。

### 解决

所以我们可以写一个 convertor

```java
// 包要导对
import org.springframework.core.convert.converter.Converter;

class StringToRangeEnumConverter implements Converter<String, RangeEnum> {

    private Map<String, RangeEnum> enumMap = new HashMap<>();

    StringToRangeEnumConverter() {
        
        for(RangeEnum e : RangeEnum.values()) {
            enumMap.put(e.getValue(), e);
        }
    }

    @Override
    public RangeEnum convert(String source) {

        RangeEnum result = enumMap.get(source);
        if (result == null) {
            // 异常可以稍后去捕获
            throw new IllegalArgumentException("No element matches " + source);
        }
        return result;
    }
}
```

这样问题又来了，如果有很多个枚举类，那我就要写很多了 convertor 了啊。

所以我们引入了一个 ConverterFactory

首先有一个 BaseEnum

```java
public interface BaseEnum {
    String getValue();
}
```

其他的枚举类实现这个借口就可以了，然后我们开始写 ConverterFactory


```java
import org.springframework.core.convert.converter.Converter;
import org.springframework.core.convert.converter.ConverterFactory;

import java.util.HashMap;
import java.util.Map;


public class StringToEnumConverterFactory implements ConverterFactory<String, BaseEnum> {

    private static final Map<Class, Converter> converterMap =  new HashMap<>();

    @Override
    public <T extends BaseEnum> Converter<String, T> getConverter(Class<T> targetType) {
        Converter<String, T> converter = converterMap.get(targetType);
        if(converter == null) {
            converter = new StringToEnumConverter<>(targetType);
            converterMap.put(targetType, converter);
        }
        return converter;
    }

    class StringToEnumConverter<T extends BaseEnum> implements Converter<String, T> {

        private Map<String, T> enumMap = new HashMap<>();

        StringToEnumConverter(Class<T> enumType) {
            T[] enums = enumType.getEnumConstants();
            for(T e : enums) {
                enumMap.put(e.getValue(), e);
            }
        }

        @Override
        public T convert(String source) {

            T t = enumMap.get(source);
            if (t == null) {
                // 异常可以稍后去捕获
                throw new IllegalArgumentException("No element matches " + source);
            }
            return t;
        }
    }
}
```

写完了之后还不行，还需要在 spring 中注册这个 ConverterFactory 为什么要注册呢，这个地方我还不会，以后来填坑

```java
import org.springframework.boot.SpringBootConfiguration;
import org.springframework.format.FormatterRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@SpringBootConfiguration
public class WebMvcConfig implements WebMvcConfigurer {

    /**
     * 枚举类的转换器 addConverterFactory
     */
    @Override
    public void addFormatters(FormatterRegistry registry) {
        registry.addConverterFactory(new StringToEnumConverterFactory());
    }
}
```

这样以后我们就可以传参数 week month 等等了，如果传入了别的参数，就会抛出异常，异常的处理可以用全局的异常处理，这部分以后来填坑




