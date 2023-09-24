from django.urls import path
from .views import LessonStatusList, LessonStatusListByProduct, ProductStatisticsList


urlpatterns = [
    path('lesson-status/', LessonStatusList.as_view(), name='lesson-status-list'),
    path('lesson-status/product/<int:product_id>/', LessonStatusListByProduct.as_view(), name='lesson-status-list-by-product'),
    path('product-statistics/', ProductStatisticsList.as_view(), name='product-statistics-list'),
]
