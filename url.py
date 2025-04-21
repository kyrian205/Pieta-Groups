from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Gallery page
    path('gallery/', views.gallery, name='gallery'),

    # News page
    path('news/', views.news, name='news'),

    # Complaints page
    path('complaint/', views.complaint_view, name='complaint'),

    # Admission page
    path('admission/', views.admission_view, name='admission'),

    # Result Checker page
    path('result-checker/', views.result_checker, name='result_checker'),

    # Admin page
    path('admin/', views.admin_dashboard, name='admin'),
]