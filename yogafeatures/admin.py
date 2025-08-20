from django.contrib import admin
from .models import Exercise, YogaPlan, YogaCourse

# Register your models here.

@admin.register(YogaPlan)
class YogaPlanAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = []
    search_fields = ('title',)

@admin.register(YogaCourse)
class YogaCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'plan', 'order')
    list_filter = ('plan',)
    search_fields = ('title', 'plan__title')
    ordering = ('plan', 'order')

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'minutes', 'kcal')
    list_filter = ('course',)
    search_fields = ('title', 'course__title')

