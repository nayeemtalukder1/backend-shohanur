# admin.py
from django.contrib import admin
from .models import (
    ProjectPortfolio,
    PortfolioImage,
    ProjectGallery,
    GalleryImage,
    Stat,
    ServiceItem,
    Service

)


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1


@admin.register(ProjectPortfolio)
class ProjectPortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'created_at')
    prepopulated_fields = {"slug": ("title",)}  # auto-fill but editable
    inlines = [PortfolioImageInline]

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1


@admin.register(ProjectGallery)
class ProjectGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'created_at')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [GalleryImageInline]

admin.site.register(Stat)

class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    inlines = [ServiceItemInline]

