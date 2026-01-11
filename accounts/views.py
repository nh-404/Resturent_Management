from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from accounts.models import User
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import login, authenticate, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator



#_______signUP___
def signUp(request):

    if request.method == 'POST':

        full_name = request.POST.get('full_name')   
        phone = request.POST.get('phone')   
        email = request.POST.get('email')   
        password = request.POST.get('password') 

        #chexking data from db
        if email and password and full_name and phone:

            user = User.objects.create_user(
                email=email,
                password=password,
                full_name=full_name,
                phone=phone,
            )

            login(request, user)
            return redirect('home')

        else:
            
            return redirect('signUP')


    return render(request, 'auth/signUp.html')



#_____Login___
def signIn(request):

    if request.method == 'POST':

        email = request.POST.get('email')   
        password = request.POST.get('password') 

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            return render(request, 'auth/login.html', {'error' : 'Invalid password or email'})


    return render(request, 'auth/login.html')




#___-Logout__
def signOut(request):

    logout(request)
    return redirect('login')




#___________reset_password__________
def reset_password(request):

    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_link = request.build_absolute_uri(
                reverse('reset_password_confirm', kwargs={'uidb64': uid, 'token': token})
            )



            # Render HTML template
            html_content = render_to_string('auth/reset_password//reset_email_template.html', {'reset_link': reset_link})

            # Optional: plain text fallback
            text_content = f"""
            Hello,

            You requested a password reset. Click the link below to reset your password:

            {reset_link}

            If you did not request this, please ignore this email.
            """

            # Send email
            msg = EmailMultiAlternatives(
                subject="Password Reset Request",
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            

        except User.DoesNotExist:
            pass

        return render(request,'auth/reset_password/reset_password_sent.html')

    return render(request,'auth/reset_password/reset_password.html')




#___________reset_password_confirm__________
def reset_password_confirm(request, uidb64, token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except (User.DoesNotExist, ValueError, TypeError):
        user = None

#__User Condition checking___
    if user is None or not default_token_generator.check_token(user, token):
        return render(
            request,
            'auth/reset_password/reset_password_invalid.html'
        )

#__password Condition checking for template___
    if request.method == 'POST':

        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        if not password or not confirm_password:
            return render(request, 'auth/reset_password/reset_password_confirm.html', {'error': 'All fields are required'})

        if password != confirm_password:
            return render(request, 'auth/reset_password/reset_password_confirm.html',{'error': 'Passwords do not match'})

#__Reset hash password______
        user.set_password(password)
        user.save()

        return redirect('login')


    return render(request, 'auth/reset_password/reset_password_confirm.html')