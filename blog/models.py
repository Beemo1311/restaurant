from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=55)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Post(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'post/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    created = models.DateTimeField(auto_now_add = True)
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural= 'Posts'
    
    def __str__(self) -> str:
        return self.title



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.content

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'




