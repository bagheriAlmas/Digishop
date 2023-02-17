from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from digiShop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('',include('users.urls'))
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
