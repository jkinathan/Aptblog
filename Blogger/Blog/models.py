from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    context_object_name = "post_list"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    