from rest_framework.serializers import ModelSerializer

from .models import Users, Food, Message, Comment, Rating


class UserSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'


class FoodSerializer(ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'