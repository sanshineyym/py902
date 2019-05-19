from django.db import models

# Create your models here.

class BookInfo(models.Model):
    #每一个字段对应 表中的一列
    bittle=models.CharField(max_length=20,verbose_name='书名')
    #auto_now_add=True意味着默认时间为该行插时间
    bpub_data=models.DateTimeField(verbose_name='出版时间')
    #打印模型
    def __str__(self):
        return self.bittle



class HeroInfo(models.Model):
    name=models.CharField(max_length=30,verbose_name='角色名')
    #bool 性别类型 默认值为true 代表男
    gender=models.CharField(max_length=30,verbose_name='性别',choices=(('1','男'),('2','女')))
    #null=true   代表该列可以为空
    skill=models.CharField(max_length=30,null=True,verbose_name='技能')
    #ForeignKey 表名和BookInfo为多对一关系
    #book 的类型  BookInfo
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='书')

    #打印模型
    def __str__(self):
        return self.name




class Account(models.Model):
    username=models.CharField(max_length=20)

class  Content(models.Model):
    tel=models.CharField(max_length=11)
    account=models.OneToOneField(Account,on_delete=models.CASCADE)

class Host(models.Model):
    hostname=models.CharField(max_length=20)

class Applicatian(models.Model):
    appname=models.CharField(max_length=20)
    host=models.ManyToManyField(Host)
    







