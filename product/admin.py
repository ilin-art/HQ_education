from django.contrib import admin
from .models import Product, ProductAccess, Lesson, LessonStatus

admin.site.register(Product)
admin.site.register(ProductAccess)
admin.site.register(Lesson)
admin.site.register(LessonStatus)
