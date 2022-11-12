# UserCreationFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm
# models.pyで定義したカスタムUserモデルをインポート
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    '''UserCreationFormのサブクラス
    '''
    class Meta:
        '''UserCreateクラスのインナークラス

        Attributes:
            model:連携するUserモデル
            fields:フォームで使用するフィールド
        '''

        # 連携するモデルを設定
        model = CustomUser
        # フォームで使用するフィールドを設定
        #　ユーザー名、メールアドレス、パスワード、パスワード（確認用）
        fields = ('username', 'email', 'password1', 'password2')
