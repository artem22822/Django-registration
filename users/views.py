from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(reauest):
    return render(reauest,'accounts/home.html')

def singup(reauest):
    if reauest.method == 'POST':
        uname = reauest.POST.get('username')
        email = reauest.POST.get('email')
        password1 = reauest.POST.get('password1')
        password2 = reauest.POST.get('password2')

        if password1 != password2:
            return HttpResponse('You Password mismatch !!!')
        else:
            my_user = User.objects.create_user(uname,email,password1)
            my_user.save()
            print(uname, email, password1, password2)

            return redirect('login')

    return render(reauest, 'accounts/index.html')

def login_page(reauest):
    if reauest.method == 'POST':
        username = reauest.POST.get('username')
        password = reauest.POST.get('pass')
        user = authenticate(reauest, username=username, password=password)
        print(username, password)
        if user is not None:
            login(reauest, user)
            return redirect('home')
        else:
            return HttpResponse('Username or Password is incorrect!!!!!')
    return  render(reauest, 'accounts/index.html')

def logout_page(request):
    logout(request)
    return redirect('login')

def cart_page(request):
    return render(request, 'accounts/cart.html')
