# models.py
from django.db import models

PLATFORM_CHOICES = [
    ('Facebook', 'Facebook'),
    ('Google', 'Google'),
    ('TikTok', 'TikTok'),
    ('LinkedIn', 'LinkedIn'),
    ('YouTube', 'YouTube'),
    ('Analytics', 'Analytics'),
    ('Other', 'Other'),
]

# models.py
class ProjectPortfolio(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)  # 👈 YOU will write this manually
    description = models.CharField(max_length=255, blank=True)
    bg = models.CharField(max_length=100, default="from-blue-50 to-indigo-100")
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES, blank=True)
    details = models.TextField()
    hero_image = models.ImageField(upload_to='projects/portfolio/hero/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class PortfolioImage(models.Model):
    project = models.ForeignKey(
        ProjectPortfolio,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='projects/portfolio/gallery/')

    def __str__(self):
        return f"Image for {self.project.title}"

    
# models.py
class ProjectGallery(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)  # 👈 Manual slug here too
    description = models.CharField(max_length=255, blank=True)
    bg = models.CharField(max_length=100, default="from-blue-50 to-indigo-100")
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES, blank=True)
    details = models.TextField()
    hero_image = models.ImageField(upload_to='projects/gallery/hero/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    project = models.ForeignKey(ProjectGallery, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/gallery/images/')

    def __str__(self):
        return f"Image for {self.project.title}"


class Stat(models.Model):
    title = models.CharField(max_length=100)  # e.g., "Experience"
    value = models.CharField(max_length=50)   # e.g., "3yr+"
    color_bg = models.CharField(max_length=50, default="bg-purple-100")
    color_text = models.CharField(max_length=50, default="text-purple-600")

    def __str__(self):
        return f"{self.title}: {self.value}"
    
class Service(models.Model):
    title = models.CharField(max_length=255)
    gradient = models.CharField(max_length=100)  # ex: "from-purple-600 to-pink-500"
    icon = models.CharField(max_length=50)       # ex: "Megaphone"
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class ServiceItem(models.Model):
    service = models.ForeignKey(Service, related_name="items", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

