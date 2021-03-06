from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login', views.login, name='login'),
	path('upload', views.upload, name='upload'),
	path('signup', views.signup, name='signup'),
	path('logout', views.logout, name='logout'),
	path('friends', views.friends, name='friends')
]