from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feedback/', views.feedback, name='feedback'),
    path('trends/', views.trends, name='trends'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    
    path('deliver/', views.deliver, name='deliver'),
    path('details/', views.details, name='details'),
    path('detailsforadmins/', views.detailsforadmins, name='detailsforadmins'),
    path('easeofrelease/', views.easeofrelease, name='easeofrelease'),
    path('factors/', views.factors, name='factors'),
    path('fun/', views.fun, name='fun'),
    path('healthbasecoder/', views.healthbasecoder, name='healthbasecoder'),
    path('intro/', views.intro, name='intro'),
    path('learning/', views.learning, name='learning'),
    path('mission/', views.mission, name='mission'),
    path('pawnsorplayers/', views.pawnsorplayers, name='pawnsorplayers'),
    path('speed/', views.speed, name='speed'),
    path('suitableprocess/', views.suitableprocess, name='suitableprocess'),
    path('support/', views.support, name='support'),
    
]