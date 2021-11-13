from django.urls import path
from .views import HomeView, LoginsView, logout

urlpatterns = [
    path('register',HomeView,name='register'),
    path('login',LoginsView,name='login'),
    path('accounts/logout',logout,name='logout'),
]
