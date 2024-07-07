
from django.urls import path
from . import views
urlpatterns = [
    path("task_form/",views.taskForm,name='taskForm'),
    path("show_task/",views.show_task,name='show_task'),
    path("edit/<int:id>",views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete_task')
]
