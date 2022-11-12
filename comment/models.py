from django.db import models
# accontsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser

class Comment(models.Model):
    '''投稿詳細ページに対するコメントを管理するモデル
    '''
    # Customモデルのuser_idとCommentモデルを
    # １対多の関係で結びつける
    # CustomUserが親でCommentが子になる
    user = models.ForeignKey(
        CustomUser,
        #フィールドのタイトル
        verbose_name='ユーザー',
        # 削除する際はユーザーのコメントデータもすべて削除
        on_delete=models.CASCADE
    )

    comment = models.TextField(
        verbose_name='投稿に対するコメント'
    )

    # コメント作成日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す

        Return(str)：投稿記事に対するコメント
        '''
        return  self.comment
