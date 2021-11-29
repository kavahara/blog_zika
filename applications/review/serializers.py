from rest_framework import serializers

from applications.review.models import Review, Like


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


# class WhoLikeSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Like
#         fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user_id'] = request.user.id
        review = Review.objects.create(**validated_data)
        return review

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation.pop('id')
        representation['user'] = f'{instance.user}'
        representation['like'] = instance.like.filter(like=True).count()
        return representation