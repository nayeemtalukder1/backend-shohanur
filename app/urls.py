from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PortfolioListAPI, PortfolioDetailAPI,
    GalleryListAPI, GalleryDetailAPI,
    StatsAPI, ServiceListAPI
)


urlpatterns = [
  path('portfolio/', PortfolioListAPI.as_view()),
    path('portfolio/<slug:slug>/', PortfolioDetailAPI.as_view()),

    path('gallery/', GalleryListAPI.as_view()),
    path('gallery/<slug:slug>/', GalleryDetailAPI.as_view()),
    path("stats/", StatsAPI.as_view(), name="stats-list"),
    path("services/", ServiceListAPI.as_view(), name="services-list")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

