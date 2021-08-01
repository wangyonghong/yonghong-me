---
title: Android 常用布局
tags:
- Android
- 布局
- Layout
- LinearLayout
- RelativeLayout
- FrameLayout
- TableLayout
- GridLayout
- ConstraintLayout
categories:
- Android
date: 2021-07-31 22:24:00
updated: 2021-07-31 22:24:00
---

## LinearLayout 线性布局

常用属性
- orientation：布局总组件的排列方式 vertical、horizontal
- gravity：组件所包含的组件的排列方式
- layout_gravity：组件在父容器里的排列方式
- background：背景
- divider：分割线
- showDividers：分割线所在位置：none, beginning, end, middle
- dividerPadding：设置分割线的 padding
- layout_weight：权重，分配剩余空间

<!-- more -->

## RelativeLayout 相对布局

根据父容器定位
- android:layout_alignParentStart
- android:layout_alignParentEnd
- android:layout_alignParentTop
- android:layout_alignParentBottom
- android:layout_centerHorizontal
- android:layout_centerVertical
- android:layout_centerInParent

根据兄弟组件定位
- android:layout_toStartOf
- android:layout_toEndOf
- android:layout_above
- android:layout_below
- android:layout_alignStart
- android:layout_alignEnd
- android:layout_alignTop
- android:layout_alignBottom
  
margin：组件与父容器的边距
- android:layout_margin
- android:layout_marginStart
- android:layout_marginEnd
- android:layout_marginTop
- android:layout_marginBottom

padding：组件内部的边距
- android:padding
- android:paddingStart
- android:paddingEnd
- android:paddingTop
- android:paddingBottom


## FrameLayout 帧布局

常用属性：
- android:foreground="@drawable/ceshi"
- android:foregroundGravity="right|bottom"

## TableLayout 表格布局

常用属性
- android:collapseColumns   隐藏
- android:stretchColumns    拉伸
- android:shrinkColumns     收缩

子控件属性
- android:layout_column     显示在第几列
- android:layout_span       横向跨几列


## GridLayout 网格布局

常用属性
- android:orientation 
- android:columnCount
- android:rowCount

子控件属性
- android:layout_gravity fill、center
- android:layout_column
- android:layout_columnSpan
- android:layout_columnWeight
- android:layout_row
- android:layout_rowSpan
- android:layout_rowWeight

## ConstraintLayout 约束布局

https://developer.android.com/training/constraint-layout?hl=zh-cn
