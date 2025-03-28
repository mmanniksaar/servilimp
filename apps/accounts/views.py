from django.shortcuts import render, redirect
from .forms import RegistrationForm
from apps.accounts.models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# email verification
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from apps.carts.views import _cart_id
from apps.carts.models import Cart, CartItem

def admin(request):
    return redirect('/admin')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split("@")[0] # poolitab meiliaadressi @ koha pealt ja annab positsiooni 0 kasutajanimeks
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()

            # user activation
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),  # encode users primari key
                'token': default_token_generator.make_token(user),  # generete default user token
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            return redirect('/login/?command=verification&email='+email)
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None: # 
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                print(is_cart_item_exists)
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)
                    print(cart_item)
                    for item in cart_item:
                        item.user = user
                        item.save()
            except:
                pass
            auth.login(request, user)
            # messages.success(request, 'You are logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'login.html')

@login_required(login_url = 'login') # funktsioon käivitub vaid siis kui logitud sisse
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link.')
        return redirect('register')
