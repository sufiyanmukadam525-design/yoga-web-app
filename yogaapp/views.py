from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, ProfileForm
from .models import Profile, RegisteredUser

class Register(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'yogaapp/signup.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            admin_code = form.cleaned_data.get('admin_code')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'yogaapp/signup.html', {'form': form})

            user = User.objects.create_user(username=username, email=email, password=password)
            if admin_code and admin_code == 'ADMIN123':
                user.is_staff = True
                user.save()
            RegisteredUser.objects.create(user=user, username=username, email=email)
            messages.success(request, 'Registration successful. You can log in now.')
            return redirect('login')
        return render(request, 'yogaapp/signup.html', {'form': form})

class Login(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'yogaapp/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            messages.error(request, 'Invalid credentials.')
        return render(request, 'yogaapp/login.html', {'form': form})

class Logout(View):
    def get(self, request):
        logout(request)
        messages.info(request, 'Logged out.')
        return redirect('login')

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'yogaapp/home.html')
        else:
            return render(request, 'yogaapp/loading.html')

@login_required
def profile_view(request):
    # Get or create profile for logged in user
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")  # Replace with your url name
    else:
        form = ProfileForm(instance=profile)

    return render(request, "yogaapp/profile.html", {
        "profile": profile,
        "form": form
    })

class Base(View):
    def get(self, request):
        return render(request, 'yogaapp/base.html')
<<<<<<< HEAD


class ProfileEdit(View):
    def get(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = ProfileForm(instance=profile)
        return render(request, "yogaapp/profile_edit.html", {
            "form": form
        })

    def post(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
        return render(request, "yogaapp/profile_edit.html", {
            "form": form
        })
=======
>>>>>>> 378cfd2d643889c1b7f817a9487d8e62135be505
