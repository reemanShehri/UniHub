import django
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.models import AbstractUser

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

# class CustomUser(AbstractUser):  # استخدم الحرف الكبير "C"
#     email = models.EmailField(unique=True)  # بريد إلكتروني فريد
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

class University(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    established_year = models.IntegerField()
    # website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# class Login(models.Model):
#             username = models.CharField(max_length=150, unique=True)
#             password = models.CharField(max_length=128)
#             def __str__(self):
#                 return f"{self.username} - {self.last_login}"

class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.code})"





i=0
def generate_student_id():
    global i
    i+=1
    return f"2022-{i:04d}"
class StudentProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # بدلًا من auth.User
        on_delete=models.CASCADE
    )    
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
    student_id = models.CharField(max_length=20, unique=True, default=generate_student_id)
    courses = models.ManyToManyField('Course', blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    academic_level = models.CharField(max_length=50, blank=True)
    major = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.user.username

   



class Board(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)  # اسم التصنيف
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # وقت الإنشاء

    def __str__(self):
        return self.name  # يعيد اسم التصنيف لعرضه بسهولة



class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, default=1)  # Remove default=2022
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
  
    def __str__(self):
        return self.title


class Reply(models.Model):
    content = models.TextField()
    author = models.ForeignKey(StudentProfile, on_delete=models.CASCADE,default=1)  # Remove default=2022
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Reply by {self.author.user.username} on {self.post.title}"

class Notification(models.Model):
    user = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.message


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(default='Default auth', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)
    board = models.ForeignKey(default='Default Board', on_delete=django.db.models.deletion.CASCADE, to='firstapp.board')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

class Admin(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # بدلًا من auth.User
        on_delete=models.CASCADE
    )    
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username



