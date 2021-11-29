from rest_framework import serializers
from applications.post.models import Category, Post
from applications.review.serializers import ReviewSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title',)

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'category', 'title', 'content')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        question = Post.objects.create(**validated_data)
        return question

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.title
        representation['author'] = instance.author.email
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) > 0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        return representation


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) > 0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        representation['reviews'] = ReviewSerializer(instance.review.filter(post=instance.id), many=True).data
        return representation