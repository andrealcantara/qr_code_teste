from django.urls import path

from apps.qrcode.views import QRCodeView, home

urlpatterns = [
    path('', home, name='home'),
]