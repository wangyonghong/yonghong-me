---
layout: post
title: OpenCV + CodeBlocks 环境配置
date: 2018-03-23 00:00:00
updated: 2018-03-23 00:00:00
---

OpenCV 在 3.X 的版本以后就不提供 MinGW 的编译版本了，所以要想用 CodeBlocks 来进行 OpenCV 的编程就需要自己手动编译 OpenCV。并且需要注意的是 OpenCV 在 3.X 的版本以后就必须使用 MinGW 的64位版本，因此用 CodeBlocks 自带的 MinGW 显然是行不通的。

<!-- more -->

最终我仍然没能自己编译成功。用了网上编译好的一个 OpenCV MinGW 版本。

1.下载 MinGW 的 **64位版本！** **64位版本！** **64位版本！**。

[tdm-gcc](http://tdm-gcc.tdragon.net/download)

或者 [tdm64-gcc-5.1.0-2.exe](https://pan.lanzou.com/i0piqyd)。

解压到 C:/ 根目录

2.下载编译好的 [OpenCV 3.1版本](https://pan.lanzou.com/i0piqpe) 

解压到 C:/ 根目录

3.将 opencv 文件夹的 x64/mingw/bin 添加到系统环境变量 PATH 中。

4.更改 codeblocks 的设置

![](https://up-img.yonghong.tech/pic/2021/07/29-16-52-1-YDjKne.png)

Settings -> Compiler -> Toolchain executables -> Compiler's installation directory

改为 MinGW 的目录即刚刚下载的 C:\TDM-GCC-64 

保存设置 OK 

5.新建一个工程，新建工程的目的在于 OpenCV 的设置不会对其他工程产生影响。

Project -> Build Options 

![](https://up-img.yonghong.tech/pic/2021/07/29-16-52-2-6QvXWW.png)

Linker Settings 将 opencv 文件夹的 x64\mingw\lib 里的文件都添加进来

![](https://up-img.yonghong.tech/pic/2021/07/29-16-52-3-rgk0iM.png)

Search directories -> Compilers 把 opencv\include 添加进来

![](https://up-img.yonghong.tech/pic/2021/07/29-16-52-4-KALj1H.png)

Search directories -> Linker 把 opencv\x64\mingw\bin 添加进来

保存设置 OK 

这种方式要求每次新建一个工程都要进行这些操作。



6.测试程序

将一张图片放在工程文件夹里，假设名称为 im.jpg

```c++
#include <opencv2/opencv.hpp>
using namespace cv;

int main(int argc, char** argv) {
    Mat image;
    image = imread("./im.jpg");
    namedWindow("Display Image", WINDOW_AUTOSIZE);
    imshow("Display Image", image);
    waitKey(0);
    return 0;
}
```

运行成功 ！
