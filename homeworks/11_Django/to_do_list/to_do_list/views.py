from django.shortcuts import render, get_object_or_404
from to_do_list.models import Todolist

def todo_list(request):
    todo_table = Todolist.objects.all()
    context = {
        'todo_table':todo_table
    }

    return render(request, 'todo_list.html',context)


def todo_info(request, pk):
    todo = get_object_or_404(Todolist, pk=pk)
    context = {
        'todo':todo
    }

    return render(request, 'todo_info.html',context)
