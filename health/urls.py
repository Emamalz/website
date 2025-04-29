from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_team, name='select_team'),
    path('intro/', views.intro_page, name='intro_page'),
    path('done/', views.done, name='done'),

    # health card pages
    path('deliver/', views.deliver, name='deliver'),
    path('fun/', views.fun, name='fun'),
    path('support/', views.support, name='support'),
    path('easeofrelease/', views.ease_of_release, name='ease_of_release'),
    path('learning/', views.learning, name='learning'),
    path('mission/', views.mission, name='mission'),
    path('speed/', views.speed, name='speed'),
    path('suitableprocess/', views.suitable_process, name='suitable_process'),
    path('pawnsonplayers/', views.pawnsonplayers, name='pawnsonplayers'),
    path('healthbasecoder/', views.healthbasecoder, name='healthbasecoder'),
]
