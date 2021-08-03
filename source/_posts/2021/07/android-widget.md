---
title: Android 常用组件
tags:
- Android
- 控件
- Widget
- TextView
- Button
- EditText
- ImageView
- ProgressBar
- Notification
- Toolbar
- AlertDialog
- PopUpWindow
categories:
- Android
date: 2021-07-30 22:24:00
updated: 2021-07-30 22:24:00
---

## TextView

TextView 基础属性
- layout_width：组件宽度
- layout_height：组件高度
- id：为 TextView 组件设置一个 id
- text：设置显示文本的内容
- textColor：设置字体颜色
- textStyle：设置字体风格：三种可选值：normal, bold, italic
- textSize：字体大小，单位一般是用 sp
- background：控件的背景颜色，可以理解为填充整个控件颜色，可以是图片
- gravity：设置控件中内容对齐方向

<!-- more -->

带阴影的TextView
- shadowColor：设置阴影的颜色值
- shadowRadius：设置阴影的模糊度
- shadowDx：设置水平偏移
- shadowDy：设置垂直偏移

跑马灯效果TextView
- singleLine：设置内容单行显示
- focusable：是否可以获得焦点
- focusableInTouchMode：在触摸模式下是否可以获得焦点
- ellipsize：在哪里省略文本
- marqueeRepeatLimit：字幕动画重复次数

```xml
    <TextView
        android:id="@+id/tv_one"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:ellipsize="marquee"
        android:focusable="true"
        android:focusableInTouchMode="true"
        android:marqueeRepeatLimit="marquee_forever"
        android:singleLine="true"
        android:text="@string/tv_one">

        <requestFocus />
    </TextView>
```

## Button

继承 TextView

三层
- foreground：前景色、前景图片
- text：文字内容
- background：背景色、背景图片

事件处理
- 点击事件：onClickListener，抬起时触发
- 长按事件：onLongClickListener，按下指定时长后触发
- 触摸事件：onTouchListener
  - 按下(ACTION_DOWN, 0)
  - 抬起(ACTION_UP, 1)
  - 移动(ACTION_MOVE, 2)


## StateListDrawable

StateListDrawable 是 Drawable 资源的一种，可以根据不同的状态，设置不同的图片效果，关键节点 `<selector>`，我们只需要将 Button 的 background 属性设置为该 drawable 资源即可

常用属性
- drawable：引用的 Drawable 资源
- state_focused：是否获得焦点
- state_pressed：控件是否被按下
- state_enabled：控件是否可用
- state_selected：控件是够被选择，针对有滚动的情况
- state_checked：控件是否被勾选
- state_checkable：控件可否被勾选
- state_window_focused：是否获得窗口焦点
- state_active：控件是否处于活跃状态
- state_single：控件包含多个子控件时，确定是否只显示一个控件
- state_first：控件包含多个子控件时，确定第一个控件是否处于显示状态
- state_middle：控件包含多个子控件时，确定中间一个控件是否处于显示状态
- state_last：控件包含多个子控件时，确定最后一个控件是否处于显示状态

## EditText

继承 TextView

常用属性
- hint：输入提示
- textColorHint：输入提示文字颜色
- inputType：输入类型
- drawableXxxx：在输入框的指定方位添加图片
- drawablePadding：设置图片与文字间距
- padding：设置内容与边框边距
- background：背景色

## ImageView

常用属性
- src：设置图片资源
- scaleType：设置图片缩放类型
- maxHeight：最大高度
- maxWidth：最大宽度
- adjustViewBounds：调整View的界限

缩放类型
- fitStart：保持宽高比缩放图片，缩放完成后在 ImageView 的左上角
- fitCenter：默认，保持宽高比缩放图片，缩放后放于中间
- fitEnd：保持宽高比缩放图片，缩放后在 ImageView 的右下角 
- fitXY：对图像的纵横方向进行独立缩放，使得图片完全适应 ImageView，但是图片宽高比可能会发生变化
- center：保持原图大小，显示在 ImageView 中心，当原图大于 ImageView 的 size，会进行适当裁剪
- centerCrop：保持宽高比缩放图片，直到完全覆盖 ImageView，可能会出现图片显示的不完全
- centerInside：保持宽高比缩放图片，直到 ImageView 能够完全的显示图片
- matrix：不改变原图大小，从 ImageView 左上角开始绘制原图，超出部分做裁剪处理

## ProgressBar

常用属性
- max：进度条的最大值
- progress：进度条已完成进度
- indeterminate：如果设置成 true，则进度条不精确显示进度
- style="?android:attr/progressBarStyleHorizontal"：水平进度条

## Notification

- NotificationManager manager = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
- NotificationChannel（Build.VERSION.SDK_INT >= Build.VERSION_CODES.O）
- NotificationCompat.Builder()
- Notification
- PendingIntent

通知重要程度设置
- IMPORTANCE_NONE：关闭通知
- IMPORTANCE_MIN：开启通知，不会弹出，没有提示音，状态栏无显示
- IMPORTANCE_LOW：开启通知，不会弹出，没有提示音，状态栏显示
- IMPORTANCE_DEFAULT：开启通知，不会弹出，有提示音，状态栏显示
- IMPORTANCE_HIGH：开启通知，会弹出，有提示音，状态栏显示

常用属性
- .setContentTitle() 标题
- .setContentText()  内容
- .setSmallIcon()    小图片 使用 alpha 图层
- .setLargeIcon()    大图片 Bitmap
- .setColor()        小图标颜色 Color.parseColor("#ff0000")
- .setContentIntent() 跳转意图 PendingIntent
- .setAutoCancel()    自动清除通知
- .setWhen()         通知创建时间


## Toolbar

常用属性
- id
- layout_width
- layout_height="?attr/actionBarSize"
- title
- titleMarginStart
- titleTextColor
- subtitle
- subtitleTextColor
- background
- logo
- navigationIcon
- layout_height="wrap_content"
- android:layout_gravity="center"

## AlertDialog

常用属性
- .setIcon()
- .setTitle()
- .setMessage()
- .setView()     自定义布局
- .setPositiveButton()
- .setNegativeButton()
- .setNeutralButton()

## PopUpWindow

- contentView
- width
- height
- focusable
- showAsDropDown
- dismiss
- touchable
- outsideTouchable


```java
    View popupView = getLayoutInflater().inflate(R.layout.popup_view, null);
    PopupWindow popupWindow = new PopupWindow(popupView, ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT, true);
    popupWindow.showAsDropDown(view);
```
