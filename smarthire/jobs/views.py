from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm


def home(request):

    jobs = Job.objects.all()

    return render(request, 'home.html', {'jobs': jobs})


def job_detail(request, id):

    job = Job.objects.get(id=id)

    return render(request, 'job_detail.html', {'job': job})


def add_job(request):

    if request.method == "POST":

        form = JobForm(request.POST)

        print(form.errors)

        if form.is_valid():

            form.save()

            return redirect('home')

    else:

        form = JobForm()

    return render(request, 'add_job.html', {'form': form})


#Edit View
@login_required
def edit_job(request, id):

    job = Job.objects.get(id=id)

    if request.method == "POST":

        form = JobForm(request.POST, instance=job)

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    else:

        form = JobForm(instance=job)

    return render(request, 'edit_job.html', {'form': form})