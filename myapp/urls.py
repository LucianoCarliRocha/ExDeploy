from django.urls import path
from .views import get_items, create_item

urlpatterns = [
    path('items/', get_items, name='get_items'),
    path('items/create/', create_item, name='create_item'),
]

from django.conf import settings 
from django.conf.urls.static import static
if settings.DEBUG:
   urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)