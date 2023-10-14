from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def logar(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        usuario = form.cleaned_data.get('username')
        senha = form.cleaned_data.get('password')

        user = authenticate(username = usuario, password = senha)

        if user is not None:
            login(request, user)
            messages.info(request, f'Seja bem vindo, {user.username}')
            return redirect('index')
        else:
            #messages.error(request, message='Usuário ou senha inválido.')
            messages.info(request, message='Usuário ou senha inválido.')
            #return render(request, template_name='login.html', context={'login_form':form})
    else:
        messages.info(request, message='Usuário ou senha inválido.')
    form = AuthenticationForm()    
    return render(request, template_name='login.html', context={'login_form':form})

def registro(request):
    return render(request, template_name='registro.html')