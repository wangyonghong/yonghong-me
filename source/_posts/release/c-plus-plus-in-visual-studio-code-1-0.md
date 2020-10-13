---
title: Visual Studio Code 的 C++ 扩展迎来首个正式版本（v1.0）!
tags:
- release
- C++
- Visual Studio Code
- vscode
categories:
- release
date: 2020-09-27 21:00:00
updated: 2020-09-27 21:00:00
---

微软最近[宣布](https://devblogs.microsoft.com/cppblog/c-in-visual-studio-code-reaches-version-1-0/) Visual Studio Code 的 C++ 扩展已达到 1.0 稳定版本。C++ 扩展为 C++ 开发人员带来了包括 IntelliSense 智能代码补全、调试、重构、代码导航等在内的功能。这些功能可适应多个平台、架构和编译器，从而实现各种交叉编译和远程开发方案。 

VS Code C++ 扩展 1.0 版本的一大亮点是对 ARM Linux 和 ARM 64 的支持，并提供了 IntelliSense 以及远程构建和调试支持。现在用户可以使用 VS Code 和 Remote-SSH 在 Raspberry Pi 上构建 C++ 应用程序。

另外，此发行版附带了一个[教学视频](https://aka.ms/cpp-intelliSense)，用来告诉大家如何配置 C++ IntelliSense。

<!-- more -->

原文如下：

We’re excited to announce the first generally available release of the **C++ extension for Visual Studio Code**! Visual Studio Code is a free code editor that runs on Linux, macOS, and Windows, and is highly-customizable to make it exactly what you want it to be.

The C++ extension brings a rich set of productivity features to VS Code for C++ developers, including IntelliSense smart code completion, debugging, refactoring, code navigation, and more! On top of that, these features are adaptable to various platforms, architectures and compilers, enabling all your cross-compiling and remote development scenarios.

Throughout the years, our customers have helped shape the direction of C++ development in VS Code by asking for key features and reporting bugs. The version 1.0 of the C++ extension for Visual Studio Code delivers these features in high quality. You asked, we listened.

## Editing

When it comes to editing, the C++ extension provides an abundance of productivity features to boost your coding efficiency. To name a few, the extension comes with:

- IntelliSense: code completion, parameter info, quick info, and member lists
- Code navigation: Find All References, Go to Definition/Declaration, Peek Definition/Declaration
- Refactoring support: Rename Symbol
- Code formatting
- Semantic colorization, which provides colorization to variables even when they are used outside of the scope in which they are declared
- Doxygen comment documentation

![Screenshot of member list from C++ IntelliSense engine](https://up-img.yonghong.tech/pic/2020/09/27-11-38-editing-screenshot-02eKoJ.png)

## Debugging

Visual Studio Code’s built-in debugger UI launches your C++ debugger of choice under the hood, creating an intuitive, yet customizable, debugging experience across Linux, macOS, and Windows. With the C++ extension’s debugger, you can:

- Set breakpoints (conditional, unconditional, and function breakpoints)
- Set watch variables
- Step through your program
- Debug multi-threaded programs
- Debug a remote process
- And more!

![Screenshot showing C++ debug session in VS Code](https://up-img.yonghong.tech/pic/2020/09/27-11-38-debug-screenshot-nEYKCp.png)

The C++ extension 1.0 also includes all our recent fixes to previous issues with the debugger, such as:

- Support for macOS Catalina (GitHub issue [#3829](https://github.com/microsoft/vscode-cpptools/issues/3829))
- Support for modifying conditional breakpoints while debugging (cppdbg) (GitHub issue [#2297](https://github.com/microsoft/vscode-cpptools/issues/2297))
- Watch local variables support for LLDB (GitHub issue [#1768](https://github.com/microsoft/vscode-cpptools/issues/1768))

## What’s new in 1.0?

### Support for Linux on ARM and ARM64

We’re excited to announce that version 1.0 of the C++ extension brings a first-class development experience for Linux on ARM and ARM64, complete with IntelliSense and remote build and debug support. You can now develop C++ applications on Raspberry Pi with VS Code and Remote-SSH!

### Easy IntelliSense configuration

We know that configuring C++ IntelliSense hasn’t always been easy. So, we’ve created a [video tutorial](https://aka.ms/cpp-intelliSense) to help you out. Get rid of your error squiggles in minutes!

### Customizable code formatting

Version 1.0 of the C++ extension brings a new, rich set of C++ formatting settings. All C++ code formatting settings from the Visual Studio IDE are now supported in VS Code. What’s more, the C++ extension has built-in [EditorConfig](https://docs.microsoft.com/en-us/visualstudio/ide/cpp-editorconfig-properties?view=vs-2019) support for all these new settings, giving you more control and flexibility with code formatting than ever before.

### C++ extension pack

To make it as easy as possible to take full advantage of everything Visual Studio Code has to offer—remote development, GitHub integration, first-class CMake support to name a few—we’ve created a [C++ Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools-extension-pack) for you. The extension pack includes:

- C/C++
- C/C++ Themes
- CMake
- CMake Tools
- Remote Development Extension Pack
- GitHub Pull Requests and Issues
- Visual Studio Codespaces
- LiveShare Extension Pack
- Doxygen Documentation Generator
- Better C++ Syntax

### Quality

If you haven’t tried Visual Studio Code with C++ in a while, it is time to give it another go. Our team has been hard at work for months fixing a myriad of reported issues and the C++ extension is now better for it. For example, we’ve addressed nine [performance-related GitHub issues](https://github.com/microsoft/vscode-cpptools/issues?q=is%3Aissue+is%3Aclosed+label%3Aperformance+label%3A"fixed+(release+pending)"+sort%3Aupdated-desc) in the past nine months. In fact, many VS Code extensions build off of the C++ extension’s high quality IntelliSense engine, such as [PlatformIO IDE](https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide), a popular extension for embedded development in VS Code. Version 1.0 of the C++ extension meets the high bar we, and our customers, have set for quality—but we won’t stop there. Performance will continue to be a prioritization for the C++ extension.

## Give it a try

Install the [C/C++ Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools-extension-pack), check out the new [*Configure C++ IntelliSense in Visual Studio Code* video tutorial](https://aka.ms/cpp-intelliSense), and let us know what you think! You can also find Hello World build and debug tutorials for different compilers and platforms in the [VS Code C++ documentation](https://aka.ms/cpphelloworld).

If you run into any issues, or have any suggestions, please report them in the [Issues section of our GitHub repository](https://github.com/Microsoft/vscode-cpptools/issues). You can also join our Insiders program and get access to early builds of our release by going to **File > Preferences > Settings** and under **Extensions > C/C++,** change the “C_Cpp: Update Channel” to “Insiders”.

We can be reached via the comments below or in email at [visualcpp@microsoft.com](mailto:visualcpp@microsoft.com). You can also find our team on Twitter at [@VisualC](https://twitter.com/visualc).


