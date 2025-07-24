from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from products import views  # Импортируем views из приложения products

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем остальные маршруты products, если есть
    path('', include('products.urls')),
    path("news/", include("news.urls")),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
