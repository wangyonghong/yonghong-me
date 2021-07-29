---
layout: post
title:  "Jekyll 分页"
category: "Jekyll"
tags: ["Jekyll", "paginate", "分页"]
date: 2018-10-27 00:00:00
updated: 2018-10-27 00:00:00
---


### 修改 `Gemfile` 文件，在文件末尾追加

```
gem "jekyll-paginate"
```

<!-- more -->

如果没有追加这一句的话就会出现下面的报错


> Dependency Error: Yikes! It looks like you don't have jekyll-paginate or one of its dependencies installed. In order to use Jekyll as currently configured, you'll need to install this gem. The full error message from Ruby is: 'cannot load such file -- jekyll-paginate' If you run into trouble, you can find helpful resources at https://jekyllrb.com/help/! 


### 修改 `_config.yml` 文件

这个很好理解，就是在 yml 文件中添加这个插件，并且规定每页的数量和每页的链接

```yml
plugins:
  - jekyll-paginate

paginate: 10
paginate_path: "blog/page:num"
```

### 修改 `index.html` 文件

```html
{% raw %}
---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default	
pagination: 
  enabled: true
---

<!-- This loops through the paginated posts -->
{% for post in paginator.posts %}
  <h1><a href="{{ post.url }}">{{ post.title }}</a></h1>
  <p class="author">
    <span class="date">{{ post.date | date_to_rfc822 }}</span>
  </p>
  <div class="content">
    {{ post.content | strip_html |truncate:210,'...' }}
  </div>
  <br>
{% endfor %}

<br><hr><br>

<!-- Pagination links -->
<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path }}" class="previous">
      Previous
    </a>
  {% else %}
    <span class="previous">Previous</span>
  {% endif %}
  <span class="page_number ">
    Page: {{ paginator.page }} of {{ paginator.total_pages }}
  </span>
  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path }}" class="next">Next</a>
  {% else %}
    <span class="next ">Next</span>
  {% endif %}
</div>
{% endraw %}
```

### 在本地运行

如果想在本地运行的话，就要执行下面这条命令来安装依赖包

```shell
gem install jekyll-paginate
```
或者

```shell
bundle install
```

如果不执行的话就会出现下面的报错


```
Could not find jekyll-paginate-1.1.0 in any of the sources
Run `bundle install` to install missing gems.
```

