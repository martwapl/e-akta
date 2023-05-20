"""
URL configuration for finalProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from e_akta import views as pr_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pr_views.LoginView.as_view(), name="login"),
    path('dashboard/', pr_views.EmployeeDashboardView.as_view(), name="dashboard"),
    path('client_dashboard/', pr_views.CustomerDashboardView.as_view(), name="customer-dashboard"),
    path('logout/', pr_views.LogoutView.as_view(), name="logout"),
    path('case/<int:pk>', pr_views.CaseView.as_view(), name="case-view"),
    path('upload/', pr_views.FileUploadView.as_view(), name="upload"),
    path('delete/<int:pk>', pr_views.DeleteFileView.as_view(), name="delete"),
    path('add_case/', pr_views.AddCaseView.as_view(), name="add-case"),
    path('edit_case/<int:pk>', pr_views.EditCaseView.as_view(), name="edit-case"),
    path('download/<int:file_id>', pr_views.DownloadView.as_view(), name="download"),
    path('calendar/', pr_views.CalendarView.as_view(), name="calendar"),
    path('add_event/', pr_views.AddEventView.as_view(), name="add-event"),
    path('events/', pr_views.EventsView.as_view(), name="events"),
    path('register/<uidb64>/<token>', pr_views.RegisterView.as_view(), name="register"),
    path('activate/<uidb64>/<token>', pr_views.ActivateView.as_view(), name="activate"),
    path('invitation/', pr_views.ContactFormView.as_view(), name="invite"),

]