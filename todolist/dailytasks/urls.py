from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.home,name='homepage'),
    path('accounts/profile/',views.user_profile,name='user profile'),
    path('tasks/', views.TasksOverview.as_view(), name='tasks overview'),
    path('tasks/<int:pk>/', views.TasksDetails.as_view(), name='task details'),
    path('user/', views.UserList.as_view(), name='users overview'),
    path('user/<int:pk>/', views.UserDetails.as_view(), name='user details'),

]
