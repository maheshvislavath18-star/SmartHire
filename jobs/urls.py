from django.urls import path
from . import views

urlpatterns = [
    # 🏠 HOME PAGE (IMPORTANT - ROOT URL)
    path('', views.home, name='home'),

    # ➕ ADD JOB
    path('add-job/', views.add_job, name='add_job'),

    # ✏️ EDIT JOB
    path('edit-job/<int:id>/', views.edit_job, name='edit_job'),

    # ❌ DELETE JOB
    path('delete-job/<int:id>/', views.delete_job, name='delete_job'),

    # 👥 APPLICANTS LIST (RECRUITER VIEW)
    path('job/<int:job_id>/applicants/', views.recruiter_applicants, name='applicants'),
]