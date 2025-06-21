from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash, get_user_model
from . import form as fm
from .utils import send_verification_email
from django.contrib.auth.decorators import login_required

User = get_user_model()

# This where users can register/create an account
def register_user(request):
    if request.method == 'POST':
        form = fm.RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.username = user.email
            user.save()
            send_verification_email(user, request)
            messages.success(request, 'Email verification link sent to your inbox.')
            return redirect('register')
        else:
            messages.warning(request, 'Something went wrong. Please try again')
            return redirect('register')
    else:
        form = fm.RegisterUserForm()
        context = {'form': form}

    return render(request, 'accounts/register.html', context)


def verify_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your email has been verified. You can now log in')
        return redirect('login')
    else:
        messages.warning(request, 'Invalid verification link')
        return redirect('register')

# This is where users can log in
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f'Welcome {user.first_name}')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Check credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')


# This is where users can log out from their account
def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')


# This is where users can change their password in-app
@login_required
def change_password(request):
    if request.method == 'POST':
        form = fm.UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password is updated')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please try check form errors')
            return redirect('change_password')
    else:
        form = fm.UserPasswordChangeForm(request.user)
        context = {'form': form}

    return render(request, 'accounts/change_password.html', context)

# This is where the user can update their profile
@login_required()
def update_profile(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'POST':
        form = fm.UserProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return redirect('update-profile', user.pk)
    else:
        form = fm.UserProfileUpdateForm(instance=user)
        context = {'form': form, 'user': user}

    return render(request, 'accounts/update_profile.html', context)


# This is where the user can disable account
@login_required()
def disable_account(request, pk):
    user = User.objects.get(pk = request.user.pk)

    user.is_active = False
    user.save()
    return redirect('login')


# this is where the user can view profile details
@login_required()
def profile_details(request, pk):
    user = User.objects.get(pk=request.user.pk)
    context = { 'user': user}
    return render(request, 'accounts/profile_details.html', context)