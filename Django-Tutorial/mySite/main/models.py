from django.db import models

# Create your models here.


class ToDoList(models.Model):
    """
    Defining the Model of our database
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        """
        String representation of our ToDoList
        """
        return self.name


class item(models.Model):
    """
    Defining another model related to the ToDoList
    """
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        """
        String representation of items in the ToDoList
        """
        return self.text
