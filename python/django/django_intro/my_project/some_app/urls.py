from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('another_route', views.another_method),
    path('redirected_route', views.redirected_method),
    path('bears', views.one_method),                        # would only match localhost:8000/bears
    path('bears/<int:my_val>', views.another_method),       # would match localhost:8000/bears/23
    path('bears/<str:name>/poke', views.yet_another),       # would match localhost:8000/bears/pooh/poke
    path('<int:id>/<str:color>', views.one_more),           # would match localhost:8000/17/brown
]
