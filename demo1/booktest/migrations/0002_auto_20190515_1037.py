# Generated by Django 2.2.1 on 2019-05-15 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='bittle',
            field=models.CharField(max_length=20, verbose_name='书名'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='bpub_data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='出版时间'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.BookInfo', verbose_name='书'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='gender',
            field=models.CharField(choices=[(1, '男'), (2, '女')], max_length=30, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='name',
            field=models.CharField(max_length=30, verbose_name='角色名'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='skill',
            field=models.CharField(max_length=30, null=True, verbose_name='技能'),
        ),
    ]
