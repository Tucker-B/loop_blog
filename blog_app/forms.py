from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50)
    excerpt = forms.CharField(max_length=50)
    content = forms.CharField(label="Content", widget=forms.Textarea, max_length=1000)
    # tags = forms.ModelChoiceField()