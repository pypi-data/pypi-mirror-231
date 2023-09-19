## **库的介绍及用法：**

### **简单介绍：**

1.  库(**ahui**)由作者**阿辉**开发并维护，不定期发布更新版本 [查看最新版本>>](https://pypi.org/project/ahui/)
2.  该库的模块及函数覆盖实际工作中的多种场景的应用，函数的开发基于原标准库中的模块、调用第三方接口实现、原始函数的二次开发应用等
3.  本文档列举了库中所有模块下的函数及要点注解，更多详细教程可访问作者(阿辉)博客：**[CSDN](https://blog.csdn.net/weixin_44007104)  [知乎](https://www.zhihu.com/people/ahui6888)**

### **基本用法：**

1.  安装库 (以下方法默认安装最新版本)：&#x20;

    *   `pip install ahui`

        &#x20;

2.  调用库或模块：

    *   `import ahui`
    *   `from ahui import pyemail,pywechat`
    *   注：因部分依赖库没有加入到默认安装列表，调用时可根据报错提示安装所缺少的\<module>

        &#x20;

3.  调用库(**ahui**)时默认导入各模块下的所有函数，故可以直接调用库下的函数，示例如下：

    ```python
    import ahui

    ahui.Email_send(username='your_email', password='email_password', subject='test', contents='test...', receivers=['receiver_email'], accs=[], links={}, df=None, df_links={}, file_pathname=None, smtp='exmail', ssl=True)
    ```

&#x20;

***

&#x20;

## **一、Python 发送邮件的多种场景的应用**

### **0.邮箱-SMTP服务器地址/端口号(SSL加密)/端口号(非加密)：**

*   注：qq(腾讯QQ邮箱)、exmail(腾讯企业邮箱)、126和163(网易邮箱)

    ```python
    smtp_servers(smtp='exmail', ssl=True)
    ```

### **1.发送邮件信息：**

*   参数：\[file\_pathname]类型(str/list) 支持添加多个附件-文件格式不限、附件总大小不超过50M；\[contents]类型(str/list) 支持正文内容换行(列表中一个元素代表一行)；\[links]设置超链接-支持添加多个；\[df\_links]支持设置多个链接字段，默认为空。
*   设置：\[QQ邮箱发送]用于发送邮件的qq邮箱需要开启SMTP服务，进入邮箱-设置-账户-开启(POP3/SMTP)验证-获取授信码(授信码用于邮箱登录密码)

    ```python
    Email_send(username='', password='', subject='', contents='', receivers=[], accs=[], links={}, df=None, df_links={}, file_pathname=None, smtp='exmail', ssl=True)
    ```

### **2.发送邮件报告：**

*   功能：支持正文插入1张图片(png/jpg/gif动图); 支持添加多个附件(文件格式不限)
*   参数：\[image\_name]支持类型(本地图片/变量Image/变量bytes)；\[file\_pathname]类型(str/list) 支持添加多个附件-文件格式不限、附件总大小不超过50M；\[contents]类型(str/list) 支持正文内容换行(列表中一个元素代表一行)
*   说明：插入动图浏览器中首次打开正常，但手机端需要二次打开邮件才显示动图(刷新邮件)

    ```python
    Email_image(username='', password='', title='', contents='', image_name=None, receivers=[], accs=[], file_pathname=None, smtp='exmail', ssl=True, sign=False)
    ```

&#x20;

***

&#x20;

## **二、企业微信群机器人-推送多类型消息的应用**

### **0.配置企业微信群机器人key：**

```python
wechat_key(key='key1')
```

### **1.1.企业微信群机器人-推送消息类型-markdown：**

*   参数：\[content]支持传入字符串(str)/列表(list)/数据框(DataFrame)；\[df\_links]支持多个链接字段，默认参数空；
*   说明：只支持@1个人/不支持@all；@对象为企业微信英文名，英文名不区分大小写；若@对象无此人仍正常推送消息内容；
*   系统：适用于 Windows、Linux 系统环境下的Python3版本。

```python
wechat_markdown(top='', title='', content='', user='', links={}, df_links={}, show_cols=False, key=None)
```

### **1.2.企业微信群机器人-推送消息类型-markdown：**

*   简介：基于 wechat\_markdown() 函数的二次封装开发；功能上支持@多人、支持推送多个群；
*   参数：\[user]支持传入数据类型str/list； \[key]支持数据类型str/list，当传入多个元素则用列表形式。

```python
wechat_markdowns(top='', title='', content='', user='', links={}, df_links={}, show_cols=False, key=None)
```

### **2.企业微信群机器人-推送消息类型-text：**

*   功能：@对象支持使用企业微信英文名或手机号、支持 '@all' 或 @多个人；
*   参数：\[content]支持数据类型str/list，列表中的每个元素文本代表一行。

```python
wechat_text(top='', title='', content='', users_name=[], users_phone=[], key=None)
```

### **3.企业微信群机器人-推送消息类型-@群成员：**

*   功能：@对象支持使用企业微信英文名或手机号，英文名不区分大小写；支持 '@all' 或 @多个人，若无此人则不@且不影响执行推送。

    ```python
    wechat_at(users_name=[], users_phone=[], key=None, content='')
    ```

### **4.企业微信群机器人-推送消息类型-图像：**

*   参数：\[image]支持传入的数据类型-本地图片路径/变量Image/变量bytes
*   说明：图片最大不能超过2M，支持JPG、PNG格式。
*   安装：PIL(pip install pillow)

```python
wechat_image(image, key=None, users=[], content='')
```

### **5.企业微信群机器人-推送消息类型-本地文件：**

*   参数：\[pathfile]传参要求，图片:最大10MB 支持JPG、PNG格式；语音:最大2MB 播放长度不超过60s 支持AMR格式；视频:最大10MB 支持MP4格式；普通文件:最大20MB

```python
wechat_file(pathfile, key=None, users=[], content='')
```

&#x20;
