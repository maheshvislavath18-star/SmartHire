from django.urls import path
from . import views

urlpatterns = [

    path('job/<int:job_id>/applicants/', views.recruiter_applicants, name='applicants'),

    path('edit-job/<int:id>/', views.edit_job, name='edit_job'),

    path('delete-job/<int:id>/', views.delete_job, name='delete_job'),

    path('add-job/', views.add_job, name='add_job'),

    path('', views.home, name='home'),

]