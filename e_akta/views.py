from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.urls import reverse_lazy
from PyPDF2 import PdfWriter, PdfReader

# Create your views here.
from .models import Case, File
from .forms import LoginForm, FileUploadForm, AddCaseForm, RegisterForm, CaseUpdateForm, CaseUpdateFormSU
User = get_user_model()
from .views import *


class EmployeeLoginView(View):
    # Login form for employees
    template_name = "e_akta/login.html"
    form_class = LoginForm
    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, "Błędna nazwa użytkownika lub hasło")
                return redirect("employee-login")
            else:
                login(request, user)
                return redirect("dashboard")

        return render(request, self.template_name, {"form": form})

class EmployeeLogoutView(View):
    # Dashboard view after employee logout
    def get(self, request):
        logout(request)
        return redirect("/")


class EmployeeDashboardView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ["e_akta.view_case", "e_akta.view_file"]
    template_name = "e_akta/employee_dashboard.html"
    login_url = '/'

    def get(self, request):
        cases = Case.objects.all().order_by('-date_created')
        cases_count = Case.objects.all().count()
        context = {
            'cases': cases,
            'cases_count': cases_count,
        }
        return render(request, self.template_name, context)


class CaseView(LoginRequiredMixin, PermissionRequiredMixin, View):
    # View of case contents
    login_url = '/'
    permission_required = ["e_akta.view_case"]
    template_name = "e_akta/case_content.html"

    def get(self, request, pk):

        case = Case.objects.get(id=pk)
        file = File.objects.filter(case_id=pk).order_by('-date_created')
        context = {
            'file': file,
            'case': case,
        }
        return render(request, self.template_name, context)
class FileUploadView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = '/'
    permission_required = ["e_akta.change_file"]
    model = File
    template_name = "e_akta/upload.html"
    form_class = FileUploadForm


    success_url = '/case/{case_id}'


class DeleteFileView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):

    login_url = '/'
    permission_required = ["e_akta.delete_file"]
    model = File
    template_name = "e_akta/delete.html"
    success_url = '/case/{case_id}'

class AddCaseView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    login_url = "/"
    permission_required = ["e_akta.add_case"]
    model = Case
    form_class = AddCaseForm
    template_name = "e_akta/add_case.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        f.save()
        return super().form_valid(form)

class EditCaseView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

    login_url = '/'
    permission_required = ["e_akta.change_case"]
    model = Case
    form_class = CaseUpdateFormSU
    template_name = 'e_akta/edit_case.html'
    success_url = reverse_lazy('dashboard')
    def form_valid(self, form):
            f = form.save(commit=False)
            f.user = self.request.user
            f.save()
            return super().form_valid(form)


class DownloadView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = '/'
    permission_required = ["e_akta.view_case", "e_akta.view_file"]
    template_name = 'e_akta/download'
    success_url = '/download/{file_id}'

    def get(self, request, file_id):
        file = get_object_or_404(File, pk=file_id)
        response = HttpResponse(file.file, content_type='application/pdf')
        response['Content-Disposition'] = f'attatchment; filename="{file.file.name}"'
        return response