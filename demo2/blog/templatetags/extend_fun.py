from django import template
from ..models import Article,Category,Tag
register=template.Library()

'''
过滤器最多两个参数
'''

@register.simple_tag(name='getcategorys')
def getcategorys():
    return Category.objects.all()


@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def getarchives(num=3):
    re=Article.objects.dates('create_time','month',order='DESC')[:num]
    return re

@register.simple_tag
def gettags():
    return Tag.objects.all()


@register.simple_tag
def getlatestarticles(num=3):
    return  Article.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def getarchives(num=3):
    result=Article.objects.dates("create_time",'month',order='DESC')[:num]
    print(result)
    return result
