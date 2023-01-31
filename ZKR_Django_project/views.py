# 部门:人工智能
# 编写人:张开然
# 开发日期: 2023/1/11
# !/usr/bin/python
# -*- coding: UTF-8 -*-
import json

from django.http import HttpResponse, HttpResponseRedirect

POST_FORM = '''
<form method='post' action='/get_or_post'>
    用户名: <input type='text' name='uname'>
    <input type='submit' value='提交'>
</form>
'''

def page_yun_view(request):
    html = """<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>利用VScode创建的网页</title>
  </head>
  <body>
    <h1><strong>键盘敲烂年薪过万</strong></h1>
    <h2>学技术来太理云顶书院</h2>
    <h3>学完前端学后端</h3>
    <h4>学完Python学Java</h4>
    <h5><strong>还有CPU和OS</strong></h5>
    <br />
    <h2>教育理念</h2>
    <p>
      云顶书院探索和总结出<strong>“导师为人、自师为学”</strong>的教育理念，全面系统地开展了新书院制的实践。<br />通过借鉴吸收国际先进教育理念，研究创新型人才培养规律及特点，基于真实问题和项目设计培养过程，着力培养学生自主学习和终身学习的意识，逐渐形成了以兴趣驱动为核心的泛在学习体系，以要素驱动为基础的知识管理体系，以情景驱动为抓手的工程能力攀升体系，以自我驱动为主线的艺术素养教育体系，以梦想驱动为支撑的理想信念教育体系，构建起一种基于新书院制管理模式的、低熵化的适应性学习系统。
    </p>
    <p>
      云顶书院通过构建融通网络世界与现实世界的泛在学习社区，<ins
        ><em>面向全校不分专业招募选拔本科新生，</em></ins
      >建立基于梦想驱动的学习共同体，针对学生成长不同阶段提供循序渐进的梯度培育，引导成员突破影响成长的思维桎梏，激励学生在广泛的学科渗透和文化浸润中协调发展，进而实现自主性、包容性、开放性的新型学生教育管理制度。
    </p>
    图像标签的具体使用<br />
    <img src="logo.gif" title="这是云顶的logo" width="800" height="600" />
    <img src="zkr.png" alt="我是七期的张开然" /><br />
    <img src="logo.gif" title="这是云顶的logo" height="100" />
    <img src="logo.gif" title="这是云顶的logo" width="300" border="15" />
    <div>一个人我占一整行</div>
    222
    <div>第二个人我占一整行</div>
  </body>
</html>"""
    return HttpResponse(html)

def index_view(request):
    html = '这是我的首页'
    return HttpResponse(html)

def page1_view(request):
    html = '这是网页的第一页'
    return HttpResponse(html)

def page2_view(request):
    html = '这是网页的第二页'
    return HttpResponse(html)

def pagen_view(request, pg):
    html = '网页的这是第%s页'%(pg)
    return HttpResponse(html)

def birthday_view(request, year, month, day):

    html = '生日为：%s年%s月%s日'%(year, month, day)
    return HttpResponse(html)

def test_request(request):
    print("请求的路径是", request.path_info)
    print("请求的方法是", request.method)
    print("请求的主体是", request.body)

    return HttpResponseRedirect("/page/yun")

def get_or_post(request):
    if request.method == "GET":
        print(request.GET.get('a', 'no a'))
        print(request.GET.get('c', 'no c'))
        return HttpResponse(POST_FORM)

    elif request.method == "POST":
        '''处理用户提交的数据'''
        print('uname is', request.POST['uname'])
        print(request.POST)

        return HttpResponse('post is ok!')
    else:
        pass
    return HttpResponse('--test is ok!')

def test_html(request):
    """方案1"""
    # from django.template import loader
    # t = loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)
    """方案2"""
    # from django.shortcuts import render
    # return render(request, 'test_html.html')
    """方案3可以使用传进来的参数"""
    from django.shortcuts import render
    dic = {
        "username":'zhangkr',
        "age":"18"
    }
    return render(request, 'test_html.html', dic)

def test_html_param(request):
    from django.shortcuts import render
    dic={}
    dic['int'] = 88
    dic['str'] = 'zkr'
    dic['lst'] = ['tom','jessie','lisa']
    dic['dict']={'a':9,'b':7}
    dic['func'] = say_hi  # 传函数要取掉括号，不然就是传字符串
    dic['class_obj'] = Dog()
    dic['html'] = """<script>alert('111')</script>"""
    return render(request, 'test_html_param.html', dic)

def test_if_for(request):
    from django.shortcuts import render
    dic={}
    dic['x'] = 150
    dic['lst'] = ['tom', 'jessie', 'lisa']
    return render(request, 'test_if_for.html', dic)

def test_calculator(request):
    from django.shortcuts import render
    if request.method == "GET":
        return render(request, 'test_calculator.html')
    elif request.method == "POST":
        # 处理计算
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']

        if op == "add":
            result = x + y
        elif op == "sub":
            result = x - y
        elif op == "mul":
            result = x * y
        else:
            result = x / y
        return render(request, 'test_calculator.html', locals())  # locals会把当前的局部变量封装出一个字典
def base_view(request):
    from django.shortcuts import render
    lst = ['base', 'music', 'sports']
    return render(request, 'base.html', locals())
def music_view(request):
    from django.shortcuts import render
    return render(request, 'music.html')
def sports_view(request):
    from django.shortcuts import render
    return render(request, 'sports.html')

def test_url(request):
    from django.shortcuts import render
    return render(request, 'url.html')

def test_url_result(request, age):

    # 302跳转
    from django.urls import reverse
    url = reverse('base_index')
    return HttpResponseRedirect(url)

    # return HttpResponse('____the test is ok!')

def test_json(request):
    dic = {}

    if request.method == "POST":
        resp = json.loads(request.body)
        print(resp)
        username = resp['username']
        password = resp['password']
        print(password)

    dic['username'] = username
    dic['password'] = password
    print(f"用户名是{username},密码是{password}")
    json_1 = json.dumps(dic)
    return HttpResponse(json_1)



def say_hi():
    return 'hahaha'
class Dog:
    def say(self):
        return 'hahaha'