---
layout: post
title:  "Linux 面试 Top10 题目"
category: "linux"
tags: ["linux"]
date: 2019-01-28 00:00:00
updated: 2019-01-28 00:00:00
---

#### 1.How to check the kernel version of a Linux system?

<!-- more -->

```
uname -a
```

```shell
Print certain system information.  With no OPTION, same as -s.

  -a, --all                print all information, in the following order,
                             except omit -p and -i if unknown:
  -s, --kernel-name        print the kernel name
  -n, --nodename           print the network node hostname
  -r, --kernel-release     print the kernel release
  -v, --kernel-version     print the kernel version
  -m, --machine            print the machine hardware name
  -p, --processor          print the processor type or "unknown"
  -i, --hardware-platform  print the hardware platform or "unknown"
  -o, --operating-system   print the operating system
      --help     display this help and exit
      --version  output version information and exit
```

#### 2.How to see the current IP address on Linux?

```
ifconfig
```

lo0: 回环地址。一般回环接口的 ipv4 地址为:127.0.0.1，子网掩码：255.255.255.0

虚拟网络接口:并非真实存在，并不真实地从外界接收和发送数据包，而是在系统内部接收和发送数据包，因此虚拟网络接口不需要驱动程序。

为什么会有该接口？ 
如果包是由一个本地进程为另一个本地进程产生的, 它们将通过外出链的lo接口,然后返回进入链的 lo 接口

eth0: 以太网接口。

以太网接口与网卡对应，每个硬件网卡(一个 MAC )对应一个以太网接口，其工作完全由网卡相应的驱动程序控制。

如果物理网卡只有一个，而却有 eth1，eth2 等，则可能存在无线网卡或多个虚拟网卡，虚拟网卡由系统创建或通过应用层程序创建，作用与物理网卡类似。

venet0: OpenVZ 虚拟出来的 VPS 默认是没有 eth0，只有 venet0 或 venet0-00

```
ip addr show
```

这个命令看 ip 地址可能会更好一些


#### 3.How to check for free disk space in Linux?

```
df -ah
```

#### 4.How to see if a Linux service is running?

```
service udev status 旧系统
systemctl status udev 新系统
```

#### 5.How to check the size of a directory in Linux?

```
du -sh code/
```

-s --summarize 

-h --human-readable

#### 6.How to check for open ports in Linux?

```
netstat -tulpn
```

#### 7.How to check Linux process information (CPU usage, memory, user information, etc.)?

```
ps aux | grep nginx
```

```
top -d secs -n max -u user -p pid 
```

```
htop
```
F3 查找 F4过滤 F5tree F6SortBy F9Kill


#### 8.How to deal with mounts in Linux

将 /dev/hda1 挂在 /mnt 之下。

```
mount /dev/hda1 /mnt
```

只读方式

```
mount -o ro /dev/hda1 /mnt
```

#### 9.Man pages

```
man <command>
```

#### 10.Other resources

[https://www.google.com/](https://www.google.com/)

---

#### 参考

[https://www.youtube.com/watch?v=l0QGLMwR-lY](https://www.youtube.com/watch?v=l0QGLMwR-lY)