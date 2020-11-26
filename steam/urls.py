from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filter', views.filter, name='filterData'),
    path('filter/reversed/<key>', views.reverse, name='reverselist')
]
