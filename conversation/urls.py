from django.urls import path, include
from . import views 

app_name = 'conversation'

urlpatterns = [
  path('', views.inbox, name='inbox'),
  path('<int:pk>/', views.detail, name='detail'),
  # path('<int:item_pk>/', views.detail, name='detail'),
  # path('<int:item_pk>/', views.new_conversation, name='new'),
  # path('new/<int:pk>/', views.new_conversation, name='new'),
  path('new/<int:item_pk>/', views.new_conversation, name='new'),
]
