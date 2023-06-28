from django.urls import path
from . import views

app_name = 'survey'

urlpatterns = [
    path('', views.index, name='my_index'),
    path('result', views.result, name='my_result')
]