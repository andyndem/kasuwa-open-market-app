# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path
from item.views import detail, new, delete, edit, items

app_name = 'item'

urlpatterns = [
  path('', items, name='items'),
  path('new/', new, name='new'),
  path('<int:pk>/', detail, name='detail'),
  path('<int:pk>/delete/', delete, name='delete'),
  path('<int:pk>/edit/', edit, name='edit'),
] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
