from django.urls import path
from .views import addssidView

urlpatterns = [
    path('addssid/',addssidView),
]


