from rest_framework.serializers import ModelSerializer
from videos.models import Video


class VideoDetailsSerializer(ModelSerializer):
    class Meta:
        fields = ('name', 'file',)
        model = Video
        
class VideoListSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Video