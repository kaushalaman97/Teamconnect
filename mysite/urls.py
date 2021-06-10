"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from normal_user.views import *
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include("normal_user.urls")),
    path('captcha/', include('captcha.urls')),
    path('i18n/',include('django.conf.urls.i18n')),
	path('employee-task-list',EmployeeTaskList.as_view(),name='employee_task_list'),
	path('employee-task-list-detail/<int:id>',EmployeeTaskListDetail.as_view(),name='employee-task-list-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.MEDIA_NEW_URL,document_root=settings.MEDIA_ROOT)

handler404 = 'normal_user.views.error_404'
# handler500 = 'normal_user.views.custom_error_view'