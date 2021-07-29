---
layout: post
title:  "LeetCode 232. 用栈实现队列"
category: "leetcode"
tags: ["leetcode", "algorithm", "queue", "stack"]
date: 2018-11-21 00:00:00
updated: 2018-11-21 00:00:00
---

原题链接：

https://leetcode.com/problems/implement-queue-using-stacks/description/

https://leetcode-cn.com/problems/implement-queue-using-stacks/description/

这道题其实比较简单，题目要求就是用栈实现一个队列。

<!-- more -->

我们考虑有两个栈，一个输入栈，一个输出栈。

放数据永远放入输入栈，取数据永远从输出栈取。

输出栈为空的时候把把输入栈的数据一次性取出来放到输出栈。

下面是 Java 和 Python 的代码

Java


```java
class MyQueue {

    private Stack<Integer> input = null;
    private Stack<Integer> output = null;
    
    /** Initialize your data structure here. */
    public MyQueue() {
        
        input = new Stack<>();
        output = new Stack<>();
        
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        input.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        if(output.isEmpty()) {
            while(!input.isEmpty()) {
                output.push(input.pop());
            }
        }
        return output.pop();
    }
    
    /** Get the front element. */
    public int peek() {
        if(output.isEmpty()) {
            while(!input.isEmpty()) {
                output.push(input.pop());
            }
        }
        return output.peek();
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return input.isEmpty() && output.isEmpty();
    }
}
```

Python


```python
class MyQueue:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.instack = []
		self.outstack = []
		

	def push(self, x):
		"""
		Push element x to the back of queue.
		:type x: int
		:rtype: void
		"""
		self.instack.append(x)
		

	def pop(self):
		"""
		Removes the element from in front of queue and returns that element.
		:rtype: int
		"""
		if not self.outstack:
			while self.instack:
				self.outstack.append(self.instack.pop())
		return self.outstack.pop()
		

	def peek(self):
		"""
		Get the front element.
		:rtype: int
		"""
		if not self.outstack:
			while self.instack:
				self.outstack.append(self.instack.pop())
		return self.outstack[-1]
		

	def empty(self):
		"""
		Returns whether the queue is empty.
		:rtype: bool
		"""
		return not self.outstack and not self.instack

```