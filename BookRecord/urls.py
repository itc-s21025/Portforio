from django.urls import path
from . import views

# URLパターンを逆引きできるように名前をつける
app_name = 'BookRecord'

# URLパターン登録用の変数
urlpatterns = [
    # viewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(),
         name='index'),

    path('post/', views.CreateBookView.as_view(),
         name='post'),

    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),

    # カテゴリ一覧ページ
    # photos/<Categorysテーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)｝としてCategoryViewに渡される
    path('book/<int:category>',
         views.CategoryView.as_view(),
         name = 'book_cat'),

    # ユーザー投稿一覧ページ
    # photos/<ユーザーテーブルのid値>にマッチング
    # <int:user>は辞書{user: id値}としてCategoryViewに渡される
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name = 'user_list'),

path('book-detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'book_detail'),

path('mypage/',
         views.MypageView.as_view(),
         name = 'mypage'),

path('book/<int:pk>/delete',
         views.BookDeleteView.as_view(),
         name = 'book_delete'),




]