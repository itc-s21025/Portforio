from django.forms import ModelForm
from .models import BookPost

class BookPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        Attribute:
            model: モデルのクラス
            fields: フォームで使用するモデルのフィールドを指定
        '''
        model = BookPost
        fields = ['category', 'title', 'author', 'publisher', 'comment', 'image1']