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


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
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


