from django.urls import path
from . import views

urlpatterns = [
    path('', views.iam, name='iam'),
    path('country', views.country, name='country'),
    path('language', views.language, name='language'),
    path('country/<id>', views.country_max),
    path('language/<id>', views.language_max)
]
