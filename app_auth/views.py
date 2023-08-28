from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import ExtendedUserCreationForm


def my_login(request):
    main_page_url = reverse("main-page")
    if request.method == "GET":
        if not request.user.is_authenticated:
            return render(request, 'app_auth/login.html')
        return redirect(main_page_url)

    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        redirect_url = reverse("profile")
        login(request, user)
        return redirect(redirect_url)

    return render(request, 'app_auth/login.html', {"error": "Такой пользователь не найден"})


def profile(request):
    return render(request, "app_auth/profile.html")


def my_logout(request):
    login_url = reverse("login")
    logout(request)
    return redirect(login_url)


def register_view(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            login(request, user=user)
            return redirect(reverse('profile'))
    else:
        form = ExtendedUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'app_auth/register.html', context)

