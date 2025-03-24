from django.test import TestCase

# Create your tests here.
from django.urls import path
from . import views  # استيراد الوظائف (views) من التطبيق

urlpatterns = [
    path('', views.home, name='home'),  # رابط الصفحة الرئيسية
    path('login/', views.login, name='login'),  # رابط صفحة تسجيل الدخول
    path('signup/', views.signup, name='signup'),  # رابط صفحة التسجيل
    path('reset/', views.reset, name='reset'),  # رابط صفحة إعادة تعيين كلمة المرور
    # يمكنك إضافة المزيد من الروابط هنا
]