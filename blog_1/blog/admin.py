# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
# Register your models here.

#
# class ArticleAdmid(admin.ModelAdmin):
#      list_display = ('title', 'desc', 'content',)
    #
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'desc', 'content')
    #     }),
    #     ('更多选择', {
    #         'classes': ('collapse',),
    #         'fields': ('click_count', 'is_recommend')
    #     }),
    # )

class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )



admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)