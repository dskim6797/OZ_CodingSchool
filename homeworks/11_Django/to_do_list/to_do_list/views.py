from django.shortcuts import render, get_object_or_404
from to_do_list.models import Todo

def todo_list(request):
    todo_id_title = Todo.objects.all().values_list('id', 'title')
    todos = [{'id': todo[0], 'title': todo[1]} for todo in todo_id_title]

    context = {
        'todos':todos
    }

    return render(request, 'todo_list.html',context)


def todo_info(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    context = {
        'todo':todo
    }

    return render(request, 'todo_info.html',context)
