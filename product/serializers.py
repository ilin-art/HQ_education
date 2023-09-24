from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import serializers
from .models import LessonStatus, Product, ProductAccess


class LessonStatusSerializer(serializers.ModelSerializer):
    last_viewed_at = serializers.DateTimeField(source='get_last_viewed_at', read_only=True)

    class Meta:
        model = LessonStatus
        fields = '__all__'


class ProductStatisticsSerializer(serializers.ModelSerializer):
    total_lessons_viewed = serializers.SerializerMethodField()
    total_time_watched = serializers.SerializerMethodField()
    total_students = serializers.SerializerMethodField()
    purchase_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'total_lessons_viewed', 'total_time_watched', 'total_students', 'purchase_percentage']

    def get_total_lessons_viewed(self, obj):
        '''
        Общее количество просмотренных уроков для данного продукта
        '''
        return LessonStatus.objects.filter(lesson__products=obj).filter(viewed=True).count()

    def get_total_time_watched(self, obj):
        '''
        Общее время просмотра для данного продукта
        '''
        total_time = LessonStatus.objects.filter(lesson__products=obj).aggregate(Sum('view_time_seconds'))
        return total_time['view_time_seconds__sum'] if total_time['view_time_seconds__sum'] else 0

    def get_total_students(self, obj):
        '''
        Общее количество учеников для данного продукта
        '''
        return LessonStatus.objects.filter(lesson__products=obj).select_related('user').values('user').distinct().count()

    def get_purchase_percentage(self, obj):
        '''
        Процент приобретения продукта для данного продукта
        '''
        total_users = User.objects.all().count()
        product_accesses = ProductAccess.objects.filter(product=obj).count()
        return (product_accesses / total_users) * 100 if total_users > 0 else 0
