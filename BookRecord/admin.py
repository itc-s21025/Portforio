from django.contrib import admin

# CustomUserをインポート
from .models import Category, BookPost

class CategoryAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧を表示するカラムを設定するクラス

    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

class BookPostAdmin(admin.ModelAdmin):
    '''管理ページにレコード一覧を表示するカラムを設定するクラス

    '''

    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    #表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

# Django管理サイトにCategory,CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)

# Djangoの管理サイトにPhotoPost, PhotoPostAdminを登録する
admin.site.register(BookPost, BookPostAdmin)