from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Tag
from .models import Comment
from taggit.forms import TagWidget

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            "tags": TagWidget(),  # nicer UI for entering tags
        }

        class Meta:
            model = Post
            fields = ['title', 'content', 'tags']

        def save(self, commit=True):
            post = super().save(commit=False)
            if commit:
                post.save()
            tags_str = self.cleaned_data['tags']
            if tags_str:
                tag_names = [name.strip() for name in tags_str.split(',')]
                for name in tag_names:
                    tag, created = Tag.objects.get_or_create(name=name)
                    post.tags.add(tag)
            return post 
     
    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Write your comment..."
            })
        }


    

    
