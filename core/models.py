from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 50)
    description = models.CharField(max_length = 255)
    author = models.CharField(max_length = 50)
    published_date = models.DateField()
    content = models.TextField()
    image = models.CharField(max_length = 255)
    def __str__(self):
        return self.title


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"Comment: {self.content}"
