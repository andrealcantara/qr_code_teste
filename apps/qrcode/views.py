from django.shortcuts import render

# Create your views here.
from django.views import View


def home(request):
    return render(request, 'index.html')

def scan(request):
    return render(request, 'scan.html')

def scan_dois(request):
    return render(request, 'scan2.html')

class QRCodeView(View):
    pass