# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-06 07:48
from __future__ import unicode_literals

import ckeditor_uploader.fields
import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='评论内容')),
                ('publish_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '评论/回复',
                'verbose_name_plural': '评论/回复',
                'db_table': 'news_comment',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('picture', models.CharField(max_length=20, verbose_name='标签')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='新闻内容')),
                ('image', models.ImageField(default='default.png', max_length=255, upload_to='image/%Y/%m', verbose_name='文章图片')),
                ('publish_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间')),
                ('clicked', models.IntegerField(default=0, verbose_name='点击量')),
            ],
            options={
                'verbose_name': '文章内容',
                'verbose_name_plural': '文章内容',
                'db_table': 'content',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='新闻类型')),
            ],
            options={
                'verbose_name': '新闻类型',
                'verbose_name_plural': '新闻类型',
                'db_table': 'news_type',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[('0', '男'), ('1', '女')], max_length=1, verbose_name='性别')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='电话')),
                ('image', models.ImageField(default='default.png', max_length=255, upload_to='image/%Y/%m', verbose_name='头像')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'user_info',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='context', to='APP04.Type', verbose_name='新闻类型'),
        ),
        migrations.AddField(
            model_name='content',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='context', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='comment',
            name='news_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='APP04.Content', verbose_name='评论文章'),
        ),
        migrations.AddField(
            model_name='comment',
            name='restore',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APP04.Comment', verbose_name='回复对象'),
        ),
        migrations.AddField(
            model_name='comment',
            name='restore_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restore', to=settings.AUTH_USER_MODEL, verbose_name='回复用户'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='评论作者'),
        ),
    ]