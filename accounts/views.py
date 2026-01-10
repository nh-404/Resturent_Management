from django.shortcuts import render,redirect
from accounts.models import User
from django.contrib.auth import login

# Create your views here.
def signUp(request):

    if request.method == 'POST':
        full_name = request.POST.get('full_name')   
        phone = request.POST.get('phone')   
        email = request.POST.get('email')   
        password = request.POST.get('password') 

        if email and password and full_name and phone:

            user = User.objects.create_user(
                email=email,
                password=password,
                full_name=full_name,
                phone=phone,
            )

            # login(request, user)
            return redirect('home')

        else:
            
            return redirect('signUP')


    return render(request, 'auth/signUp.html')

def signIn(request):
    return render(request, 'auth/login.html')