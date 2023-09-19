# -*- coding: utf-8 -*-
# 从库中导入模块：
try:
    from ahui import pywechat
    from ahui import pyemail
except Exception as e:
    print(e)


# 从库中的模块中导入函数：
try:
    from ahui.pyemail import (
        Email_send,
        Email_image)

    from ahui.pywechat import (
        wechat_markdown,
        wechat_markdowns,
        wechat_text,
        wechat_at,
        wechat_image,
        wechat_file)
except Exception as e:
    print(e)


# 相关教程：
blog_csdn = 'https://blog.csdn.net/weixin_44007104'
blog_zhihu = 'https://www.zhihu.com/people/ahui6888'
blogs = f'☆更多教程见作者(阿辉)博客：\nCSDN: {blog_csdn}\n知乎: {blog_zhihu}'
print(blogs)