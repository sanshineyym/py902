from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import BookInfo,HeroInfo

# Create your views here.
#MVT中的V 可以是视图函数，也可以是视图类
def index(request):
    # # return HttpResponse('index首页')
    # #1.加载模板
    # template=loader.get_template('')
    # #2.构造参数字典
    # context={'username':'zzy'}
    # #3.使用模块渲染动态数据
    # result=template.render(context=context)
    # return HttpResponse(result)
    return render(request,'booktest/index.html',context={'username':'zzy'})


def list(request):

    # #查询所有书籍
    allbook=BookInfo.objects.all()
    # # return HttpResponse('列表页')
    # #1.加载模块
    # template=loader.get_template('booktest/list.html')
    # result=template.render({'allbook':allbook})
    # return HttpResponse(result)
    return render(request,'booktest/list.html',context={'allbook':allbook})


def detail(request,id):
    print(id)
    # #id代表书的主键
    book=None
    try:
        book=BookInfo.objects.get(pk=id)
    except Exception as e:
        return HttpResponse('没有当前书籍')
    #
    # templ=loader.get_template('booktest/detail.html')
    # result=templ.render({'book':book})
    # return HttpResponse(result)
    return render(request,'booktest/detail.html',context={'book':book})

    # return HttpResponse('当前为第%s页'%id)

def deletebook(request,id):
    BookInfo.objects.get(pk=id).delete()
    return HttpResponseRedirect('/booktest/list/')

    # return HttpResponse('success')

def deletehero(request,id):
    # return HttpResponse('success')角色
    #通过角色id找到角色
    hero=HeroInfo.objects.get(pk=id)
    #通过多找一 关系找到书的id
    bookid =hero.book.id
    #删除英雄
    hero.delete()
    return HttpResponseRedirect('/booktest/detail/%s' % (bookid,))


def addhero(request,id):
    if request.method=='GET':

        return render(request,'booktest/addhero.html',{'bookid':id})
    elif request.method=='POST':
        book=BookInfo.objects.get(pk=id)
        hero=HeroInfo()
        hero.name=request.POST['username']
        value=request.POST['sex']
        hero.gender=value
        hero.skill=request.POST['skill']
        hero.book=book
        hero.save()

        return HttpResponseRedirect('/booktest/detail/%s'%(id,))

def edithero(request,id):
    hero = HeroInfo.objects.get(pk=id)

    if request.method=='GET':
        hero = HeroInfo.objects.get(pk=id)
        return render(request,'booktest/edithero.html',{'hero':hero})

    elif request.method == 'POST':
        hero.name=request.POST['username']
        hero.gender=request.POST['sex']
        hero.skill=request.POST['skill']

        hero.save()
        # return HttpResponse('success')
        return HttpResponseRedirect('/booktest/detail/%s/'%(hero.book.id,))




