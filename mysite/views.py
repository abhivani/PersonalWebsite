from django.shortcuts import render
from .models import Contact
import requests
import json

def index(request):
    if request.method == 'POST':
        firstname = request.post.get('fname')
        lastname = request.post.get('lname')

        r = request.get('http://api.icndb.com/jokes/random?firstname='+ firstname + '&lastname='+ lastname )
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'mysite/index.html', context)

    else:
        firstname = 'abhi'
        lastname = 'vani'

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'mysite/index.html', context)


def portfolio(request):
    return render(request, 'mysite/portfolio.html')


def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email = email_r, subject = subject_r, message = message_r)
        c.save()

        return render(request, 'mysite/thankyou.html')
    else:
        return render(request,'mysite/contact.html')


