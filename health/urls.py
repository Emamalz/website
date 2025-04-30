from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('',          views.login_view,  name='login'),
    path('select_team/', views.select_team, name='select_team'),
    path('register/', RegisterView.as_view(), name='register'),
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
    

    path('feedback/', views.feedback, name='feedback'),
    path('trends/', views.trends, name='trends'),
    path('registration/logout/', views.logout_view, name='logout'),

    
    
    
    path('factors/', views.factors_view, name='factors'),
    path('factors/', views.factors, name='factors'),
    path('trends/', views.trends_view, name='trends'),


]
