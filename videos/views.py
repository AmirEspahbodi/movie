from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from .serializer import VideoListSerializer, VideoDetailsSerializer
from .models import Video
from rest_framework.response import Response

# Create your views here.


class VideoListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = VideoListSerializer
    queryset = Video.objects.all()


class VideoRetrieveAPIView(RetrieveAPIView):
    serializer_class = VideoDetailsSerializer
    queryset = Video.objects.all()


class VideoCreateAPIView(CreateAPIView):
    serializer_class = VideoDetailsSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author = request.user)
        headers = self.get_success_headers(serializer.data)
        
        #HTTP_201_CREATED
        return Response(serializer.data, status=201, headers=headers)


class VideoUpdateAPIView(UpdateAPIView):
    serializer_class = VideoDetailsSerializer
    queryset = Video.objects.all()
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if request.user != instance.author:
            return Response(status=403)

        try:
            old_file_path = instance.file.path
            import os
            if os.path.exists(old_file_path):
                os.remove(old_file_path)
        except BaseException:
            pass
        
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class VideoDestroyAPIView(DestroyAPIView):
    serializer_class = VideoDetailsSerializer
    queryset = Video.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if request.user != instance.author:
            return Response(status=403)
        
        self.perform_destroy(instance)
        
        # HTTP_204_NO_CONTENT
        return Response(status=204)
