from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from to_do_list.forms import TodoForm
from to_do_list.models import Todo


@ login_required()
def todo_list(request):
    todos = Todo.objects.filter(user=request.user).order_by('created_at')

    q = request.GET.get('q')
    if q:
        todos = todos.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q)
        )

    paginator = Paginator(todos, 10)
    page = request.GET.get('page')
    page_object = paginator.get_page(page)

    context = {
        'page_object':page_object,
    }

    return render(request, 'todo_list.html',context)


@ login_required()
def todo_info(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)

    context = {
        'todo':todo.__dict__,
    }
    return render(request, 'todo_info.html',context)


@ login_required()
def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        return redirect(reverse('todo_info', kwargs={'pk':todo.pk}))

    context = {
        'form':form,
    }
    return render(request,'todo_create.html',context)


@ login_required()
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        todo = form.save()
        return redirect(reverse('todo_info', kwargs={'pk':todo.pk}))

    context = {
        'form':form,
    }
    return render(request, 'todo_update.html',context)


@ login_required()
@ require_http_methods(['POST'])
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()

    return redirect(reverse('todo_list'))
