# views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('app_dashboard') 
    error_message = None

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('app_dashboard')
            else:
                error_message = "Senha incorreta. Tente novamente."

        except User.DoesNotExist:
            error_message = "Nenhum usuário encontrado com este email."
        except Exception as e:
            error_message = f"Ocorreu um erro: {e}"

    context = {'error': error_message}
    return render(request, "login.html", context)

def login_create(request):
    if request.user.is_authenticated:
        return redirect('app_dashboard')

    error_message = None

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cf_password = request.POST.get('cf_password')

        if password != cf_password:
            error_message = "As senhas não coincidem. Tente novamente."
        else:
            try:
                user = User.objects.create_user(username=email, email=email, password=password)
                
                user_auth = authenticate(request, username=email, password=password)
                if user_auth is not None:
                    auth_login(request, user_auth)
                    return redirect('app_dashboard') 
                else:
                    error_message = "Erro ao autenticar após a criação."

            except IntegrityError:
                error_message = "Um usuário com este email já existe."
            except Exception as e:
                error_message = f"Ocorreu um erro inesperado: {e}"

    context = {'error': error_message}
    return render(request, 'login_create.html', context)

@login_required
def app_dashboard(request):
    return render(request, 'app_ui_dashboard.html')

@login_required
def app_users(request):
    return render(request, 'app_ui_users.html')

@login_required
def app_requests(request):
    return render(request, 'app_ui_requests.html')

@login_required
def app_history(request):
    return render(request, 'app_ui_history.html')

@login_required
def app_reports(request):
    return render(request, 'app_ui_reports.html')

@login_required
def app_items(request):
    return render(request, 'app_ui_items.html')

@login_required
def app_configs(request):
    return render(request, 'app_ui_configs.html')