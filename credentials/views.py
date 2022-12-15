from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password == re_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already In Use")
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                user.save()
                print("USER CREATED")
                return redirect('credentials:login')
        else:
            messages.info(request, "Password Not Matching")
            return redirect('credentials:register')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print(user.first_name)
            return redirect('website:home')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('credentials:login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
