from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('createpost/', views.createpost, name='createpost'),    
    path('members/', views.members, name='members'), 
    path('members/<int:id>', views.user, name='user'),
    path('schools/', views.schools, name='schools'), 
    path('schools/<int:id>', views.school, name='school'),     
]
