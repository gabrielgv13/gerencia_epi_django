# views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.db import IntegrityError # Removido, pois o form agora cuida disso
from django.contrib.auth.decorators import login_required
from .models import Colaborador # <-- Importe o modelo
from .forms import ColaboradorForm # <-- Importe o novo formulário

# Importe seus novos formulários
from . import forms

def login_view(request):
    if request.user.is_authenticated:
        return redirect('app_dashboard')
    
    error_message = None

    if request.method == 'POST':
        # 1. Crie uma instância do formulário com os dados POST
        form = forms.LoginForm(request.POST)
        
        # 2. Verifique se o formulário é válido (campos preenchidos, email tem formato de email)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd.get('email')
            password = cd.get('password')

            # Sua lógica de autenticação existente
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
        # Se o formulário não for válido (ex: email mal formatado), 
        # o 'form' será passado ao template com os erros.
        # (Mas mantemos error_message para erros de *autenticação*)

    else:
        # 3. Se for GET, crie um formulário vazio
        form = forms.LoginForm()

    context = {'form': form, 'error': error_message}
    return render(request, "login.html", context)


def login_create(request):
    if request.user.is_authenticated:
        return redirect('app_dashboard')

    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        
        if form.is_valid():
            # 1. Os dados estão validados! (Email é email, senhas batem, email não existe)
            cd = form.cleaned_data
            email = cd.get('email')
            password = cd.get('password')

            try:
                # Usamos username=email por padrão, como na sua view original
                user = User.objects.create_user(username=email, email=email, password=password)
                
                user_auth = authenticate(request, username=email, password=password)
                if user_auth is not None:
                    auth_login(request, user_auth)
                    return redirect('app_dashboard')
                else:
                    # Este erro é improvável, mas é bom ter
                    form.add_error(None, "Erro ao autenticar após a criação.")

            except Exception as e:
                # Erro genérico
                form.add_error(None, f"Ocorreu um erro inesperado: {e}")

    else:
        form = forms.RegistrationForm()

    # 2. Note que não precisamos mais de 'error_message'. 
    # O próprio 'form' carrega todos os erros.
    context = {'form': form}
    return render(request, 'login_create.html', context)

# ... (suas outras views 'app_*' permanecem iguais) ...
@login_required
def app_dashboard(request):
    return render(request, 'app_ui_dashboard.html')

@login_required
def app_users(request):
    """
    READ (List): Mostra todos os colaboradores em uma tabela.
    """
    colaboradores_list = Colaborador.objects.all().order_by('nome') # Pega todos, ordena por nome
    context = {
        'colaboradores': colaboradores_list
    }
    return render(request, 'app_ui_users.html', context) #

@login_required
def app_users_create(request):
    """
    CREATE: Adiciona um novo colaborador.
    """
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save() # Salva o novo colaborador no banco
            return redirect('app_users') # Redireciona para a lista
    else:
        form = ColaboradorForm() # Cria um formulário vazio

    context = {
        'form': form,
        'page_title': 'Cadastrar Novo Colaborador' # Título para o template
    }
    # Vamos reutilizar um template de formulário
    return render(request, 'app_ui_users_form.html', context)

@login_required
def app_users_edit(request, pk):
    """
    UPDATE: Edita um colaborador existente.
    'pk' é a Primary Key (ID) do colaborador vindo da URL.
    """
    colaborador = get_object_or_404(Colaborador, pk=pk) # Pega o colaborador ou retorna Erro 404

    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador) # Carrega o form com dados existentes
        if form.is_valid():
            form.save() # Salva as mudanças
            return redirect('app_users')
    else:
        form = ColaboradorForm(instance=colaborador) # Abre o form preenchido com dados atuais

    context = {
        'form': form,
        'page_title': f'Editar Colaborador: {colaborador.nome}' # Título para o template
    }
    return render(request, 'app_ui_users_form.html', context) # Reutiliza o mesmo template

@login_required
def app_users_delete(request, pk):
    """
    DELETE: Exclui um colaborador (com página de confirmação).
    """
    colaborador = get_object_or_404(Colaborador, pk=pk)

    if request.method == 'POST':
        colaborador.delete() # Exclui o colaborador
        return redirect('app_users')

    # Se for GET, mostra a página de confirmação
    context = {
        'colaborador': colaborador
    }
    return render(request, 'app_ui_users_delete_confirm.html', context)

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