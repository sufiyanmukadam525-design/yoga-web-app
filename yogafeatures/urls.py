from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.plans_list, name='plans'),
    path('plans/<int:plan_id>/', views.plan_detail, name='plan_detail'),
    path('courses/<int:course_id>/exercises/', views.exercise_list, name='exercise_list'),
    path('exercises/<int:exercise_id>/', views.exercise_detail, name='exercise_detail'),
]
