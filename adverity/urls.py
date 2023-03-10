from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from adverity import views

urlpatterns = [
    path('', views.show_collections, name="index"),
    path('fetch/collection', views.add_collection),
    path('view/collection/<str:_id>', views.view_collection),
    path('view/collection/<str:_id>/<int:max_rows>', views.view_collection),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
