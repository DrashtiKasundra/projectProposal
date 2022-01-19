from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Return an 'invalid login' error message.
            messages.success(request,('try again'))
            return redirect('login')
            
    else:
        return render(request,'authenticate/login.html',{})