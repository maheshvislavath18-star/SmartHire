from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import Profile

from jobs.models import Job
from applications.models import Application


# REGISTER
def register(request):

    form = RegisterForm()

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # create profile safely
            Profile.objects.get_or_create(
                user=user,
                defaults={
                    'user_type': form.cleaned_data['user_type']
                }
            )

            return redirect('login')

    return render(request, 'register.html', {'form': form})


# LOGIN
def login_user(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            # ALWAYS GO TO DASHBOARD
            return redirect('dashboard')

        else:

            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')


# LOGOUT
def logout_user(request):

    logout(request)

    return redirect('login')


# DASHBOARD
@login_required
def dashboard(request):

    profile = Profile.objects.get(user=request.user)

    # RECRUITER DASHBOARD
    if profile.user_type == "recruiter":

        jobs = Job.objects.filter(
            posted_by=request.user
        )

        return render(
            request,
            'recruiter_dashboard.html',
            {'jobs': jobs}
        )

    # APPLICANT DASHBOARD
    else:

        applications = Application.objects.filter(
            user=request.user
        )

        return render(
            request,
            'applicant_dashboard.html',
            {'applications': applications}
        )