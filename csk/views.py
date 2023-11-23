from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def msd(request):
    return render(request,'msd.html')

def rayudu(request):
    return HttpResponse('<h1><center><marquee>Ambati Baahubali Rayudu</h1></center></marquee>')