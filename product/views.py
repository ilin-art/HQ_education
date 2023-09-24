from rest_framework import generics, permissions
from .models import LessonStatus, Product
from .serializers import LessonStatusSerializer, ProductStatisticsSerializer


class LessonStatusList(generics.ListAPIView):
    serializer_class = LessonStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return LessonStatus.objects.filter(user=user)


class LessonStatusListByProduct(generics.ListAPIView):
    serializer_class = LessonStatusSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        return LessonStatus.objects.filter(user=user, lesson__products=product_id)


class ProductStatisticsList(generics.ListAPIView):
    serializer_class = ProductStatisticsSerializer
    queryset = Product.objects.all()
