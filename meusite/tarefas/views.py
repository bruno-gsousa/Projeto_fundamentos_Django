from django.shortcuts import render,redirect,get_object_or_404
from .forms import TarefaForm
from .models import TarefaModel
# Create your views here.

def tarefas_home(request):
    contexto = {
        'nome': 'Bruno',
        "tarefas": TarefaModel.objects.all()
    }
    return render(request, 'pagetarefas/home.html', contexto)

def tarefas_adicionar(request):
    if request.method == "POST":
        formulario = TarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")
    contexto={
        "form": TarefaForm()
    }
    
    return render(request, 'pagetarefas/adicionar.html',contexto)

def tarefas_remover(request,id):
    tarefa = get_object_or_404(TarefaModel,id=id)
    tarefa.delete()
    return redirect("tarefas:home")

def tarefas_editar(request,id):
    tarefa = get_object_or_404(TarefaModel,id=id)
    if request.method == "POST":
        formulario = TarefaForm(request.POST,instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")
    else:
        contexto={
            "form":TarefaForm(instance=tarefa)
        }
    
    return render(request, "pagetarefas/editar.html",contexto)
