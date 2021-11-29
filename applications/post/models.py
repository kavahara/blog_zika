from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# class Category(models.Model):
#     title = models.CharField(max_length=50)

#     def __str__(self):
#         return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post')
    content = models.TextField()
    image = models.ImageField(upload_to='', blank=True)
    public_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'post """{self.title}""" from """{self.author}""" AUTHOR'

class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorite', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='favorite', on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.favorite