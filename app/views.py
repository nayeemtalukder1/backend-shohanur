from rest_framework import generics
from .models import ProjectPortfolio
from .serializers import ProjectPortfolioSerializer

from .models import ProjectGallery
from .serializers import ProjectGallerySerializer
from .models import Stat
from .serializers import StatSerializer

from .models import Service
from .serializers import ServiceSerializer





class PortfolioListAPI(generics.ListAPIView):
    queryset = ProjectPortfolio.objects.all().order_by('-created_at')
    serializer_class = ProjectPortfolioSerializer


class PortfolioDetailAPI(generics.RetrieveAPIView):
    queryset = ProjectPortfolio.objects.all()
    serializer_class = ProjectPortfolioSerializer
    lookup_field = 'slug'


class GalleryListAPI(generics.ListAPIView):
    queryset = ProjectGallery.objects.all().order_by('-created_at')
    serializer_class = ProjectGallerySerializer



class GalleryDetailAPI(generics.RetrieveAPIView):
    queryset = ProjectGallery.objects.all()
    serializer_class = ProjectGallerySerializer
    lookup_field = 'slug'

class StatsAPI(generics.ListAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

class ServiceListAPI(generics.ListAPIView):
    queryset = Service.objects.all().order_by("order")
    serializer_class = ServiceSerializer
