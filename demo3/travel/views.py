from django.shortcuts import render
from django.core.mail import send_mail,send_mass_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    try:
        send_mail('旅游指南','你的欢乐之旅',settings.DEFAULT_FROM_EMAIL,['719048728@qq.com','zhangzhaoyu@qikux.com'])
        return render(request, 'index.html')
    except Exception as e:
        print(e)
        return render(request, 'index.html')


