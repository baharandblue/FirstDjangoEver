from django.shortcuts import render , redirect
from .forms import UserRegistrationForm , UserLogInForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

def user_register(request):
    if request.method =='POST' :
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=User.objects.create_user(cd['username'] , cd['email'] , cd['password'])
            user.first_name=cd['first_name']
            user.last_name=cd['last_name']
            user.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request , 'register.html' , {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = UserLogInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])  # Fixed typo
            if user:  # Simplified condition
                login(request, user)
                return redirect('home')
    else:
        form = UserLogInForm()
    return render(request, 'login.html', {'form': form})

    
def user_logout(request):
    logout(request)
    return redirect('home')