
from django.urls import path
from . import views
urlpatterns = [
    path("task_cetagory/",views.cetagory,name='cetagory')
]
