# Generated by Django 2.1.7 on 2019-04-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_auto_20190405_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Comment_Author',
            field=models.TextField(default='Author', max_length=25, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Comment_Text',
            field=models.TextField(default='Comment', max_length=150, verbose_name=''),
        ),
    ]
