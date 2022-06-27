from django.urls import path

from . import views

urlpatterns = [    
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
    path('project/<str:pk>/<str:another_param>', views.project_test, name='project_test'),

    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>', views.updateProject, name="update-project"),
    path('delete-project/<str:pk>', views.deleteProject, name="delete-project"),
]