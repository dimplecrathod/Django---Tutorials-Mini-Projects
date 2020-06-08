from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    send_mail('Hello from DiRathod',
    'Hello there. This is an automated message',
    'dicrathod@gmail.com',
    ['cecehil742@ismailgul.net'],
    fail_silently=False)
    return render(request, 'send/index.html')