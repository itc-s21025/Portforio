# Generated by Django 4.1.3 on 2022-11-05 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='カテゴリ')),
            ],
        ),
        migrations.CreateModel(
            name='BookPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('author', models.CharField(max_length=200, verbose_name='著者')),
                ('publisher', models.CharField(max_length=200, verbose_name='出版社')),
                ('comment', models.TextField(verbose_name='コメント')),
                ('image1', models.ImageField(upload_to='photos', verbose_name='イメージ1')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BookRecord.category', verbose_name='カテゴリ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
    ]
