from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス

    '''
    # レコード一覧にidとusernameを表示
    list_display = ('id', 'username')
    # リンクの設定
    list_display_links = ('id', 'username')

# 管理サイトにCustomUserとCustomUserAdminを追加する
admin.site.register(CustomUser,CustomUserAdmin)
