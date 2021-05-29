from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'login.html')

def facedet(request, session):
    return render(request, 'webcam.html', {
        'session_name': session
    })


def facedet_alt(request, session):
    return render(request, 'facedetect.html', {
        'session_name': session
    })
