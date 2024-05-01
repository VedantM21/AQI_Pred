from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.homepage, name=""),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('maharashtra', views.maharashtra, name="maharashtra"),
    path('gujarat', views.gujarat, name="gujarat"),
    path('uttarpradesh', views.uttarpradesh, name="uttarpradesh"),
    path('kerala', views.kerala, name="kerala"),
    path('punjab', views.punjab, name="punjab"),

]











