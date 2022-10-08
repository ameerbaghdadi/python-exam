from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns=[
    path('', views.dashboard),
    path('new/tree/', views.plant_a_tree),
    path('add_plant/', views.add_plant),
    path('user/account/', views.show_my_tree),
    path('edit/<int:id>/', views.edit_my_tree),
    path('update/<int:id>/', views.update_tree),
    path('delete/<int:id>/', views.delete_tree),
    path('show/<int:id>/', views.details),
    path('visited_by/<int:id>/', views.visited_by)
]