# Python 发送邮件的多种场景的应用
# 函数应用教程见作者(阿辉)博客：https://blog.csdn.net/weixin_44007104


# 0.邮箱-SMTP服务器地址/端口号(SSL加密)/端口号(非加密)：
# 注：qq(腾讯QQ邮箱)、exmail(腾讯企业邮箱)、126和163(网易邮箱)
def smtp_servers(smtp='exmail', ssl=True):
    servers = {'qq' : ('smtp.qq.com', 465, 25),
               'exmail' : ('smtp.exmail.qq.com', 465, 25),
               '126' : ('smtp.126.com', 465, 25),
               '163' : ('smtp.163.com', 465, 25)
               }
    server = servers[smtp][0]
    if ssl==True:
        port = servers[smtp][1]
    else:
        port = servers[smtp][2]
    return server,port


# 1.发送邮件信息：
# 参数：[file_pathname]类型(str/list) 支持添加多个附件-文件格式不限、附件总大小不超过50M；[contents]类型(str/list) 支持正文内容换行(列表中一个元素代表一行)；[links]设置超链接-支持添加多个；[df_links]支持设置多个链接字段，默认为空。
# 设置：[QQ邮箱发送]用于发送邮件的qq邮箱需要开启SMTP服务，进入邮箱-设置-账户-开启(POP3/SMTP)验证-获取授信码(授信码用于邮箱登录密码)
def Email_send(username='', password='', subject='', contents='', receivers=[], accs=[], links={}, df=None, df_links={}, file_pathname=None, smtp='exmail', ssl=True):

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib,re

    # 设置smtplib所需的参数:
    server,port = smtp_servers(smtp=smtp, ssl=ssl)
    sender = username
    fromname = sender.split('@')[0] + ' <{}>'.format(sender)   # 'Hexxx.sun <Hexxx.sun@wetax.com.cn>'
    receiver = receivers + accs    # 接收人

    # 邮件页面设置-只是显示：(主题，发件人/收件人-允许为空)
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = fromname
    msg['To'] = ";".join(receivers)
    msg['Cc'] = ";".join(accs)

    # 以下设置：正文内容、邮件签名、传入参数(<br/>换行作用)
    message = '''
        <html>
        <body>
        <font size="4">Dear,</font><br/>
        <font size="1">&nbsp</font><br/>
        <font size="3">&nbsp&nbsp&nbsp&nbsp content</font><br/>
        <font size="1">&nbsp</font><br/>
        <font size="3">&nbsp&nbsp&nbsp&nbsp words_df</font><a href="link_df">linkname_df</a><br/>
        <font size="1">&nbsp</font><br/>
        <font size="3">&nbsp&nbsp&nbsp&nbsp&nbsp</font><a href="link">linkname</a><br/>
        <p>&nbsp</p>
        </body>
        </html>'''

    msgs = message.split('\n')
    lsq5 = msgs[:5]  # 头部
    mstr = msgs[5]   # content
    kg_1 = msgs[6]   # 空行
    w_df = msgs[7]   # df
    kg_2 = msgs[8]   # 空行
    lstr = msgs[9]   # link
    lsh3 = msgs[-3:] # 尾部

    if isinstance(contents,str):
        conts = [contents]
    elif isinstance(contents,list):
        conts = contents
    else:
        raise TypeError('contents type is wrong!')

    if df is not None:
        df = df.copy()
        columns = list(df.columns)
        for c in columns:
            df[c] = df[c].astype(str)

        if len(df_links):
            link_cols,link_names = [],[]
            for link_col,link_name in df_links.items():
                colname = f'link_name_{link_col}'
                df[colname] = link_name
                link_cols.append(link_col)
                link_names.append(colname)

            columns = [c for c in columns if c not in link_cols]

        df['combine'] = ''
        for c in columns:
            df['combine'] = df['combine'] + ' | ' + df[c]
        df['combine'] = df['combine'] + ' | '

        w_dfs = []
        if len(df_links):
            wds1 = []
            for link_col,link_name in zip(link_cols, link_names):
                w_ds = []
                for link,linkname in zip(df[link_col], df[link_name]):
                    w_d = '<a href="link_df">linkname_df</a> | '.replace('link_df', link).replace('linkname_df', linkname)
                    w_ds.append(w_d)
                wds1.append(w_ds)
            wds1 = [''.join(item) for item in zip(*wds1)]

            wds2 = []
            for words in df['combine']:
                w_d = w_df.replace('words_df', words).replace('<a href="link_df">linkname_df</a>', 'links_names')
                wds2.append(w_d)

            w_dfs = [j.replace('links_names',i) for i,j in zip(wds1,wds2)]
        else:
            for words in df['combine']:
                w_d = w_df.replace('words_df', words).replace('<a href="link_df">linkname_df</a>', '')
                w_dfs.append(w_d)

    mstrs = []
    for i in conts:
        i = str(i).replace('\\','\\\\')           # 消除转义字符\ 以免下面报错(特殊字符会报错)
        s = re.sub('content', str(i), mstr)       # i中若有\x会报错!
        mstrs.append(s)

    link_hs = []
    for key,value in links.items():
        link_key = str(key).replace('\\','\\\\')
        link_value = str(value).strip()
        link_h = lstr.replace('linkname',link_key).replace('link',link_value)
        link_hs.append(link_h)

    if df is not None:
        ls_msg = lsq5 + mstrs + [kg_1] + w_dfs + [kg_2] + link_hs + lsh3
    else:
        ls_msg = lsq5 + mstrs + [kg_1] + link_hs + lsh3
    message = '\n'.join(ls_msg)

    # 邮件对象: （三个参数：文本内容、plain 设置文本格式、utf-8 设置编码）
    msg.attach(MIMEText(message, 'html', 'utf-8'))

    # 添加附件-名称支持英文/数字/符号：(中文名称在foxmail的pc端、QQ邮箱的pc与手机端都正常，但在foxmail手机端名称显示为UrlDdecode编码)
    if file_pathname != None:
        if isinstance(file_pathname, str):
            files = [file_pathname]
        else:
            files = file_pathname
        for f in files:
            fname = f.split('\\')[-1]     # 支持路径的两种斜杠/\形式
            fname = fname.split('/')[-1]
            att = MIMEText(open(r'{}'.format(f), 'rb').read(), 'base64', 'utf-8')  # 编码参数不可省略！
            att["Content-Type"] = 'application/octet-stream'
            att.add_header('Content-Disposition', 'attachment', filename=fname)   # fname-附件的文件名称(test.png)
            msg.attach(att)

    # 发送邮件：
    if ssl==True:
        smtp = smtplib.SMTP_SSL(server, port)   # 安全连接(加密发送)
    else:
        smtp = smtplib.SMTP(server, port)       # 普通连接(未加密发送)
    try:
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())  # receiver(接收人+抄送人)中若无有效邮箱则报错; 若至少有1个有效邮箱则发送成功(自动跳过无效邮箱)
        smtp.quit()
        print(f'[发送成功]{subject}')
    except Exception as e:
        if 'Mailbox not found' in str(e):
            print(f'接收信息的邮箱无效！\n{receiver}')
        elif 'authentication failed' in str(e):
            print('发送信息的邮箱账号或密码有误！')
        else:
            print(e)



