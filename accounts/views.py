from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
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
        if not all([full_name, phone, email, password]):
            messages.error(request, 'All fields are requried')
            return redirect('signUp')


        #duplicate email checking
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already existed!")
            return redirect('signUp')


        #password validation
        try:
            validate_password(password)

        except ValidationError as e:

            for error in e.messages:
                messages.error(request, error)
            return redirect('signUp')


        #Create User
        user = User.objects.create_user(
                email=email,
                password=password,
                full_name=full_name,
                phone=phone,
            )

        #user validation
        login(request, user)
        messages.success(request, 'Account created successfully')
        return redirect('home')

    return render(request, 'auth/signUp.html')






#_____Login___nh404@duxk.com
def signIn(request):

    if request.method == 'POST':

        email = request.POST.get('email')   
        password = request.POST.get('password') 


        #validate email and password
        if not email or not password:
            messages.error(request, "Email and Password required!")
            return redirect('login')

        user = authenticate(request, email=email, password=password)


        #Validate Login
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "invalid Email or Password!")
            return redirect('login')

    return render(request, 'auth/login.html')




#___-Logout__
def signOut(request):

    logout(request)
    messages.success(request, 'Logout successfully!')
    return redirect('home')




#___________reset_password__________
def reset_password(request):

    if request.method == 'POST':

        email = request.POST.get('email')

        user = User.objects.filter(email=email).first()

        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_link = request.build_absolute_uri(
                reverse(
                    'reset_password_confirm',
                    kwargs={'uidb64': uid, 'token': token}
                )
            )

            html_content = render_to_string(
                'auth/reset_password/reset_email_template.html',
                {'reset_link': reset_link}
            )

            text_content = f"""
                Hello,

                You requested a password reset. Click the link below to reset your password:

                {reset_link}

                If you did not request this, please ignore this email.
                """
                
            email_message = EmailMultiAlternatives(

                subject='Request for password reset',
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
            )

            email_message.attach_alternative(html_content, 'text/html')
            email_message.send()

        # Always show success page (prevents email enumeration)
        return render(request,'auth/reset_password/reset_password_sent.html')

    return render(request,'auth/reset_password/reset_password.html')






# #___________reset_password_confirm__________
def reset_password_confirm(request, uidb64, token):

    # Decode the user
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError):
        user = None

    # Validate token
    if not user or not default_token_generator.check_token(user, token):
        return render(
            request,
            'auth/reset_password/reset_password_invalid.html'
        )

    errors = []  # Collect validation errors

    if request.method == 'POST':

        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Required fields
        if not password or not confirm_password:
            errors.append('All fields are required.')

        # Password match
        elif password != confirm_password:
            errors.append('Passwords do not match.')

        # Django password validation
        else:
            try:
                validate_password(password, user)
            except ValidationError as e:
                errors.extend(e.messages)

        # If no errors, set password
        if not errors:
            user.set_password(password)
            user.save()
            return redirect('login')

    # Render template with errors if any
    return render(request,'auth/reset_password/reset_password_confirm.html',{'errors': errors, 'uidb64': uidb64, 'token': token})


