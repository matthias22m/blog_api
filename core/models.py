from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(unique=True,max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk': self.pk})

class Comment(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"'{self.author}' to '{self.post}' "


class LikedItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, default=1)
    
    class Meta:
        unique_together = ('user','post')
    
    def __str__(self):
        return f"'{self.user}' liked '{self.post.title}'"
