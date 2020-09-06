from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:main_id>/', views.post, name='post'),
    path('new/',views.new,  name='new'),
    path('create/',views.create, name='create'),
    path('edit/<int:main_id>/',views.edit, name='edit'),
    path('update/<int:main_id>/',views.update, name='update'),
    path('post/<int:main_id>/delete',views.delete, name='delete'),
    path('delete/<int:main_id>/', views.delete, name='delete'),
]