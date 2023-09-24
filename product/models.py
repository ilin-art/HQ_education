from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    video_link = models.URLField()
    duration_seconds = models.PositiveIntegerField()
    products = models.ManyToManyField('Product', related_name='lessons')

    def __str__(self):
        return self.name


class LessonStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_viewings')
    viewed = models.BooleanField(default=False)
    view_time_seconds = models.PositiveIntegerField(default=0)
    percentage_watched = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        video_duration = self.lesson.duration_seconds
        percentage_watched = (self.view_time_seconds / video_duration) * 100

        self.percentage_watched = percentage_watched
        if percentage_watched >= 80:
            self.viewed = True

        super().save(*args, **kwargs)

    def get_last_viewed_at(self):
        try:
            last_viewing = LessonViewing.objects.filter(lesson_status=self).latest('timestamp')
            return last_viewing.timestamp
        except LessonViewing.DoesNotExist:
            return None

    def __str__(self):
        return f"{self.user.username} - {self.lesson.name}"


class LessonViewing(models.Model):
    lesson_status = models.ForeignKey(LessonStatus, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lesson_status.user.username} - {self.lesson_status.lesson.name} - {self.timestamp}"
