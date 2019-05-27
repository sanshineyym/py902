from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from .models import Article
#分页器Paginator  page 当前页面
from django.core.paginator import Paginator
import markdown
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    pagenum=request.GET.get('page')
    pagenum=1 if pagenum==None else pagenum
    #得到所有文章
    articles = Article.objects.all().order_by('-views')
    paginator=Paginator(articles,1)
    #传入一个网页得到一个页面  page包含所有信息
    page=paginator.get_page(pagenum)

    # latesartiles=Article.objects.all().order_by('-create_time')[:3]

    return render(request,'index.html',{'page':page})

def detail(request,id):
    article=get_object_or_404(Article,pk=id)
    #使用markdown处理body  将markdown语法转为HTML标签
    article.body=markdown.markdown(article.body,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])

    # latesartiles=Article.objects.all().order_by('-create_time')[:3]

    return render(request,'single.html',locals())

def archives(request,year,month):
    pagenum = request.GET.get('page')
    pagenum = 1 if pagenum == None else pagenum

    articles = Article.objects.filter(create_time__year=year, create_time__month=month)
    paginator = Paginator(articles,1)

    page = paginator.get_page(pagenum)
    page.parms = '/archives/%s/%s/' % (year, month)
    return render(request, 'index.html', {'page': page})

def category(request,id):
    pagenum=request.GET.get('page')
    pagenum=1 if pagenum==None else pagenum

    articles=get_object_or_404(category,pk=id).article_set.all()
    paginator=Paginator(articles,1)
    page=paginator.get_page(pagenum)
    page.parms = '/category/%s/'%(id,)
    return render(request,'index.html',{'page':page})

def tag(request,id):

    pagenum = request.GET.get('page')
    pagenum = 1 if pagenum == None else pagenum

    articles = get_object_or_404(tag,pk=id).article_set.all()
    paginator = Paginator(articles, 1)
    page = paginator.get_page(pagenum)
    page.parms = '/category/%s/' % (id,)
    return render(request, 'index.html', {'page': page})

def contact(request):
    send_mail('django邮件','django可以发送邮件',settings.DEFAULT_FROM_EMAIL,['719048728@qq.com','zhangzhaoyu@qikux.com'])


    return render(request, 'contact.html')





