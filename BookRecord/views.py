from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import BookPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import BookPost
from django.views.generic import DetailView
from django.views.generic import DeleteView


class IndexView(ListView):
    '''トップページのビュー
    '''
    # index.htmlをレンダリング
    template_name = 'index.html'

    # bookpostのオブジェクトにorder_byを適用
    # 投稿日時を降順
    queryset = BookPost.objects.order_by('-posted_at')

    # １ページに表示するレコードの件数
    paginate_by = 9


# デコレーターにより、CreatePhotoViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsetting.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreateBookView(CreateView):
    '''写真投稿のページのビュー

    BookPostFormで定義されているモデルとフィールドと連携して
    投稿データをデータベースに登録する

    Attributes:
        form_class: モデルとフィールドが登録されたフォームクラス
        template_name: レンダリングするテンプレート
        success_url: データベースへの登録完了後のリダイレクト先
    '''
    # forms.pyのBookPostFormをフォームクラスとして登録
    form_class = BookPostForm
    # レンダリングするテンプレート
    template_name = "post_book.html"
    # フォームデータ完了後のリダイレクト先
    success_url = reverse_lazy('BookRecord:post_done')

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド

        フォームのバリデーションを通過したときに呼ばれる
        フォームのデータ登録をここで行う

        :param form:
        :return:
        '''

        # commit=FalseにしてPostされたデータを取得
        postdata = form.save(commit=False)
        #　投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    '''投稿完了ページのビュー

    '''
    template_name = 'post_success.html'

class CategoryView(ListView):

    template_name = 'index.html'

    paginate_by = 9

    def get_queryset(self):

        category_id = self.kwargs['category']
        categories = BookPost.objects.filter(
            category=category_id).order_by('-posted_at')

        return categories

class UserView(ListView):
    '''ユーザー投稿一覧ページのビュー

    '''
    template_name = 'index.html'

    paginate_by = 9

    def get_queryset(self):

        # CategoryViewと同じ原理
        user_id = self.kwargs['user']
        # filterでフィールド名IDを取り込む
        user_list = BookPost.objects.filter(
            user=user_id).order_by('posted_at')
        # クエリによって取得されたレコードを返す
        return user_list

class DetailView(DetailView):
    '''詳細ページのビュー

    投稿記事の詳細を表示するのでDetailViewを継承する

    '''
    template_name = 'detail.html'

    model = BookPost

class MypageView(ListView):
    '''マイページのビュー
    '''
    # mypage.htmlをレンダリングする
    template_name = 'mypage.html'
    # １ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):


        # 現在ログインしているユーザー名はHttpRequest.userに格納されている
        # filter(userフィールド=userオブジェクト)で絞りこむ
        queryset = BookPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset

class BookDeleteView(DeleteView):
    '''
    レコードの削除を行うビュー
    '''
    # 操作対象はPhotoPostモデル
    model = BookPost
    # photo_delete.htmlをレンダリングする
    template_name = 'book_delete.html'
    # 処理完了後にマイページにリダイレクト
    success_url = reverse_lazy('BookRecord:mypage')

    def delete(self, request, *args, **kwargs):
        '''レコードの削除を行う

        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        return super().delete(request, *args, **kwargs)