from django.contrib.auth.mixins import PermissionRequiredMixin,\
    LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

# Create your views here.
from .models import Case, File, Event
from .forms import LoginForm, FileUploadForm, AddCaseForm, \
    RegisterUserForm, CaseUpdateFormSU, AddEventForm, EmailForm
from .token import account_activation_token
User = get_user_model()


class LoginView(View):
    # Login view

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
                return redirect("login")
            elif user.groups.filter(name='clients').exists():
                login(request, user)
                return redirect("customer-dashboard")
            else:
                login(request, user)
                return redirect("dashboard")

        return render(request, self.template_name, {"form": form})


class LogoutView(View):
    # Logout view
    def get(self, request):
        logout(request)
        return redirect("/")

class EmployeeDashboardView(LoginRequiredMixin, PermissionRequiredMixin, View):
    # Dashboard view for employees
    permission_required = ["e_akta.add_case", "e_akta.add_file"]
    template_name = "e_akta/employee_dashboard.html"
    login_url = '/employee'

    def get(self, request):
        cases = Case.objects.all().order_by('-date_created')
        cases_count = Case.objects.all().count()
        context = {
            'cases': cases,
        }
        return render(request, self.template_name, context)


class CustomerDashboardView(LoginRequiredMixin, PermissionRequiredMixin, View):
    # Dashboard view for clients

    login_url = '/'
    permission_required = ["e_akta.view_case"]
    template_name = "e_akta/customer_dashboard.html"

    def get(self, request):
        cases = Case.objects.all().order_by('-date_created')
        mail = self.request.user.email
        # profile = Profile.objects.filter(email=mail)
        context = {
            'cases': cases,
            # 'profile': profile,
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
    # View for uploading files

    login_url = '/'
    permission_required = ["e_akta.change_file"]
    model = File
    template_name = "e_akta/upload.html"
    form_class = FileUploadForm
    success_url = '/case/{case_id}'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class DeleteFileView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    # View for deleting files
    login_url = '/'
    permission_required = ["e_akta.delete_file"]
    model = File
    template_name = "e_akta/delete.html"
    success_url = '/case/{case_id}'


class AddCaseView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    # View for adding new case

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
    # View for editing case form

    login_url = '/'
    permission_required = ["e_akta.change_case"]
    model = Case
    form_class = CaseUpdateFormSU
    template_name = 'e_akta/edit_case.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['groups'] = self.request.user
        return kwargs


class DownloadView(LoginRequiredMixin, PermissionRequiredMixin, View):
    # View of file download
    login_url = '/'
    permission_required = ["e_akta.view_case", "e_akta.view_file"]
    template_name = 'e_akta/download'
    success_url = '/download/{file_id}'

    def get(self, request, file_id):

        file = get_object_or_404(File, pk=file_id)
        response = HttpResponse(file.file, content_type='application/pdf')
        response['Content-Disposition'] = \
            f'attatchment; filename="{file.file.name}"'

        return response


class AddEventView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    # View for adding new events
    login_url = '/'
    permission_required = ["e_akta.add_event"]
    template_name = 'e_akta/add_event.html'
    model = Event
    form_class = AddEventForm
    success_url = reverse_lazy('calendar')

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        f.save()
        return super().form_valid(form)


class CalendarView(LoginRequiredMixin, PermissionRequiredMixin, View):
    # View events in calendar

    login_url = '/'
    permission_required = ["e_akta.view_event"]
    template_name = "e_akta/calendar.html"

    def get(self, request):
        events = Event.objects.all()
        context = {
            "events": events,
        }
        return render(request, self.template_name, context)


class EventsView(LoginRequiredMixin, PermissionRequiredMixin, View):
    # View of specific event
    login_url = '/'
    permission_required = ["e_akta.view_event"]
    template_name = "e_akta/calendar.html"

    def get(self, request):

        events = Event.objects.all()
        output = []
        for event in events:
            output.append({
                'title': event.title,
                'start': event.start,
                'end': event.end,
            })

        return JsonResponse(output, safe=False)


class ContactFormView(LoginRequiredMixin, PermissionRequiredMixin, View):
    # Email invitation for new clients to register

    login_url = '/'
    permission_required = ["e_akta.view_sendemail"]
    template_name = 'e_akta/send_email.html'
    form = EmailForm()

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data.get('recipient')
            subject = form.cleaned_data.get('subject')
            user = self.request.user
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('e_akta/invitation_mail.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[recipient]
            )
            messages.success(request, "Zaproszenie zostało wysłane")
            return redirect('dashboard')
        else:
            form = EmailForm()
        return render(request, self.template_name, {'form': form})


class RegisterView(View):
    # Registration form view for new clients
    template_name = 'e_akta/register.html'
    form = RegisterUserForm

    def get(self, request, uidb64, token):
        form = RegisterUserForm
        uid = force_str(urlsafe_base64_decode(uidb64))
        User.objects.get(pk=uid)
        return render(request, self.template_name, {'form': form})

    def post(self, request, uidb64, token):
        form = self.form(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = "Aktywuj swoje konto"
            message = render_to_string('e_akta/activation_mail.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.POST.get("email")]
            )

            return HttpResponse("Zaraz otrzymasz maila z linkiem aktywacyjnym")
        else:
            form = RegisterUserForm
        return render(request, self.template_name, {'form': form})


class ActivateView(View):
    # Registration confirmation
    def get(self, request, uidb64, token):
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if user is not None and \
                account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.signup_confirmation = True
            group = Group.objects.get(name='clients')
            user.groups.add(group)
            user.save()
            messages.success(request, "Konto zostało aktywowane.")
            return redirect('login')
        else:
            return HttpResponse("Nie udało się założyć konta.")
