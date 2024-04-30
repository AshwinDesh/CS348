from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path("", views.report_view, name='report_form'),  # Render the report form
    path('report/', views.report_view, name='report_view'),
    path('change_recipes/', views.change_recipes, name='change_recipes'),
    path('filter_sort/', views.filter_sort, name='filter_sort'),
]