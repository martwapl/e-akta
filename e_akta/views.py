from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import Permission


# Create your views here.
from .models import *
from .forms import *

User = get_user_model()

class EmployeeLoginView(View):
    # Login form for employees
    template_name = "e_akta/form.html"
    form_class = LoginForm
    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            return redirect("employee-dashboard")

            if user is None:
                messages.error(request, "Błędna nazwa użytkownika lub hasło")
                return redirect("employee-login")

        else:
            login(request, user)
            return redirect("employee-login")

        return render(request, self.template_name, {"form": form})

class EmployeeDashboardView(View):
    # Dashboard view after employee login
    template_name = "e_akta/employee_dashboard.html"
    def get(self, request):
        cases = Case.objects.all().order_by('-date_created')
        cases_count = Case.objects.all().count()
        context = {
            'cases': cases,
            'cases_count': cases_count,
        }
        return render(request, self.template_name, context)