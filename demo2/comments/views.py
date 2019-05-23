from django.shortcuts import render,get_object_or_404,redirect,reverse


from django.http import HttpResponse
from blog.models import Article
from .models import Comment

# Create your views here.


def addcomment(request,id):


        article=get_object_or_404(Article,pk=id)
        username=request.POST.get('name')
        email=request.POST.get('email')
        url=request.POST.get('url')
        comment=request.POST.get('comment')

        comt=Comment()
        comt.username=username
        comt.url=url
        comt.article=article
        comt.email=email
        comt.comment=comment
        comt.article=article
        comt.save()

        return redirect(reverse('blog:detail',args=(id,)))
