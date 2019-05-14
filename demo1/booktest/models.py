from django.db import models

# Create your models here.

class BookInfo(models.Model):
    #每一个字段对应 表中的一列
    bittle=models.CharField(max_length=20)
    #auto_now_add=True意味着默认时间为该行插时间
    bpub_data=models.DateTimeField(auto_now_add=True)
    #打印模型
    def __str__(self):
        return self.bittle



class HeroInfo(models.Model):
    name=models.CharField(max_length=30)
    #bool 性别类型 默认值为true 代表男
    gender=models.BooleanField(default=True)
    #null=true   代表该列可以为空
    skill=models.CharField(max_length=30,null=True)
    #ForeignKey 表名和BookInfo为多对一关系
    #book 的类型  BookInfo
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    #打印模型
    def __str__(self):
        return self.name



