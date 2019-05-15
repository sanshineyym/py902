from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from .models import BookInfo,HeroInfo

# Create your views here.
#MVT中的V 可以是视图函数，也可以是视图类
def index(request):
    # return HttpResponse('index首页')
    #1.加载模板
    template=loader.get_template('booktest/index.html')
    #2.构造参数字典
    context={'username':'zzy'}
    #3.使用模块渲染动态数据
    result=template.render(context=context)
    return HttpResponse(result)


def list(request):

    #查询所有书籍
    allbook=BookInfo.objects.all()
    # return HttpResponse('列表页')
    #1.加载模块
    template=loader.get_template('booktest/list.html')
    result=template.render({'allbook':allbook})
    return HttpResponse(result)


def detail(request,id):
    print(id)
    #id代表书的主键
    book=None
    try:
        book=BookInfo.objects.get(pk=id)
    except Exception as e:
        return HttpResponse('没有当前书籍')

    templ=loader.get_template('booktest/detail.html')
    result=templ.render({'book':book})
    return HttpResponse(result)

    # return HttpResponse('当前为第%s页'%id)

