from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post,Comment

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class PostSerializer(serializers.ModelSerializer):

    owner=serializers.StringRelatedField(read_only=True)
    greetings=serializers.SerializerMethodField()
    comment_count=serializers.SerializerMethodField()

    class Meta:
        model=Post
        fields="__all__"

        read_only_fields=["id","created_at","owner"]

    def get_greetings(self,obj):
        return "Good Morning"
    def get_comment_count(self,obj):
        return obj.comments.count()

class CommentSerializer(serializers.ModelSerializer):
    owner=serializers.StringRelatedField(read_only=True)
    post_object=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Comment
        fields="__all__"

        read_only_fields=["id","owner","post_object","created_at"]