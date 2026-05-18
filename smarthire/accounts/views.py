from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm
from .models import Profile


def register(request):

    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            Profile.objects.create(
                user=user,
                user_type=form.cleaned_data['user_type']
            )

            return redirect('login')

        else:
            print("ERRORS:", form.errors)

    return render(request, 'register.html', {'form': form})


def login_user(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def logout_user(request):

    logout(request)

    return redirect('login')