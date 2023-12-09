from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth import get_user_model

class Post(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=100)
    published_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    body = models.TextField()
    image_url = models.URLField(null=True,blank=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='posts')
    # slug = models.SlugField(null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_at']

    # def save(self,*args,**kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})
    

class CategoryChoices(models.TextChoices):
    GENERAL = 'general','General'
    EDUCATION = 'education','Education'
    SPORTS = 'sports','Sports'

class Category(models.Model):
    name = models.CharField(max_length=100,choices=CategoryChoices.choices)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)