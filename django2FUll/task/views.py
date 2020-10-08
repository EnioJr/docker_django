from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
import datetime   # Usado no dashboard

from .models import Task
from .forms import TaskForm


@login_required
# usado pela biblioteca  (django.contrib.auth.decorators)
#  Nao sera acessivel se o usuario nao estiver registrado
def taskList(request):

    # componente de busca
    search = request.GET.get('search')
    # componente de filtro
    filter = request.GET.get('filter')

    # Variaveis pro Dashboard
    tasksDoneRecently = Task.objects.filter(
        done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing', user=request.user).count()

    if search:

        tasks = Task.objects.filter(title__icontains=search, user=request.user)

    elif filter:

        tasks = Task.objects.filter(done=filter, user=request.user)

    else:
        # Pega todas as task do banco de dados, ordenado pela data de criaçao
        tasks_list = Task.objects.all().order_by(
            '-created_at').filter(user=request.user)

        # Paginçao das tasks
        # O numero a esquerda o Paginator(,0), defina o numero de task q ira ter na pagina
        paginator = Paginator(tasks_list, 3)
        # pega a pagina que ira mostrar
        page = request.GET.get('page')
        # tasks ira exibir a pagina deseja de page
        tasks = paginator.get_page(page)

    return render(request, 'task/list.html', {'tasks': tasks, 'tasksrecently': tasksDoneRecently, 'tasksdone': tasksDone, 'tasksdoing': tasksDoing})


@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task/task.html', {'task': task})


@login_required
def newTask(request):
    # if que verifica se ha uma request de POST
    if request.method == 'POST':
        form = TaskForm(request.POST)

        # Verifica se o formulario e valido
        if form.is_valid():
            # Para o save com o comit, para inserir no campo <done> a string 'doing', e no final salva a task
            task = form.save(commit=False)
            task.done = 'doing'
            # adiciona o id da task para o usuario q esta criando ele
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'task/addtask.html', {'form': form})


@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    # instance deixa o formulario pre-populado para poder editar
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        # pega oque vem do post (ou seja da ediçao) , e coloca a instance para saber qual task esta sendo alterado
        form = TaskForm(request.POST, instance=task)

        if(form.is_valid()):
            task.save()
            return redirect('/')
        # Se hover erros de validaçao de ediçao no formulario,  volta para tela principal
        else:
            return render(request, 'task/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'task/edittask.html', {'form': form, 'task': task})


@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deleta com sucesso.')

    return redirect('/')


@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)

    if(task.done == 'doing'):
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()
    return redirect('/')


def Hey(request):
    return HttpResponse('Hello World!')


def yourName(request, name):
    return render(request, 'task/yourname.html', {'name': name})
