from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, 
    RetrieveUpdateAPIView, RetrieveDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
'''
class ArticleListApiView(ListAPIView):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleCreateAPIView(CreateAPIView):
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

class AMixin:
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

class ArticleRetrieveAPIView(AMixin, RetrieveAPIView):
    pass

class ArticleRetrieveUpdateAPIView(AMixin, RetrieveUpdateAPIView):
    pass

class ArticleRetrieveDestroyAPIView(AMixin, RetrieveDestroyAPIView):
    pass    
'''