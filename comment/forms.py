from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス

        '''
        model = Comment
        fields = ['comment']