from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from car.models import parameter,message,show,top
# Create your views here.
def index(request):
    na=show.objects.all()
    print(type(na))
    # pr=show.objects.all()
    img=show.objects.all()

    return render(request,'index.html',locals())


def other(request):
    title=top.objects.get(title='法拉利加州兑换')
    fea=top.objects.get(fea='特征')
    dep=top.objects.get(dep='描述')
    return render(request,'single.html',locals())



def single(request):
    par=parameter.objects.all()
    mes=message.objects.all()
    fea=message.objects.all()
    des=message.objects.all()

    return render(request,'single.html',locals())

def contact(request):
    # try:
    #     send_mail('购车指南', '速度与舒适,尽在体验之中', settings.DEFAULT_FROM_EMAIL, ['719048728@qq.com', 'zhangzhaoyu@qikux.com'])
    #
    # except Exception as e:
    #     print(e)

    return render(request,'contact.html')






