from django.urls import path
from .views import addmacView

urlpatterns = [
    path('addmac/',addmacView),
]


