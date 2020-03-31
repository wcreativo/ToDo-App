from django.db import models

# Create your models here.

class ToDoList(models.Model):

    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Task(models.Model):

    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    list_Task = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

