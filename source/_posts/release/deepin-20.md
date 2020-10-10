---
title: 【release】深度操作系统 20——崭新视界，创无止境
tags:
- release
- deepin
- 深度操作系统
- 深度
- 操作系统
- Linux
categories:
- release
date: 2020-09-27 23:10:00
updated: 2020-09-27 23:10:00
---

深度操作系统是一个致力于为全球用户提供美观易用、安全可靠的Linux发行版。

深度操作系统 20正式版（1002）采取统一的设计风格，从桌面环境和应用进行重新设计，带来焕然一新的视觉感受。底层仓库升级到Debian 10.5，系统安装采用双内核机制（Kernel 5.4、Kernel 5.7），全面提升系统稳定性和兼容性。全新设计的启动器菜单、指纹识别、系统安全增强等，系统部分预装应用升级到最新版本，只为给你更好体验。

## 特性

### 统一风格的桌面环境

别出心裁的图标设计，焕然一新的图形界面，自然、平滑的动画过渡效果，更有独树一帜的圆角窗口设计，精美绝伦的多任务视图，处处精心，只为给你细腻自然的品质体验。

> **|** 支持黑白主题、透明度调节、色温调节自定义、电源电池设置等贴心功能。

![统一风格的桌面环境](https://up-img.yonghong.tech/pic/2020/09/27-16-23-27-16-23-iRV5BI-ATr2ZD-JjGJ5m.jpg)

<!-- more -->

### 个性贴心的通知管理

增强通知中心功能，支持设置通知时提示声音、锁屏时显示消息、仅在通知中心显示、显示消息预览，必要应用强提醒、特定应用弱提醒或不提醒，个性化你的消息通知，在不错过任何重要提醒的同时，避免不必要的打扰。

![个性贴心的通知管理](https://up-img.yonghong.tech/pic/2020/09/27-16-24-27-16-24-hJCvMy-WLeZpv-mvBBhl.jpg)

### 系统支持双内核安装

系统安装界面提供双内核选项，Kernel 5.4（LTS）和Kernel 5.7（Stable）以及Safe Graphics模式，保证系统安装更多选择，提升系统整体的稳定性、兼容性，最新的内核支持更多的硬件设备。

![系统支持双内核安装](https://up-img.yonghong.tech/pic/2020/09/27-16-24-27-16-24-WspxeU-zvptvY-YvoU8n.jpg)

### 更易用的新版安装器

化繁为简的设计和交互，保证更一致的操作习惯。新版的安装器界面，只需按照操作向导提示安装即可，在硬盘分区操作中，提供手动和全盘安装两种模式，并且支持全盘加密功能。

> **|** 注：对于N卡用户，安装器自动检测并提供安装闭源驱动选项。

![更易用的新版安装器](https://up-img.yonghong.tech/pic/2020/09/27-16-25-27-16-24-bumxXq-GrMhtE-20200927162509782-giomVd.jpg)

### 管理方便的应用商店

应用商店的不同类别应用，覆盖了生活、工作的主要使用场景，本次新增一键更新、应用筛选等功能，带来更便捷的应用管理体验，同时也兼容部分Wine应用，并达到原生应用的体验。

![管理方便的应用商店](https://up-img.yonghong.tech/pic/2020/09/27-16-25-27-16-25-RxrLgT-5Q3bom-UfkDuS.jpg)


### 好用安全的指纹识别

全新的指纹功能框架，提供了更细腻的引导交互和更准确的场景提示。可使用指纹进行解锁登录、验证身份和管理员权限。现已支持多款国产指纹硬件。

![好用安全的指纹识别](https://up-img.yonghong.tech/pic/2020/09/27-16-25-27-16-25-aejF3j-Pz3lYF-4fHAhu.jpg)

------

## 系统更新日志（15.11->20正式版）

### 新增功能

- 新增设备管理器，查看和管理硬件设备
- 新增字体管理器，支持安装、管理字体，个性化文字内容显示
- 新增茄子，满足拍照、录制视频需求
- 新增用户反馈，快来深度社区和其他深粉一起交流讨论吧
- 新增画板，随心创作你的想法，简直设计爱好者福音
- 新增日志收集工具，查看系统同步的日志类型，快速定位问题
- 新增图标主题，带来更丰富的显示体验
- 新增商店应用更新功能，分类交互显示增强，详情页面布局调整
- 增强语音记事本，结合记事本和语音记录功能
- 截图、录屏应用合并，记录内容更省心
- 替换文档查看器、归档管理器、编辑器，更好的交互、视觉体验

### 其他更新

DDE

- 优化系统待机唤醒体验
- 优化自动更换壁纸功能体验
- 修复高分屏切换分辨率后出现花屏现象
- 修复在控制中心设置字体大小为20，登录页面字体没有生效
- 修复输入正确账号密码登录云同步，又弹出账号密码输入框
- 修复外接无线网卡和蓝牙，机器没有响应的问题
- 修复双屏模式下任务栏选择状态一直隐藏，桌面的图标部分消失
- 修复配合N卡切换闭源驱动失败的问题
- 修复任务栏概率性显示2个文件管理器图标
- 修复数位板下列表里"鼠标"和"笔"的设置相反的问题
- 修复每点击一次任务栏上的回收站图标，都会打开一个窗口

语音记事本

- 优化整体功能操作，记录管理更便捷
- 修复启动系统后第一次打开操作卡顿的问题
- 修复添加文字区域点击鼠标右键，“语音朗读”，“翻译”，“语音听写”文字未去掉
- 修复文本内容太长时，剪贴板中没有显示省略号

输入法

- 优化输入法配置预装五笔输入法
- 修复输入法设置页面“ctrl”属性设置置灰
- 修复恢复默认键盘布局不生效

任务栏

- 优化任务栏插件区的网络图标显示
- 优化qBittorrent应用托盘显示
- 优化右下角电池图标显示
- 修复语音记事本的音量文字部分显示重叠

相册

- 修复打开图片占用CPU过高的问题

控制中心

- 优化时区设置显示的地图信息
- 优化拔掉数位板，控制中心界面显示只有二级菜单
- 修复蓝牙无法连接设备的问题
- 修复选择设备后，选择后背景图层覆盖文字
- 修复电源管理中关闭显示器时间设置无效
- 修复网络应用代理设置无效的端口可以保存成功
- 修复设置屏幕缩放为1.25或1.5，打开通知栏后，点击红色区域无法关闭通知栏
- 修复系统重启或开机后，无线网络显示连接但没有网络的问题
- 修复更新/更新设置的图标点击之后的状态显示不对
- 修复网络账户登出后应用商店同步登出，图像显示未同步退出的问题
- 修复系统快捷键和应用快捷键冲突的问题
- 修复插上USB数位板，控制中心无数位板栏
- 修复插上USB无线网卡后，设备有输入但控制中心和任务栏无显示
- 修复插入usb耳机后重启查看高级设置，界面前后不一致的问题
- 修复控制中心多了一个High Contrast图标主题
- 修复在扩展模式下接入双屏，显示器花屏的问题
- 修复任务栏上出现两个控制中心的图标
- 修复设置外接显示器为主屏时，截图功能异常
- 修复图标主题设置bloom-classic，启动器里面的"文档查看器"图标显示锯齿
- 修复系统待机休眠唤醒后，无法识别网络的问题
- 修复wifi图标个别主题没有显示

日历

- 修复安装系统后打开日历，左上角图标跟实际日期不一致

音乐

- 修复偶像歌手名称下拉选项与音乐页面分离的问题
- 修复根据歌手不能搜索到歌曲

通知中心

- 修复系统语言为英文时，通知消息为中文

应用商店

- 修复应用点击安装无反应，实际可以安装成功没有进度显示
- 修复点击商店分类缓冲超过15秒，提示网络错误的问题
- 修复有应用下载或者报错时，下载管理列表信息中显示空白
- 修复在搜索栏搜索应用出现提示栏时，移动应用商店框后提示栏不会跟随移动
- 修复商店安装wine应用，概率性出现提示依赖错误的问题

安装器

- 优化时区设置页里的map划分
- 修复加密安装完以后重启电脑，安装器全盘加密失败
- 修复手动分区安装，U盘没有自动挂载，文件管理器不显示U盘信息
- 修复全盘安装时，全盘加密选项不生效

打印管理器

- 修复：佳能驱动安装成功后下发网络打印任务，没有文件在打印的问题

深度影院

- 修复播放视频时点击任务栏音量，单独调节影院音量播放不均匀且显示名称重叠
- 修复播放视频时，进度栏边角没有做虚化处理
- 修复播放视频CPU占用过高，4K视频不能硬解的问题

设备管理器

- 修复连接蓝牙适配器，概况里显示未知的问题

归档管理器

- 修复压缩包解压完成后界面文字错误
- 修复下载的chrome插件crx(重命名zip后)或zip格式，使用自带压缩应用打开需要密码
- 修复在设置中是否勾选“当解压完成后自动打开文件夹”，都会打开文件夹的问题
- 修复解压压缩包文件后，文件名称显示乱码

第三方应用

- 优化chrome在任务栏驻留体验
- 修复企业微信频繁崩溃的问题
- 修复打开文件，永中office不自动弹出打开页面且无法进行粘贴快捷键粘贴图片
- 修复WPS2019发送到任务栏，以及打开后在任务栏图标显示均为锯齿的问题
- 修复显示消息记录面板中，QQ的消息历史无法阅读

deepin-wine

- 修复修复企业微信剪切图片切换窗口后崩溃的问题
- 修复微信发送多个文件失败的问题
- 修复QQ图片无法加载的问题
- 修复企业微信图片分配内存异常的问题
- 修复企业微信会议/直播，提示版本低无法使用的问题
- 修复语音通话没声音的问题

文档查看器

- 优化打开多个PDF文档时以标签形式显示
- 修复同时打开3个PDF文档后，关闭按钮不可用的问题

系统监视器

- 优化整体功能体验，查看系统状态更清晰
- 修复某些语言下名称显示错误

窗口管理器

- 修复alt+tab切换窗口管理器时，部分wine应用显示图标模糊

日志收集工具

- 修复日志收集工具的时间显示超前的问题
- 修复日志收集工具导出按钮概率性弹不出保存对话框

文本编辑器

- 优化编辑器窗口拖动响应区域大小
- 修复搜索相同字符时，“上一个”、“下一个”均无反应

软件包安装器

- 优化批量安装 deb 软件包体验

帮助手册

- 优化更新帮助手册介绍内容
- 优化截图录屏的英文介绍内容

## 系统更新日志（20（1001）->20正式版）

DDE

- 修复配合N卡切换闭源驱动失败的问题
- 修复任务栏概率性显示2个文件管理器图标
- 修复数位表下列表里"鼠标"和"笔"的设置相反的问题
- 修复每点击一次任务栏上的回收站图标，都会打开一个窗口

相册

- 修复打开图片占用CPU过高的问题

任务栏

- 优化qBittorrent应用托盘显示
- 优化右下角电池图标显示
- 修复语音记事本的音量文字部分显示重叠

控制中心

- 修复在扩展模式下接入双屏，显示器花屏的问题
- 修复任务栏上出现两个控制中心的图标
- 修复设置外接显示器为主屏时，截图功能异常
- 修复图标主题设置bloom-classic，启动器里面的"文档查看器"图标显示锯齿
- 修复系统待机休眠唤醒后，无法识别网络的问题
- 修复wifi图标个别主题没有显示

安装器

- 修复全盘安装时，全盘加密选项不生效

归档管理器

- 修复下载的chrome插件crx(重命名zip后)或zip格式，使用自带压缩应用打开需要密码
- 修复在设置中是否勾选“当解压完成后自动打开文件夹”，都会打开文件夹的问题
- 修复解压压缩包文件后，文件名称显示乱码

日志收集工具

- 修复日志收集工具的时间显示超前的问题
- 修复日志收集工具导出按钮概率性弹不出保存对话框

日历

- 修复安装系统后打开日历，左上角图标跟实际日期不一致

应用商店

- 修复在搜索栏搜索应用出现提示栏时，移动应用商店框后提示栏不会跟随移动
- 修复商店安装wine应用，概率性出现提示依赖错误的问题

文本编辑器 ￼

- 优化编辑器窗口拖动响应区域大小
- 修复搜索相同字符时，“上一个”、“下一个”均无反应

帮助手册

- 优化截图录屏的英文介绍内容

输入法

- 修复恢复默认键盘布局不生效

第三方应用

- 修复显示消息记录面板中，QQ的消息历史无法阅读
- 修复系统自带chromium浏览器登录论坛密码输入正确，但依旧提示未登录

深度影院

- 修复播放视频CPU占用过高，4K视频不能硬解的问题

窗口管理器

- 修复alt+tab切换窗口管理器时，部分wine应用显示图标模糊

已知问题

- Super+S快捷键调用窗口管理器，通过触摸板四指滑动后高概率崩溃
- 任务栏位置调整到左侧，魔灯窗口依然从底部调出

------

## ISO下载方式

64位：[点此下载](https://www.deepin.org/zh/download/)

其他下载点：

[百度云](https://pan.baidu.com/s/1rxKAKJDnFTtWgFNj-U_a-Q)（3m4f）、[OSDN](https://osdn.net/projects/deepin/storage/20/)、[Sourceforge](https://sourceforge.net/projects/deepin/files/20/)、[Google Drive](https://drive.google.com/drive/folders/1vM-Ud8m63RI3sUIWiKiO3_7DLKzbIkHh?usp=sharing)、BT、[国内外镜像源](https://www.deepin.org/mirrors/releases/)

> 全球排名：https://distrowatch.com/table.php?distribution=deepin

 

跨版本升级操作如下：

1、将15.11官方源替换成20官方源（/etc/apt/sources.list）

deb [by-hash=force] https://community-packages.deepin.com/deepin/ apricot main contrib non-free

2、新增20官方商店源（/etc/apt/sources.list.d/appstore.list ），无list文件创建后添加：

deb https://community-store-packages.deepin.com/appstore eagle appstore

------

## 关于我们

深度操作系统是一款针对普通用户而发行的开源桌面系统，您可自由下载、分发、修改和使用。

欢迎您关注我们的[微博](http://weibo.com/linuxdeepinnew)、[微信](https://www.deepin.org/wp-content/uploads/2017/01/pc_social_weixin.jpg)（深度操作系统）、[Twitter](https://twitter.com/linux_deepin)、[Facebook](https://www.facebook.com/deepinlinux)、[Github](https://github.com/linuxdeepin)以第一时间获取最新动态和源代码，同时也欢迎您前往我们的论坛，与我们交流和分享您的快乐。

最后，我们郑重感谢为深度操作系统提供测试、文档、翻译和镜像支持的社区团队与企业，感谢你们的无私的贡献，开源有你们更精彩。也要感谢一直支持、理解和等待我们的用户，是你们给了深度操作系统不断前行的动力，和不断自我修正的勇气。

## 参考链接

- https://www.deepin.org/zh/2020/09/11/deepin-20-innovation-is-ongoing/