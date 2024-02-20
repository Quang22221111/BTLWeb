from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model, login
from . token import generate_token
from btl import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.decorators import login_required
from .form import UpdateUserForm, UpdateProfileForm

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def signin(request):    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username = username, password = password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Account Does Not Exist')
            return redirect('/signin')
    else:
        return render(request, 'home/signin.html')
    
def signout(request):
    logout(request)
    return redirect('/')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    
    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth_login(request, user)
        messages.success(request, "Your Account has been activated!")
        return redirect('/signin')
    else:
        messages.error(request, "Activation link is invalid!")
    
    return redirect('/index')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('/register')
                
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('/register')
                
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                    
                user.is_active = False
                user.save()
                    
                #Gửi tin nhắn cho email
                subject = "Welcome to my project"
                message = "Hello " + username + "! \n" + "Welcome to my project\n Thank you for joining my project to have some fun"
                send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                    
                    
                current_site = get_current_site(request)
                email_subject = "Confirm your account @ Project - Django Signin"
                message2 = render_to_string('confirmation.html', {
                    'username': user.username,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': generate_token.make_token(user),
                })
                email = EmailMessage(
                    email_subject,
                    message2,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                )
                email.fail_silently = True
                email.send()
                return redirect('/success_register')
                
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('/register')
            
    else:
        return render(request, 'home/register.html')

@login_required(login_url="/signin")
def success_register(request):
    return render(request, 'home/success_register.html')

@login_required
def profile(request):
    return render(request, 'home/profile.html')