from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('job/<int:id>/',
         views.job_detail,
         name='job_detail'),

    path('add-job/',
         views.add_job,
         name='add_job'),

    path('edit-job/<int:id>/',
         views.edit_job,
         name='edit_job'),

    path('delete-job/<int:id>/',
         views.delete_job,
         name='delete_job'),
]