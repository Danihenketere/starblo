from django import forms
from .models import Post, Category

choice = Category.objects.all().values_list('name','name')
choice_list = []

for item in choice:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','advert','body','image1','image2','image3','image4','image5','image6')
        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Input the title'}),
            'title_tag': forms.TextInput(attrs = {'class':'form-control'}),
            'author': forms.Select(attrs = {'class':'form-control'}),
            'category': forms.Select(choices= choice_list,attrs = {'class':'form-control'}),
            'body': forms.Textarea(attrs = {'class':'form-control'}),
            'advert': forms.Textarea(attrs = {'class':'form-control'}),
        }



class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','advert','body','image1','image2','image3','image4','image5','image6')
        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Input the title'}),
            'title_tag': forms.TextInput(attrs = {'class':'form-control'}),
            #'author': forms.Select(attrs = {'class':'form-control'}),
            'body': forms.Textarea(attrs = {'class':'form-control'}),
            'advert': forms.Textarea(attrs = {'class':'form-control'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','author','snippet','body')
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control'}),
            'author': forms.Select(attrs = {'class':'form-control'}),
            'body': forms.Textarea(attrs = {'class':'form-control'}),
            'snippet': forms.Textarea(attrs = {'class':'form-control'}),
        }

class AboutUsForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('author','body')
        widgets = {
            'author': forms.Select(attrs = {'class':'form-control'}),
            'body': forms.Textarea(attrs = {'class':'form-control'}),
        }