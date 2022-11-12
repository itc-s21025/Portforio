from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CommentForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Comment

@method_decorator(login_required, name='dispatch')
class CreateCommentView(CreateView):
    form_class = CommentForm

    template_name = "comment.html"

    commentupload_url = reverse_lazy('BookRecord:book_detail')

    def form_valid(self, form):

        commentdata = form.save(commit=False)

        commentdata.user = self.request.user

        commentdata.save()

        return super().form_valid(form)
