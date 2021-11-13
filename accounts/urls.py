from django.urls import path,include
from .views import home, killaddmac, killaddssid, launchscripts,killremovemac, killremovessid, info, results

urlpatterns = [
    path('', home),
    path('20213301111801', killaddmac,name="killaddmac"),
    path('388181330111180', killaddssid,name="killaddssid"),
    path('202141241214711', killremovemac,name="killremovemac"),
    path('388181412412147',killremovessid,name="killremovessid"),
    path('819151871281723', launchscripts,name="launchscripts"),
    path('info',info,name='info'),
    path('results',results,name='results')
]
