from django.shortcuts import render
from django.core.mail import send_mail

def index(request):

    send_mail(
        'A new email',
        'This mail has been send to you by django',
        'prasid101@gmail.com',
        ['pirato61@gmail.com'],
        fail_silently=False,
    )

    return render(request,'index.html')