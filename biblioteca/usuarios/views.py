from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == 'POST':

        # Recebe os dados do formuário
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmacao_senha = request.POST['confirmacao-senha']

        #Validação dos campos
        if not nome.strip():
            messages.error(request, 'Nome não pode ficar em branco!')
            return redirect('cadastro')
        if not sobrenome.strip():
            messages.error(request, 'sobrenome não pode ficar em branco!')
            return redirect('cadastro')
        if not email.strip():
            messages.error(request, 'email não pode ficar em branco!')
            return redirect('cadastro')
        if senha != confirmacao_senha:
            messages.error(request, 'senhas diferentes. Informe as mesmas senhas, por favor')
            return redirect('cadastro')
        User.objects.create_user(first_name=nome, last_name=sobrenome, username=f'{nome} {sobrenome}',email=email,password=senha)
        return render(request, 'usuarios/login.html')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        # Recebe os dados do formulário
        email = request.POST['email']
        senha = request.POST['senha']
        # Validação dos campos
        if email == '' or senha == '':
            messages.success(request, 'E-mail e senha devem ser preenchidos')
            return redirect('login')
        # Autenticado usuário
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('index')
            else:
                messages.error(request, "Login inválido")
                return redirect('login')
        else:
            messages.error(request, "Login inválido")

    return render(request, 'usuarios/login.html')
def logout(request):
    auth.logout(request)
    messages.warning(request, 'Logout realizado')
    return redirect('index')