# 2.发送邮件报告：
# 功能：支持正文插入1张图片(png/jpg/gif动图); 支持添加多个附件(文件格式不限)
# 参数：[image_name]支持类型(本地图片/变量Image/变量bytes)；[file_pathname]类型(str/list) 支持添加多个附件-文件格式不限、附件总大小不超过50M；[contents]类型(str/list) 支持正文内容换行(列表中一个元素代表一行)
# 说明：插入动图浏览器中首次打开正常，但手机端需要二次打开邮件才显示动图(刷新邮件)
def Email_image(username='', password='', title='', contents='', image_name=None, receivers=[], accs=[], file_pathname=None, smtp='exmail', ssl=True, sign=False):

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    from datetime import datetime
    import smtplib,PIL,os,re

    # 设置smtplib所需的参数：
    server,port = smtp_servers(smtp=smtp, ssl=ssl)
    sender= username
    fromname = sender.split('@')[0] + ' <{}>'.format(sender)
    receiver = receivers + accs

    # 邮件页面设置：（主题，发件人，收件人，日期）
    msg = MIMEMultipart()
    msg['Subject'] = title
    msg['From'] = fromname
    msg['To'] = ";".join(receivers)
    msg['Cc'] = ";".join(accs)

    # 正文插入图片：
    mime = MIMEBase('image', 'png')

    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment')  # 自定义文件名称
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')

    # 根据参数image_name的类型判断本地文件/变量bytes：
    if isinstance(image_name, str):
        image_name = open(image_name, 'rb').read()   # 读取本地图片-bytes
    elif isinstance(image_name, bytes):
        print('image_name is bytes')
    elif isinstance(image_name, PIL.Image.Image):
        filename = 'report_' + str(datetime.now()).replace(':','') + '.png'
        image_name.save(filename)
        image_name = open(filename, 'rb').read()  # bytes
        os.remove(filename)
        print('image_name is Image')
    else:
        raise TypeError('image_name type is wrong!')

    # 读取本地文件:（若不执行html，mime的文件就会被添加到附件中）
    mime.set_payload(image_name)  # bytes
    encoders.encode_base64(mime)
    msg.attach(mime)

    # 若不执行以下代码：mime的文件就会被添加到附件中（若执行，mime的文件会被插入正文，不会添加到附件）
    # 只需要在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
    # 以下设置：正文内容、邮件签名、传入参数
    top_no_content = '''
        <html>
        <body>'''
    top_has_content = '''
        <html>
        <body>
        <font size="4"> Dear,</font><br/>
        <font size="1">&nbsp</font><br/>
        <font size="3">&nbsp&nbsp&nbsp&nbsp content</font><br/>'''
    tail_no_sign = '''
        <font size="1">&nbsp</font><br/>
        <img src="cid:0">
        <p>&nbsp</p>
        </body>
        </html>'''
    tail_has_sign = '''
        <font size="1">&nbsp</font><br/>
        <img src="cid:0">
        <p>&nbsp</p>
        <p>&nbsp</p>
        <font size="3">敬颂时祺</font><br/>
        <font size="1">——————————————————</font><br/>
        <font size="2">如有任何疑问，请及时沟通！</font><br/>
        <font size="1">&nbsp</font><br/>
        <font size="2">您的姓名</font><br/>
        <font size="2">所属部门</font><br/>
        <font size="2">Tel：187 xxxx xxxx</font><br/>
        <font size="2">Email：xxxxxx</font><br/>
        </body>
        </html>'''

    if len(contents):
        top = top_has_content.split('\n')[1:]
        if isinstance(contents, str):
            conts = [contents]
        elif isinstance(contents, list):
            conts = contents
        lsq4 = top[:4]  # 头部
        mstr = top[4]   # content
        mstrs = []
        for i in conts:
            c = str(i).replace('\\','\\\\')
            s = re.sub('content', c, mstr)
            mstrs.append(s)
        tops = lsq4 + mstrs
    else:
        tops = top_no_content.split('\n')[1:]
    if sign==True:
        tails = tail_has_sign.split('\n')[1:]
    else:
        tails = tail_no_sign.split('\n')[1:]
    msgs = tops + tails
    message = '\n'.join(msgs)

    # 邮件对象-签名: （参数：文本内容、plain 设置文本格式、utf-8 设置编码）
    msg.attach(MIMEText(message, 'html', 'utf-8'))

    # 添加附件-名称支持英文/数字/符号：（中文名称在foxmail的pc端、QQ邮箱的pc与手机端都正常，但在foxmail手机端名称显示为UrlDdecode编码）
    if file_pathname != None:
        if isinstance(file_pathname, str):
            files = [file_pathname]
        else:
            files = file_pathname
        for f in files:
            fname = f.split('\\')[-1]     # 支持路径的两种斜杠/\形式
            fname = fname.split('/')[-1]
            att = MIMEText(open(r'{}'.format(f), 'rb').read(), 'base64', 'utf-8')  # 编码参数不可省略
            att["Content-Type"] = 'application/octet-stream'
            att.add_header('Content-Disposition', 'attachment', filename=fname)   # fname-附件的文件名称
            msg.attach(att)

    # 发送邮件：
    if ssl==True:
        smtp = smtplib.SMTP_SSL(server, port)   # 安全连接(加密发送)
    else:
        smtp = smtplib.SMTP(server, port)       # 普通连接(未加密发送)
    try:
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())  # receiver(接收人+抄送人)中若无有效邮箱则报错; 若至少有1个有效邮箱则发送成功(自动跳过无效邮箱)
        smtp.quit()
        print(f'[发送成功]{title}')
    except Exception as e:
        if 'Mailbox not found' in str(e):
            print(f'接收信息的邮箱无效！\n{receiver}')
        elif 'authentication failed' in str(e):
            print('发送信息的邮箱账号或密码有误！')
        else:
            print(e)

# <END>