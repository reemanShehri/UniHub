from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Post, Reply,User
from .models import *
from django.contrib.auth.models import User








class loginForm(forms.ModelForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ['username', 'password']
class SignupForm(forms.ModelForm):
    profileName = forms.CharField(max_length=255)
    email=forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=[('female', 'Female'), ('male', 'Male'), ('non_binary', 'Non-binary')], required=False)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    accept_terms = forms.BooleanField()

    class Meta:
        model = User
        fields = ['profileName', 'email', 'password', 'gender', 'date_of_birth', 'accept_terms']
    

class StudentRegistrationForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)
    university = forms.CharField(max_length=255)
    academic_level = forms.CharField(max_length=50)
    major = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture', 'university', 'academic_level', 'major']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
    
    # additionalll
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Post.objects.filter(title=title).exists():
            raise forms.ValidationError("A post with this title already exists.")
        return title
    

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']



