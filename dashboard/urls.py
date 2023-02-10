# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path
from dashboard.views import index

app_name = 'dashboard'

urlpatterns = [
  path('index/', index, name='index'),
  # path('detail/<int:pk>/', detail, name='detail'),
] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
