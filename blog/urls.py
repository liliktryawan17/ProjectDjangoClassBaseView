from django.contrib import admin
from django.urls import path, include

from .views import HomeView

urlpatterns = [
    path('artikel/', include('artikel.urls', namespace='artikel')),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home')
]
