from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):

    error_message = None  # Para enviar mensagens de erro para o template

    # 1. Verifica se o formulário foi enviado (método POST)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('app_welcome')
            else:
                error_message = "Senha incorreta. Tente novamente."

        except User.DoesNotExist:
            error_message = "Nenhum usuário encontrado com este email."
        except Exception as e:
            error_message = "Ocorreu um erro. Tente novamente."

    context = {'error': error_message}
    return render(request, "index.html", context)

def app_welcome(request):
    return render(request, 'app_ui_welcome.html')

def create_login(request):
    return render(request, 'index_create.html')