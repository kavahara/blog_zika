from django.db import models
# from applications.category.models import Category
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from applications.likes.models import Like


User = get_user_model()


# пост
class Posts(models.Model):
    title = models.CharField(max_length=255)
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
# category
    # image = models.ImageField(upload_to='', on_delete=models.CASCADE, related_name='image') #один из двух вариантов
    # image = models.ImageField(upload_to='', height_field=100, width_field=100)
    # когда было сделано публикация
    public_date = models.DateTimeField(auto_now_add=True)
    # когда было изменена публикация
    update_date = models.DateTimeField(auto_now=True)

    likes = GenericRelation(Like)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()


class PostsImage(models.Model):
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.posts.title


# лайки для постов
# class LikePosts(models.Model):
#     #  user = models.ForeignKey(User, related_name='like', on_delete=models.CASCADE) # если что не надо
#     posts = models.ForeignKey(Posts, related_name='like', on_delete=models.CASCADE)
#     like = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.like


