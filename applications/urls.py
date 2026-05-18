from django.urls import path
from . import views

urlpatterns = [

    # 👤 APPLY JOB (APPLICANT SIDE)
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),

    # 🔥 ACCEPT / REJECT APPLICATION (RECRUITER)
    path('application/<int:app_id>/<str:status>/', views.update_status, name='update_status'),

    # 📄 RESUME LIST (RECRUITER DASHBOARD)
    path('resumes/', views.resume_list, name='resume_list'),

]