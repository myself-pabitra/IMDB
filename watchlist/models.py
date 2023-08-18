from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Show(models.Model):
    show_title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    platform = models.ForeignKey(
        StreamPlatform, on_delete=models.CASCADE, related_name="showlist")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.show_title


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_description = models.TextField(
        max_length=500, null=True, blank=True)
    showlist = models.ForeignKey(
        Show, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating)+ " || " + self.showlist.show_title
