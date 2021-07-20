from django import forms
from .models import Tag

class PostForm(forms.Form):
    title = forms.CharField(label="題名", max_length=50)
    excerpt = forms.CharField(label="抜粋",max_length=105)
    content = forms.CharField(label="内容", widget=forms.Textarea, max_length=1000)
    image_name = forms.CharField(label="イメージ名",max_length=100)
    tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset = Tag.objects.all().order_by('caption'))

    def clean_tags(self):
        value = self.cleaned_data['tags']
        if len(value) > 4:
            raise forms.ValidationError("You can't select more than 4 tags per post.")
        return value

class TagForm(forms.Form):
    caption = forms.CharField(label="キャプション", max_length=20)