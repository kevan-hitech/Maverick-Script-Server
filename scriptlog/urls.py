from django.urls import path
from .views import scriptlogView

urlpatterns = [
    path('scriptlog/',scriptlogView),
]