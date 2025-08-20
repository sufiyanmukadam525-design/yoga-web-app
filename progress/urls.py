from django.urls import path
from . import views

app_name = 'progress'

urlpatterns = [
    path('tracker/', views.progress_view, name='progress_tracker'),
    path('meditate/',views.meditate_view, name='meditate'),
    path('complete/<int:exercise_id>/', views.complete_exercise, name='complete_exercise'),
    path('stats-series/', views.stats_series, name='stats_series'),
]