from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from applications.post.models import Post

User = get_user_model()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='review')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='review')
    review = models.TextField()
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return f'REVIEW on """{self.post.title}""" post'


class Like(models.Model):
    user = models.ForeignKey(User, related_name='like', on_delete=models.CASCADE)
    review = models.ForeignKey(Review, related_name='like', on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.like

