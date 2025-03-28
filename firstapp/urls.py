from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('Dashboard/', views.dashboard, name='dashboard'),
    path('board/<int:board_id>/', views.board_detail, name='board_detail'),
    path('board/<int:board_id>/create_post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('board/<int:board_id>/create_announcement/', views.create_announcement, name='create_announcement'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
    path('complete-profile/Dashboard.html', views.dashboard, name='profile_dashboard'),
    path('student/<int:id>/', views.student_detail, name='student_detail'),

]