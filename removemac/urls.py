from django.urls import path
from .views import removemacView, getmacs

urlpatterns = [
    path('removemac/',removemacView),
    path('202191314129146', getmacs, name="getmacs")
]