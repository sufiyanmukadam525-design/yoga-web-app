from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class YogaPlan(models.Model):
    PLAN_TYPE_CHOICES = [
        ('Free', 'Free'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    plan_type = models.CharField(max_length=20, choices=PLAN_TYPE_CHOICES, default='Free')
    image = models.ImageField(upload_to="exercises/", blank=True, null=True)
    def __str__(self):
        return self.title


class YogaCourse(models.Model):
    plan = models.ForeignKey(YogaPlan, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=200)
    duration_minutes = models.PositiveIntegerField(default=10)
    order = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="exercises/", blank=True, null=True)
    class Meta:
        ordering = ['order']  # Optional: default ordering in queries

    def __str__(self):
        return f"{self.plan.title} - {self.title}"


class Exercise(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="exercises/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    minutes = models.PositiveIntegerField(default=10)  
    kcal = models.PositiveIntegerField(default=30)     
    course = models.ForeignKey('YogaCourse', related_name="exercises", on_delete=models.CASCADE)

    def __str__(self):
        return self.title



