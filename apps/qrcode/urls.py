from django.shortcuts import render
from django.urls import path

from apps.qrcode.views import QRCodeView, home, scan, scan_dois

urlpatterns = [
    path('', home, name='home'),
    path('validar-qrcode', scan , name="scan"),
    path('validar-qrcode-dois', scan_dois , name="scan-dois")
]