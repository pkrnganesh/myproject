from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.


def index(request):
    # name = 'patrick'
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.details = 'our service is very quick'

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Reliable'
    # feature2.details = 'our service is very Reliable'

    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Easy to use'
    # feature3.details = 'our service is very Easy to use'

    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'Affordable'
    # feature4.details = 'our service is very Affordable'
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')

            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'password not the same')
            return redirect('register')

    else:
        return render(request, 'register.html')



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
     return render (request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    text = request.POST['text']  # name of the textarea tag iin form
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})



def post(request, pk):
    return render(request, 'post.html', {'pk': pk})