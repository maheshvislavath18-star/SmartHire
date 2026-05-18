"""
URL configuration for smarthire project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 🚀 MEDIA IMPORT (FOR RESUME FILES)
from django.conf import settings
from django.conf.urls.static import static

# 👇 IMPORT YOUR DASHBOARD VIEW (IMPORTANT)
from jobs import views as job_views


urlpatterns = [
    # 🧑‍💻 ADMIN PANEL
    path('admin/', admin.site.urls),

    # 🔐 AUTH SYSTEM
    path('accounts/', include('accounts.urls')),

    # 🏠 JOBS APP (HOME PAGE + JOBS)
    path('', include('jobs.urls')),

    # 📄 APPLICATION SYSTEM
    path('applications/', include('applications.urls')),

    # 📊 DASHBOARD (IMPORTANT FIX FOR YOUR 404 ERROR)
    path('dashboard/', job_views.dashboard, name='dashboard'),
]

# 🚀 MEDIA FILE SERVING (RESUME DOWNLOAD FIX)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)