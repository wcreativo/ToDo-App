from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import ToDoList, Task


# Create your views here.

class ToDoListView(ListView):

    context_object_name = 'name'
    template_name = 'core/todolist_list.html'
    queryset = ToDoList.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ToDoListView, self).get_context_data(**kwargs)
        context['Tasks'] = Task.objects.all()
        context['ToDoLists'] = self.queryset
        return context