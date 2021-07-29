---
layout: post
title: macOS 技巧（1）——「预览的使用」
categories: [macOS]
tags: [macOS]
date: 2018-03-06 00:00:00
updated: 2018-03-06 00:00:00
---

> 多图预警！多图预警！多图预警！

macOS 自带的「预览.app（Preview.app）」 功能十分强大，可以用来阅读 PDF（做笔记），查看和编辑图片等，还可以通过安装丰富的插件实现其他文件的预览。

<!-- more -->

## 阅读和编辑 PDF

用预览打开一个 PDF 文档，可以看到右上角有一个编辑的按钮（如图，箭头所指），单击一下，会出现下面的一排功能按钮，每一个功能都很实用，下面我来简单介绍一下。

![](https://up-img.yonghong.tech/pic/2021/07/29-16-46-001-dBBqoj.png)

- 〇裁剪工具，画出矩形选区，裁剪。  
- ①智能线条，线条粗细不变，可以画出直线，曲线，甚至是解说气泡。    
- ②智能线条，可以根据触摸板按压力度确定线条粗细  
- ③多边形工具，可以画出直线，箭头，矩形，圆角矩形，圆，椭圆，任意正多边形，任意正多角形。  
- ④文字工具  
- ⑤签名，可以通过触摸板手写或者在纸上写好签名对着摄像头扫描   
- ⑥笔记批注工具  
- ⑦调整以上所有线条的粗细，包括多边形边框  
- ⑧调整多边形边框颜色  
- ⑨调整多边形填充颜色，无即为透明  
- ⑩调整字体，大小等

此外，右上角还有一个笔形的工具，可以给文字内容加高亮，下划线，删除线。
 
## 查看和编辑图片

![](https://up-img.yonghong.tech/pic/2021/07/29-16-46-002-LIkJpk.png)

如图所示，编辑图片比 PDF 不同的三个功能（哦，不对是两个，忽略第一个箭头）分别是调整颜色，调整图片大小。

调整颜色有基本的曝光度，色调，色温等等。

调整图片大小可以自定义大小和预设的大小，这样可以很方便的压缩图片。

## 其他技巧

### 重排和拼接 PDF 文档

在预览中打开 PDF 文档，选择左上角的「缩图清单」（Contact Sheet）选项，拖动想要调换顺序的页面即可调换顺序，也可以按住 command 键来选择多个页面。

![](https://up-img.yonghong.tech/pic/2021/07/29-16-46-003-NdXmnU.png)

在预览中打开另一个文档，同样选择左上角的「缩图清单」（Contact Sheet）选项，可以将一个 PDF 的页面拖动到另一个 PDF 文档中。

### 旋转翻转图片

旋转图片可以点击工具栏的旋转按钮，默认是逆时针旋转，也可以按住 option 键，这样就变了顺时针旋转。也可以在菜单栏中选择「工具」-> 旋转，可以发现，还可以用 command + L 和 command + R 进行旋转。

翻转图片可以在菜单栏中选择「工具」-> 水平翻转/垂直翻转。


## [插件](https://github.com/sindresorhus/quick-look-plugins)

> 插件来源为 GitHub 上的一个项目，看起来一直在更新，可以从[源项目](https://github.com/sindresorhus/quick-look-plugins)中查看。

### 安装

#### 使用 [Homebrew Cask](https://github.com/phinze/homebrew-cask)

- 运行 `brew cask install <package>`

<span id="install-all"></span>

##### 安装全部

```
brew cask install qlcolorcode qlstephen qlmarkdown quicklook-json qlprettypatch quicklook-csv betterzipql qlimagesize webpquicklook suspicious-package quicklookase qlvideo
```

#### 手动安装

- 点击 "手动下载"
- 将下载的 .qlgenerator 文件移动到 `~/Library/QuickLook`
- 运行 `qlmanage -r`


### 插件列表


#### [QLColorCode](https://github.com/anthonygelibert/QLColorCode)

> 预览代码，有基本的语法高亮

运行 `brew cask install qlcolorcode` or [手动下载](https://github.com/anthonygelibert/QLColorCode/releases/latest)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-47-QLColorCode-V6SfbN.png)](https://github.com/anthonygelibert/QLColorCode)


#### [QLStephen](https://github.com/whomwah/qlstephen)

> 预览无拓展名的普通文本文件，如：README, CHANGELOG, index.styl 等等.

运行 `brew cask install qlstephen` or [手动下载](https://github.com/whomwah/qlstephen/releases/latest)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-48-QLStephen-mBHrZO.png)](https://github.com/whomwah/qlstephen)


#### [QLMarkdown](https://github.com/toland/qlmarkdown)

> 预览 Markdown 文件

运行 `brew cask install qlmarkdown` or [手动下载](https://github.com/downloads/toland/qlmarkdown/QLMarkdown-1.3.zip)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-48-QLMarkdown-iPid34.png)](https://github.com/toland/qlmarkdown)


#### [QuickLookJSON](http://www.sagtau.com/quicklookjson.html)

> 预览 JSON 文件

运行 `brew cask install quicklook-json` or [手动下载](http://www.sagtau.com/media/QuickLookJSON.qlgenerator.zip)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-48-QuickLookJSON-lVtWMi.png)](http://www.sagtau.com/quicklookjson.html)


#### [QLPrettyPatch](https://github.com/atnan/QLPrettyPatch)

> 预览 .patch 文件

运行 `brew cask install qlprettypatch` or [手动下载](https://github.com/atnan/QLPrettyPatch/releases/latest)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-49-QLPrettyPatch-BHGW6d.png)](https://github.com/atnan/QLPrettyPatch)


#### [QuickLookCSV](https://github.com/p2/quicklook-csv)

> 预览 CSV 文件

运行 `brew cask install quicklook-csv` or [手动下载](http://quicklook-csv.googlecode.com/files/QuickLookCSV.dmg)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-49-QuickLookCSV-984HqZ.png)](https://github.com/p2/quicklook-csv)


#### [BetterZipQL](http://macitbetter.com/BetterZip-Quick-Look-Generator/)

> 预览压缩文件

运行 `brew cask install betterzipql` or [手动下载](http://macitbetter.com/BetterZipQL.zip)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-49-BetterZipQL-r7v3cM.png)](http://macitbetter.com/BetterZip-Quick-Look-Generator/)


#### [qlImageSize](https://github.com/Nyx0uf/qlImageSize)

> 显示图片大小和分辨率

运行 `brew cask install qlimagesize` or [手动下载](https://github.com/Nyx0uf/qlImageSize#installation)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-49-qlImageSize-DvCxpH.png)](https://github.com/Nyx0uf/qlImageSize)


#### [WebP](https://github.com/dchest/webp-quicklook)

> 预览 WebP 图片

运行 `brew cask install webpquicklook` or [手动下载](https://github.com/dchest/webp-quicklook/releases/latest)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-50-WebP-aPTSyy.png)](https://github.com/dchest/webp-quicklook)


#### [Suspicious Package](http://www.mothersruin.com/software/SuspiciousPackage/)

> 预览 macOS App 标准安装包内容

运行 `brew cask install suspicious-package` or [手动下载](http://www.mothersruin.com/software/downloads/SuspiciousPackage.xip)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-50-SuspiciousPackage-03DD5k.png)](http://www.mothersruin.com/software/SuspiciousPackage/)


#### [QuickLookASE](https://github.com/rsodre/QuickLookASE)

> Preview Adobe ASE Color Swatches generated with Adobe Photoshop, Adobe Illustrator, [Adobe Color CC](https://color.adobe.com), [Spectrum](http://www.eigenlogik.com/spectrum/mac), [COLOURlovers](http://www.colourlovers.com), [Prisma](http://www.codeadventure.com), among many others.

运行 `brew cask install quicklookase` or [手动下载](https://github.com/rsodre/QuickLookASE/releases/latest)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-50-QuickLookASE-QL64FT.png)](https://github.com/rsodre/QuickLookASE)


#### [QLVideo](https://github.com/Marginal/QLVideo)

> 预览大多数视频文件，缩略图，封面和元数据

运行 `brew cask install qlvideo` or [手动下载](https://github.com/Marginal/QLVideo/releases/latest)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-51-QLVideo-2lu6IP.png)](https://github.com/Marginal/QLVideo)


### 更多

*这些不包含在 [安装全部](#install-all).*

#### [ProvisionQL](https://github.com/ealeksandrov/ProvisionQL)

> 预览 iOS / macOS app 和他们提供的基本信息

运行 `brew cask install provisionql` or [手动下载](https://github.com/ealeksandrov/ProvisionQL/releases/latest)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-51-ProvisionQL-adjoj4.png)](https://github.com/ealeksandrov/ProvisionQL)


#### [QuickLookAPK](https://github.com/hezi/QuickLookAPK)

> 预览 Android APK 文件

运行 `brew cask install quicklookapk` or [手动下载](https://github.com/hezi/QuickLookAPK/blob/master/QuickLookAPK.qlgenerator.zip)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-51-QuickLookAPK-g6LM6g.png)](https://github.com/hezi/QuickLookAPK)


#### [quicklook-pat](https://github.com/pixelrowdies/quicklook-pat)

> 预览 Adobe Photoshop pattern 文件

运行 `brew cask install quicklook-pat` or [手动下载](https://github.com/pixelrowdies/quicklook-pat/releases)

[![](https://up-img.yonghong.tech/pic/2021/07/29-16-51-quicklook-pat-lq9s09.png)](https://github.com/pixelrowdies/quicklook-pat)


## 参考

[Mac「预览」应用小技巧（一）：给你的文档添加手写签名](https://sspai.com/post/27671)

[Mac「预览」应用小技巧（二）：快速调整图片尺寸](https://sspai.com/post/27674)

[Mac「预览」应用小技巧（三）：PDF 文档页面重排和拼接](https://sspai.com/post/27675)

[macOS + 那些强大的「预览」（Preview）插件](https://zhuanlan.zhihu.com/p/28924757)

[Quick Look plugins](https://github.com/sindresorhus/quick-look-plugins)