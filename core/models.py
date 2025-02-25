from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Tea(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='tea_images/', null=True, blank=True)  # Add image field for tea
    created_at = models.DateTimeField(default=datetime.datetime.now)  # Set default to current time

    def __str__(self):
        return self.name


# Tea Garden Model
class TeaGarden(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='tea_garden_images/', null=True, blank=True)  # Add image field for tea garden
    created_at = models.DateTimeField(default=datetime.datetime.now)  # Set default to current time

    def __str__(self):
        return self.name


class TeaHistory(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now)  # Set default to current time
    image = models.ImageField(upload_to='tea_history_images/', null=True, blank=True)  # Add image field for tea history

    def __str__(self):
        return self.title


# Message Model (Tree Hole)
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_message = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f"Message by {self.user.email if self.user else 'Anonymous'}"


# News Model
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news_article = models.ForeignKey(News, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'news_article')  # Prevents multiple likes from the same user

    def __str__(self):
        return f"{self.user.username} liked {self.news_article.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news_article = models.ForeignKey(News, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.news_article.title}"
