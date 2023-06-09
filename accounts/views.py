from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.template.defaultfilters import slugify

from salas.models import Sala

from accounts.validations import (
	empty_field, 
	registered_account, 
	different_passwords
)


def signup(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        error_count = 0
        if empty_field(nome):
            messages.error(request, 'Campo nome é obrigratório!')
            error_count += 1
        if empty_field(email):
            messages.error(request, 'Campo email é obrigratório!')
            error_count += 1
        if registered_account(nome, email):
            messages.error(request, 'Usuário já é cadastrado!')
            error_count += 1
        if empty_field(password):
            messages.error(request, 'Campo senha é obrigratório!')
            error_count += 1
        if different_passwords(password, password_confirmation):
            messages.error(request, 'As senhas devem ser iguais!')
            error_count += 1
        if error_count > 0:
            return redirect('accounts.signup')
        
        user = User.objects.create_user(username=nome, email=email, password=password, is_staff=True)
        user.save()
        messages.success(request, f"Usuário {user.username} cadastrado com sucesso!")

        return redirect('login')
    
    return render(request, 'accounts/signup.html')


def login(request):
    template_name = 'accounts/login.html'
    if request.method == 'POST':
        email    = request.POST['email']
        password = request.POST['password']
        
        if empty_field(email) or empty_field(password):
            messages.error(request, 'Todos os campos são obrigratórios!')
            return redirect('login')
    
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request=request, username=nome, password=password)
            
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                
                return redirect('dashboard')
        
    return render(request, template_name)


def dashboard(request):
    template_name = 'accounts/dashboard.html'
    if not request.user.is_authenticated:
        messages.error(request, 'Realize login para acessar a página \'Minhas Salas\'!')
        return redirect('login')
    
    salas = Sala.objects.filter(autor=request.user.id).order_by('criado_em')

    dados = {'salas': salas}
    
    return render(request, template_name, dados)


def logout(request):
    auth.logout(request)
    print('logout realizado')
    return redirect('index')
