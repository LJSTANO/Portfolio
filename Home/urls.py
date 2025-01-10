from django .urls import path
from .import views
from .views import services

urlpatterns=[
    path('',views.home,name='home'),
    path('portfolio/',views.portfolio,name='portfolio'),

    path('services/', views.services,name='services'),

    path('starter/', views.starter,name='starter'),
]

