from django.urls import path
from . import views

urlpatterns = [
path('', views.Home.as_view(), name='home'),
path('about/', views.about, name='about'),
path('bugs/', views.bug_index, name='bug-index'),
path('bugs/<int:bug_id>/', views.bug_detail, name='bug-detail'),
path('accounts/signup/', views.signup, name='signup'),
]