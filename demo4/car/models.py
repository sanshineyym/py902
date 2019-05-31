from django.db import models


# Create your models here.

class top(models.Model):
    title=models.CharField(max_length=20,verbose_name='标题')
    fea=models.CharField(max_length=20,verbose_name='特征')
    dep=models.CharField(max_length=20,verbose_name='描述')






class parameter(models.Model):
    Make=models.CharField(max_length=20,verbose_name='制造：')
    Model=models.CharField(max_length=20,verbose_name='模型')
    MFG=models.CharField(max_length=20,verbose_name='生产日期')
    Mileage=models.CharField(max_length=20,verbose_name='里程数')
    Power=models.CharField(max_length=20,verbose_name='动力')
    Fuel=models.CharField(max_length=20,verbose_name='燃料')
    Gearbox=models.CharField(max_length=20,verbose_name='变速箱')
    Number=models.CharField(max_length=20,verbose_name='座位数')
    Doors=models.CharField(max_length=20,verbose_name='门')
    EC=models.CharField(max_length=20,verbose_name='排放等级')
    VT=models.CharField(max_length=20,verbose_name='车辆类型')
    Color=models.CharField(max_length=20,verbose_name='颜色')
    Airbags=models.CharField(max_length=20,verbose_name='安全气囊')
    CC=models.CharField(max_length=20,verbose_name='气候控制')
    DV=models.CharField(max_length=20,verbose_name='损坏车辆')
    feature=models.TextField(max_length=100,verbose_name='特征')
    describe=models.TextField(verbose_name='描述')


class message(models.Model):
    username=models.CharField(max_length=20,verbose_name='名字')
    phone=models.CharField(max_length=20,verbose_name='电话')
    cellphone=models.CharField(max_length=20,verbose_name='手机')
    fax=models.CharField(max_length=20,verbose_name='传真')
    email=models.EmailField(max_length=20,verbose_name='邮箱')
    postcode=models.CharField(max_length=20,verbose_name='邮编')
    address=models.TextField()
    city=models.TextField()

class show(models.Model):
    name = models.CharField(max_length=20, verbose_name='品牌：')
    price = models.IntegerField(default=0, verbose_name='价钱')
    img = models.ImageField(upload_to='ads', verbose_name='图片')
    parame=models.ForeignKey(parameter,on_delete=models.CASCADE)












