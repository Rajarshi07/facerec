from django.shortcuts import render

# Create your views here.

def report(request):
    return render(request,'login.html')

def room(request, room_name):
    return render(request, 'chat.html', {
        'session_name': room_name
    })


def facedet(request, session):
    return render(request, 'webcam.html', {
        'session_name': session
    })
