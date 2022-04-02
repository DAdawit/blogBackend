from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'date']
    # title = serializers.CharField(max_length=100)
    # description = serializers.CharField(max_length=2000)
    # date = serializers.DateTimeField()

    # def create(self, validated_data):
    #     return Post.objects.create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('decription', instance.description)
    #     instance.date = validated_data.get('date', instance.date)
    #     instance.save()
    #     return instance
