from django.urls import path
from . import views

urlpatterns = [
    path("apply/", views.apply_job, name="apply_job"),
]