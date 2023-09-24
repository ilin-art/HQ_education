from .models import LessonStatus

def update_lesson_status(user, lesson, view_time_seconds):
    video_duration = lesson.duration_seconds
    percentage_watched = (view_time_seconds / video_duration) * 100

    lesson_status, created = LessonStatus.objects.get_or_create(user=user, lesson=lesson)
    lesson_status.view_time_seconds = view_time_seconds
    lesson_status.percentage_watched = percentage_watched
    if percentage_watched >= 80:
        lesson_status.viewed = True
    lesson_status.save()
