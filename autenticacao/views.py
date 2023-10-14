from django.shortcuts import render

def login(request):
    return render(request, template_name='login.html')

def registro(request):
    return render(request, template_name='registro.html')