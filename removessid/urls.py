from django.urls import path
from .views import removessidView, getssids

urlpatterns = [
    path('removessid/',removessidView),
    path('388181913141291', getssids, name='getssids'),
]