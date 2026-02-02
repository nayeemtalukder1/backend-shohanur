from rest_framework import serializers
from django.conf import settings
from .models import (
    ProjectPortfolio, PortfolioImage,
    ProjectGallery, GalleryImage,
    Stat,
    Service, ServiceItem
)


# ---------------- Portfolio ----------------
class PortfolioImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = PortfolioImage
        fields = ["image"]

    def get_image(self, obj):
        if obj.image:
            return f"{settings.MEDIA_URL}{obj.image.name}"
        return None


class ProjectPortfolioSerializer(serializers.ModelSerializer):
    images = PortfolioImageSerializer(many=True, read_only=True)
    heroImage = serializers.SerializerMethodField()

    class Meta:
        model = ProjectPortfolio
        fields = [
            "id", "slug", "title", "description", "bg",
            "platform", "details", "heroImage", "images", "created_at"
        ]

    def get_heroImage(self, obj):
        if obj.hero_image:
            return f"{settings.MEDIA_URL}{obj.hero_image.name}"
        return None


# ---------------- Gallery ----------------
class GalleryImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = GalleryImage
        fields = ["image"]

    def get_image(self, obj):
        if obj.image:
            return f"{settings.MEDIA_URL}{obj.image.name}"
        return None


class ProjectGallerySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, read_only=True)
    heroImage = serializers.SerializerMethodField()

    class Meta:
        model = ProjectGallery
        fields = [
            "id", "slug", "title", "description", "bg",
            "platform", "details", "heroImage", "images", "created_at"
        ]

    def get_heroImage(self, obj):
        if obj.hero_image:
            return f"{settings.MEDIA_URL}{obj.hero_image.name}"
        return None


# ---------------- Stats ----------------
class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ["title", "value", "color_bg", "color_text"]

class ServiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItem
        fields = ["text"]


class ServiceSerializer(serializers.ModelSerializer):
    items = ServiceItemSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ["id", "title", "gradient", "icon", "items"]
