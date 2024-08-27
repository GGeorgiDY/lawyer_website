from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordChangeForm, ProfileForm
from django.contrib import messages

import json
import os
from django.http import JsonResponse
from django.conf import settings

from django.http import HttpResponse
# from .forms import ContactForm
from .forms import CustomForm

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .models import CustomUser
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model


def get_translations(request):
    # Construct the path to the translations.json file
    translations_file_path = os.path.join(settings.BASE_DIR, 'lawyer_website', 'main_data', 'translations.json')

    # Debugging output
    print(f"Looking for translations at: {translations_file_path}")

    if not os.path.exists(translations_file_path):
        print("Translations file not found")
        return JsonResponse({'error': 'Translations file not found'}, status=404)

    try:
        with open(translations_file_path, 'r', encoding='utf-8') as json_file:
            translations = json.load(json_file)
            print("Translations loaded successfully")
    except Exception as e:
        print(f"Error loading translations: {e}")
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse(translations)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def location(request):
    return render(request, 'location.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'registration/activation_invalid.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until email confirmation
            user.save()

            # Send email confirmation
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('registration/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_mail(mail_subject, message, 'yordan.lawyer@gmail.com', [user.email])

            return render(request, 'registration/confirmation_email_sent.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('home')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = ProfileForm(instance=user)

    return render(request, 'profile.html', {'form': form})


# def contact_view(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Process form data here
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             phone = form.cleaned_data['phone']
#             message = form.cleaned_data['message']
#             return HttpResponse("Message sent!")
#     else:
#         if request.user.is_authenticated:
#             initial_data = {
#                 'name': f"{request.user.first_name} {request.user.last_name}",
#                 'email': request.user.email
#             }
#             form = ContactForm(initial=initial_data)
#         else:
#             form = ContactForm()
#
#     return render(request, 'location.html', {'form': form})


def custom_view(request):
    if request.method == "POST":
        form = CustomForm(request.POST)
        if form.is_valid():
            # Process the form data here
            header = form.cleaned_data['header']
            text = form.cleaned_data['text']
            # Save or process the data as needed
            return redirect('success_url')  # Redirect to a success page or handle accordingly
    else:
        if request.user.is_authenticated:
            form = CustomForm()  # Empty form for authenticated users to fill in
        else:
            form = None  # Form should not be displayed to unauthenticated users

    return render(request, 'location.html', {'form': form})
