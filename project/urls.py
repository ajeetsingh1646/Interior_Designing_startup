from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.all_project, name='all_project'),
    #path('project', views.all_project, name='all_project'),
    path('<int:project_id>', views.project_detail, name='project_detail')
]

