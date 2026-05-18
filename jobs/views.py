from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from jobs.models import Job
from applications.models import Application
from .forms import JobForm
from accounts.models import Profile


# 🔥 RECRUITER - SEE APPLICANTS
@login_required
def recruiter_applicants(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    applications = Application.objects.filter(job=job).order_by('-id')

    return render(request, 'applicants_list.html', {
        'job': job,
        'applications': applications
    })


# 🔥 HOME PAGE (SEARCH + FILTERS)
def home(request):

    query = request.GET.get('q')
    location = request.GET.get('location')
    salary = request.GET.get('salary')
    experience = request.GET.get('experience')

    jobs = Job.objects.all()

    # 🔍 SEARCH FILTER
    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(skills__icontains=query) |
            Q(company__icontains=query)
        )

    # 📍 LOCATION FILTER
    if location:
        jobs = jobs.filter(location__icontains=location)

    # 💰 SALARY FILTER
    if salary:
        try:
            jobs = jobs.filter(salary__gte=int(salary))
        except:
            pass

    # 📊 EXPERIENCE FILTER (simple skill-based match)
    if experience:
        jobs = jobs.filter(skills__icontains=experience)

    return render(request, 'home.html', {'jobs': jobs})


# 🔥 JOB DETAIL PAGE
def job_detail(request, id):

    job = get_object_or_404(Job, id=id)

    return render(request, 'job_detail.html', {'job': job})


# 🔥 ADD JOB (RECRUITER ONLY)
@login_required
def add_job(request):

    profile = get_object_or_404(Profile, user=request.user)

    if profile.user_type != "recruiter":
        return redirect('home')

    if request.method == "POST":

        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()

            return redirect('dashboard')

    else:
        form = JobForm()

    return render(request, 'add_job.html', {'form': form})


# 🔥 EDIT JOB
@login_required
def edit_job(request, id):

    job = get_object_or_404(Job, id=id)

    profile = get_object_or_404(Profile, user=request.user)

    if profile.user_type != "recruiter":
        return redirect('home')

    if request.method == "POST":

        form = JobForm(request.POST, instance=job)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = JobForm(instance=job)

    return render(request, 'edit_job.html', {'form': form})


# 🔥 DELETE JOB
@login_required
def delete_job(request, id):

    job = get_object_or_404(Job, id=id)

    profile = get_object_or_404(Profile, user=request.user)

    if profile.user_type != "recruiter":
        return redirect('home')

    job.delete()

    return redirect('dashboard')


# 📊 DASHBOARD (STATS)
@login_required
def dashboard(request):

    total_jobs = Job.objects.count()
    total_applications = Application.objects.count()

    pending = Application.objects.filter(status="Pending").count()
    accepted = Application.objects.filter(status="Accepted").count()
    rejected = Application.objects.filter(status="Rejected").count()

    return render(request, 'dashboard.html', {
        'total_jobs': total_jobs,
        'total_applications': total_applications,
        'pending': pending,
        'accepted': accepted,
        'rejected': rejected
    })