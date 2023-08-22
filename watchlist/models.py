from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# This is a Streaming Platform Model
class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=500)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name

# This is a show model that holds the names and about of the show


class Show(models.Model):
    show_title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    # platform = models.ForeignKey(
    #     StreamPlatform, on_delete=models.CASCADE, related_name="showlist") #platform
    platform = models.ForeignKey(
        StreamPlatform, on_delete=models.CASCADE, related_name="showname")  # platform
    active = models.BooleanField(default=True)
    avg_ratings = models.FloatField(default=0)
    number_ratings = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " | " + self.show_title


class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_description = models.TextField(
        max_length=500, null=True, blank=True)
    # showlist = models.ForeignKey(
    #     Show, on_delete=models.CASCADE, related_name='reviews')
    showname = models.ForeignKey(
        Show, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.showname.show_title + " || " + str(self.reviewer)
