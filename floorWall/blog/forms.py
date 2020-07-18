from django_summernote.widgets import SummernoteWidget
from django import forms


class CommentForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())