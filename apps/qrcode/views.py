from django.shortcuts import render

# Create your views here.
from django.views import View


def home(request):
    return render(request, 'index.html')

class QRCodeView(View):
    pass