# Generated by Django 2.2.6 on 2019-10-10 10:30

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogtypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=24, verbose_name='类型')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Blogtypes', verbose_name='类别')),
            ],
        ),
    ]
