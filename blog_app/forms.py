from django import forms
from .models import Tag
class PostForm(forms.Form):
    title = forms.CharField(label="題名", max_length=50)
    excerpt = forms.CharField(label="抜粋",max_length=100)
    content = forms.CharField(label="内容", widget=forms.Textarea, max_length=1000)
    image_name = forms.CharField(label="イメージ名",max_length=100)
    tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset = Tag.objects.all())
    # tags = forms.ModelChoiceField()