---
layout: post
title:  "Traceback (most recent call last) from /usr/local/bin/bundle "
category: "jekyll"
tags: ["bundle", "gem", "ruby", "jekyll"]
date: 2018-11-08 00:00:00
updated: 2018-11-08 00:00:00
---

在某次清理完电脑之后，发现运行 Jekyll 爆错了

<!-- more -->

```shell
$ bundle exec jekyll serve
Traceback (most recent call last):
	1: from /usr/local/bin/bundle:23:in `<main>'
/usr/local/bin/bundle:23:in `load': cannot load such file -- /usr/local/lib/ruby/gems/2.5.0/gems/bundler-1.16.6/exe/bundle (LoadError)
```

然后我开始找原因

```shell
$ gem -v
2.5.2.3
$ ruby --version
ruby 2.3.7p456 (2018-03-28 revision 63024) [universal.x86_64-darwin18]
$ bundle -v
Traceback (most recent call last):
	1: from /usr/local/bin/bundle:23:in `<main>'
/usr/local/bin/bundle:23:in `load': cannot load such file -- /usr/local/lib/ruby/gems/2.5.0/gems/bundler-1.16.6/exe/bundle (LoadError)
```

这么一看发现是 bundle 的问题

```shell
$ sudo gem install bundler
Password:
Fetching: bundler-1.17.1.gem (100%)
Successfully installed bundler-1.17.1
Parsing documentation for bundler-1.17.1
Installing ri documentation for bundler-1.17.1
Done installing documentation for bundler after 5 seconds
1 gem installed

$ bundle -v
Bundler version 1.17.1
```

OK👌，现在可以启动了

```
$ bundle exec jekyll serve
Could not find public_suffix-3.0.3 in any of the sources
Run `bundle install` to install missing gems.
```

我勒个去，又爆错了，然后跟着提示，运行下面的命令

```
$ bundle install
```

现在终于解决了！完美！！！