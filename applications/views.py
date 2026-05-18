from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from jobs.models import Job
from .models import Application


# 🔥 APPLY JOB VIEW
@login_required
def apply_job(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    # prevent duplicate applications
    if Application.objects.filter(job=job, user=request.user).exists():
        return redirect('dashboard')

    if request.method == "GET":
        return render(request, 'apply_job.html', {
            'job': job
        })

    if request.method == "POST":

        Application.objects.create(
            job=job,
            user=request.user,
            name=request.POST.get("name") or request.user.username,
            email=request.POST.get("email") or request.user.email,
            message=request.POST.get("message"),
            resume=request.FILES.get("resume")
        )

        return redirect('dashboard')


# 🔥 UPDATE STATUS (ACCEPT / REJECT)
@login_required
def update_status(request, app_id, status):

    application = get_object_or_404(Application, id=app_id)

    application.status = status
    application.save()

    return redirect('dashboard')


# 🔥 RECRUITER APPLICANTS VIEW (SEARCH + FILTER + SORT)
@login_required
def recruiter_applicants(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    applications = Application.objects.filter(job=job)

    # 🔍 SEARCH FILTER
    search = request.GET.get("search")
    if search:
        applications = applications.filter(
            Q(name__icontains=search) |
            Q(email__icontains=search)
        )

    # 🎯 STATUS FILTER
    status = request.GET.get("status")
    if status:
        applications = applications.filter(status=status)

    applications = applications.order_by('-id')

    return render(request, 'applicants_list.html', {
        'job': job,
        'applications': applications
    })


# 📄 RESUME LIST VIEW (RECRUITER)
@login_required
def resume_list(request):

    applications = Application.objects.exclude(
        resume=""
    ).exclude(
        resume__isnull=True
    ).order_by('-id')

    return render(request, 'resume_list.html', {
        'applications': applications
    })


# 📊 DASHBOARD STATS VIEW (NEW - IMPORTANT UPGRADE)
@login_required
def dashboard_stats(request):

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