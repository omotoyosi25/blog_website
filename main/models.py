from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Comments(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=200, verbose_name="Email Address")
    message=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Post (models.Model):
    title = models.CharField(max_length=250, verbose_name= "blog title")
    desc= models.TextField()
    article=models.TextField()
    published_date=models.DateField(auto_now_add=True)
    owner=models.ForeignKey(User, null=True, blank=True,on_delete = models.SET_NULL)
    thumbnail=models.ImageField(upload_to="thumbnail", default="example.jpg")
    category=models.ForeignKey(Category, related_name='article', on_delete=models.CASCADE, default=1)
    tags=models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title