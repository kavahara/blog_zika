from rest_framework import serializers
from applications.posts.models import Posts, PostsImage #LikePosts,
from applications.review.serializers import ReviewSerializer



class PostsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostsImage
        fields = ('image',)

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
                print(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) > 0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        representation['images'] = PostsImageSerializer(PostsImage.objects.filter(posts=instance.id), many=True,
                                                        context=self.context).data
        return representation


class PostsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

    def to_representation(self, instance):

        representation = super().to_representation(instance)
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) > 0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        representation['images'] = PostsImageSerializer(PostsImage.objects.filter(posts=instance.id), many=True, context=self.context).data
        representation['reviews'] = ReviewSerilizer(instance.review.filter(product=instance.id), many=True).data


# class LikeSerializer(serializers.Modelserializer):
#     class Meta:
#         model = LikePosts
#         fields = '__all__'
