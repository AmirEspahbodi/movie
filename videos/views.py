from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import VideoListSerializer, VideoDetailsSerializer
from .models import Video
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class VideoListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = VideoListSerializer
    def get_queryset(self):
        return Video.objects.all()


class VideoRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoDetailsSerializer
    def get_queryset(self):
        return Video.objects.all()


class VideoCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoDetailsSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author = request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class VideoUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoDetailsSerializer
    def get_queryset(self):
        return Video.objects.all()
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        if request.user != instance.author:
            return Response(status=403)
        
        try:
            old_file_path = instance.file.path
            print(f"old file path {old_file_path}")
        except BaseException:
            old_file_path = None
            
        if old_file_path:
            import os
            if os.path.exists(old_file_path):
                os.remove(old_file_path)
        
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class VideoDestroyAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoDetailsSerializer
    
    def perform_destroy(self, instance):
        import os
        try:
            file_path = instance.file.path
        except BaseException:
            file_path = None
        if file_path:
            os.remove(file_path)
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if request.user != instance.author:
            return Response(status=403)
        
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        return Video.objects.all()


