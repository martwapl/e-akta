from django.test import TestCase
import pytest
from django.test import Client
from django.contrib.auth.models import User
from django.core import mail
from .views import *
from .models import *
c = Client


# Create your tests here.

def test_login_get(client):
    url = "/"
    response = client.get(url)
    assert response.status_code == 200
@pytest.mark.django_db
def test_login_post(client):
    url = "/"
    response = client.post(url, {
        "username": "gargamel",
        "password": "smerfetka",
    })
    assert response.status_code == 302

@pytest.mark.django_db
def test_client_logout(client):
    url = "/logout/"
    response = client.get(url)

    assert response.status_code == 302
@pytest.mark.django_db
def test_employee_dashboard_view_SU(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_superuser(username=username, password=password)
    client.login(username=username, password=password)
    url = "/dashboard/"
    response = client.get(url)

    assert response.status_code == 200

@pytest.mark.django_db
def test_employee_dashboard_view_without_permission(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    url = "/dashboard/"
    response = client.get(url)

    assert response.status_code == 403

@pytest.mark.django_db
def test_employee_dashboard_not_logged_in(client):
    url = "/dashboard/"
    response = client.get(url)
    assert response.status_code == 302
@pytest.mark.django_db
def test_client_dashboard_view_SU(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_superuser(username=username, password=password)
    client.login(username=username, password=password)
    url = "/client_dashboard/"
    response = client.get(url)

    assert response.status_code == 200

@pytest.mark.django_db
def test_employee_dashboard_not_logged_in(client):
    url = "/client_dashboard/"
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_case_view_not_logged_in(client):
    url = "/case/5"
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_case_view_without_permission(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    url = "/case/5"
    response = client.get(url)

    assert response.status_code == 403

@pytest.mark.django_db
def test_add_case_not_logged_in(client):
    url = "/add_case/"
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_add_case_view_SU(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_superuser(username=username, password=password)
    client.login(username=username, password=password)
    url = "/add_case/"
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_case_view_without_permission(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    url = "/add_case/"
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_add_file_not_logged_in(client):
    url = "/upload/"
    response = client.get(url)
    assert response.status_code == 302

def test_add_file_view_SU(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_superuser(username=username, password=password)
    client.login(username=username, password=password)
    url = "/upload/"
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_file_view_without_permission(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    url = "/upload/"
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_download_file_not_logged_in(client):
    url = "/download/2"
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_delete_file_view_not_logged_in(client):
    url = "/delete/9"
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_add_delete_view_without_permission(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    url = "/delete/9"
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_add_delete_view_file_does_not_exist(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_superuser(username=username, password=password)
    client.login(username=username, password=password)
    url = "/delete/9"
    response = client.get(url)
    assert response.status_code == 404

@pytest.mark.django_db
def test_edit_case_view_not_logged_in(client):
    url = "/edit_case/6"
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_edit_case_view_without_permission(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    url = "/edit_case/6"
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_calendar_view_not_logged_in(client):
    url = "/calendar/"
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_calendar_view_without_permission(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    url = "/calendar/"
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_calendar_view(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_superuser(username=username, password=password)
    client.login(username=username, password=password)
    url = "/calendar/"
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_event_view_not_logged_in(client):
    url = "/events/"
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_event_view_without_permission(client):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    url = "/events/"
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_event_view(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    url = "/events/"
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_event_view_without_permission(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_superuser(username=username, password=password)
    client.login(username=username, password=password)
    url = "/events/"
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_event_view_not_logged_in(client):
    url = "/add_event/"
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_add_event_view_not_logged_in(client):
    url = "/add_event/"
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_add_event_view_without_permission(client, django_user_model):
    username = "test"
    password = "abecadlo"
    user = django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    url = "/add_event/"
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_add_event_view(client, django_user_model):
    username = "test"
    password = "abecadlo"
    user = django_user_model.objects.create_superuser(username=username, password=password)
    client.login(username=username, password=password)
    url = "/add_event/"
    response = client.get(url)
    assert response.status_code == 200
@pytest.mark.django_db
def test_contact_form_view_not_logged_in(client):
    url = "/invitation/"
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_contact_form_without_permission(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    url = "/invitation/"
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_contact_form_view(client, django_user_model):
    username="test"
    password="abecadlo"
    user=django_user_model.objects.create_superuser(username=username, password=password)
    client.login(username=username, password=password)
    url = "/invitation/"
    response = client.get(url)
    assert response.status_code == 200

def test_send_mail(mailoutbox):
    mail.send_mail(
        'Subject',
        'Content',
        'from@test.com',
        ['to@test.com']
    )
    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == 'Subject'
    assert mail.outbox[0].body == 'Content'
    assert mail.outbox[0].from_email == 'from@test.com'
    assert mail.outbox[0].to == ['to@test.com']

@pytest.mark.django_db
def test_register_view_create_user(client):
    client.post('/register/MQ/bohtdk-13e50eb50d87f1c48e046e09c51f32e9', {
        'username': 'test1',
        'email': 'test1@test.com',
        'first_name': 'Jan',
        'last_name': 'Testowy',
        'password1': 'przykladowehaslo',
        'password2': 'przykladowehaslo'
    })
    url = '/register/MQ/bohtdk-13e50eb50d87f1c48e046e09c51f32e9'
    response = client.post(url)
    assert Profile.objects.filter(user__username='test1').exists()
    assert response.status_code == 200
