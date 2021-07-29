---
layout: post
title: 天才排序算法——睡眠排序
categories: [代码]
tags: [算法, 排序算法]
date: 2018-02-19 00:00:00
updated: 2018-02-19 00:00:00
---

今天看到一个新的排序法 睡排序 真的是脑洞大开。。。

据说是 4chan 匿名用户发的一个帖子《Genius sorting algorithm: Sleep sort》，原贴已删除。

![4chan](https://up-img.yonghong.tech/pic/2021/07/29-13-20-sleep-sort-NgnMIZ.jpg)

Man, am I a genius. Check out this sorting algorithm I just invented.
朋友，我真是个天才，快来看看我刚发明的排序算法。

<!-- more -->

```bash
#!/bin/bash
function f() {
    sleep "$1"
    echo "$1"
}
while [ -n "$1" ]
do
    f "$1" &
    shift
done
wait

example usage:
./sleepsort.bash 5 3 6 3 6 3 1 4 7
```

> 估计有大部分人不知道把，原理是构造 n 个线程，它们和这 n 个数一一对应。初始化后，线程们开始睡眠，等到对应的数那么多个时间单位后各自醒来，然后输出它对应的数。这样最小的数对应的线程最早醒来，这个数最早被输出。等所有线程都醒来，排序就结束了。

再帖几个其他常用版本：

Java 版

```java
public class SleepSort {  
    public static void main(String[] args) {  
        int[] ints = {1,4,7,3,8,9,2,6,5};  
        SortThread[] sortThreads = new SortThread[ints.length];  
        for (int i = 0; i < sortThreads.length; i++) {  
            sortThreads[i] = new SortThread(ints[i]);  
        }  
        for (int i = 0; i < sortThreads.length; i++) {  
            sortThreads[i].start();  
        }  
    }  
}  
class SortThread extends Thread{  
    int ms = 0;  
    public SortThread(int ms){  
        this.ms = ms;  
    }  
    public void run(){  
        try {  
            sleep(ms*10+10);  
        } catch (InterruptedException e) {  
            // TODO Auto-generated catch block  
            e.printStackTrace();  
        }  
        System.out.println(ms);  
    }  
}  
```

PHP 版

```php
<?php  
$pids = array();  
for ($i=1; $i<$argc; $i++)  
{  
        if (($pid = pcntl_fork()) == 0)  
        {  
                $sleep = intval($argv[$i]);  
                sleep($sleep);  
                echo $sleep."\n";  
                exit();  
        }  
        else if ($pid == -1)  
        {  
                die();  
        }  
        else  
        {  
                $pids[] = $pid;  
        }  
}  
  
foreach($pids as $pid)  
        pcntl_waitpid($pid, $status);  
?>  
  
php sleepsort.php 1 3 5 6 2  
```

JavaScript 版

```js
function lazySort(list, callback) {  
    var result = [];  
  
    list.forEach(function(i) {  
        setTimeout(function() {  
            result.push(i);  
              
            if(result.length == list.length) {  
                callback(result);  
            }  
        }, i);  
    });  
}  
  
lazySort([4,5,7,1,2,4,5], alert);  
```

Ruby 版

```ruby
ARGV.each { |e| fork { sleep(e.to_f/1000); puts e } }  
```

下面👇是转载的一些评论：

路人A：

> Oh god, it works.  
But I don't like to wait 218382 seconds to sort '(0 218382)  
哦，春哥，它居然能用，但我不想用218382秒去排(0 218382)  



路人B：

> If the difference between any two of the numbers is too small, race conditions will fuck you up the ass.  
如果两个数之间的差距太小，竞态条件就要爆你菊花了。


路人C：

> What about   
./sleepsort -1 -2 -3 ?  
If you slept exp(n) instead of n it could easily include negative integers too!  
排-1 -2 -3怎么办？如果你睡exp(n)而不是n，它就能包含负数了。  



路人D：

> Someone email this to Knuth  
你可以给Knuth发邮件了 



路人E：

> I think thats brilliant :)  
Would be fun to design a hardware sorter, based on this..  
这招挺高，可以根据这个设计一个硬件排序器  



路人F：

> This has a best case O(n) and an infinity high worst case. (because its 0(n * Constant) and the constant could be much greater than n)  
它有一个最好的O(n)的时间复杂度和一个无穷大的最坏复杂度，因为这个常数可能比n大的多的多  



路人G：

> I heartily disagree with all the attempts to downplay the brilliance of the sleep sort algorithm. Many of you have missed the important point that while traditional sorting algorithms can only utilize one core, sleep sort has the capacity to use the full power of a massively parallel execution environment.
Given that you need nearly no computing in each of the threads, you can implement them using low-power CPUs, so this is in fact a GREEN COMPUTING algorithm.  
Oh, and did I mention that the algorithm can also run inside a cloud...?
Sure, you're a genius!  
我由衷的不同意那些低估sleepsort这个天才算法的举动，许多人可能忽略了一个重点那就是传统的排序只能利用一个核心，而sleepsort有这个能力充分利用可以做大量并行计算的环境。  
在每个线程中给出你几乎不需要计算的部分，你可以用低性能CPU搞定它们，所以事实上，这是一个“绿色计算”算法。  
还有我提到的这个方法能在云端运行不？  
总之，你是个天才！  


路人H：

> pretty fucking cool !  
真是太TM的cool了！  