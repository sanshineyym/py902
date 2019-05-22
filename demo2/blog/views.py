from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from .models import Article
#分页器Paginator  page 当前页面
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    pagenum=request.GET.get('page')
    pagenum=1 if pagenum==None else pagenum
    #得到所有文章
    articles = Article.objects.all().order_by('-views')
    paginator=Paginator(articles,1)
    #传入一个网页得到一个页面  page包含所有信息
    page=paginator.get_page(pagenum)




    return render(request,'index.html',{'page':page})

def detail(request,id):
    article=get_list_or_404(Article,pk=id)
    return render(request,'single.html',locals())