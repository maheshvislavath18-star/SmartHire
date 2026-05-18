from django.shortcuts import render, redirect
from .models import Application


def apply_job(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Application.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect("home")

    return render(request, "apply_job.html")