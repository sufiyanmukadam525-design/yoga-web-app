from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class CourseProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='course_progress')
    course = models.ForeignKey('yogafeatures.YogaCourse',on_delete=models.CASCADE,related_name='progress')
    percentage_complete = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    started_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True,blank=True)

    class Meta:
        unique_together = ('user','course')

    def __str__(self):
        return f"{self.user} - {self.course} - {self.percentage_complete}%"


class ExerciseProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='exercise_progress')
    exercise = models.ForeignKey('yogafeatures.Exercise',on_delete=models.CASCADE,related_name='progress')
    course = models.ForeignKey('yogafeatures.YogaCourse',on_delete=models.CASCADE,related_name='exercise_progress')
    done = models.BooleanField(default=False)
    durations_seconds = models.PositiveIntegerField(default=0)
    calories = models.PositiveIntegerField(default=0)
    date = models.DateField(default=timezone.localdate)

    class Meta:
        unique_together = ('user','exercise','date')

    def __str__(self):
        return f"{self.user} - {self.exercise} - {self.date}  - {'done' if self.done else 'pending'}"
    

class DailyStat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='daily_stats')
    date = models.DateField(default=timezone.localdate)
    minutes = models.PositiveIntegerField(default=0)
    calories = models.PositiveIntegerField(default=0)
    workouts = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.user} - {self.date} - {self.minutes} min"