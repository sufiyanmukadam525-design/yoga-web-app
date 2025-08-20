from datetime import date, timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.apps import apps
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import CourseProgress, DailyStat, ExerciseProgress


def _today():
    try:
        return timezone.localdate()
    except Exception:
        return date.today()


def __get__model(name):
    try:
        return apps.get_model('yogafeatures', name)
    except LookupError:
        return None


@login_required
def progress_view(request):
    today = _today()

    # last 7 days stats
    start7 = today - timedelta(days=6)
    last7 = DailyStat.objects.filter(
        user=request.user,
        date__range=[start7, today]
    ).order_by('date')

    # last 30 days stats
    start30 = today - timedelta(days=29)
    last30 = DailyStat.objects.filter(
        user=request.user,
        date__range=[start30, today]
    ).order_by('date')

    # courses with progress
    course_rows = CourseProgress.objects.filter(
        user=request.user
    ).select_related('course')

    # exercises with progress
    exercise_rows = ExerciseProgress.objects.filter(
        user=request.user
    ).select_related('exercise', 'course')

    context = {
        'last7': last7,
        'last30': last30,
        'course_rows': course_rows,
        'exercise_rows': exercise_rows
    }
    return render(request, 'progress/progress_tracker.html', context)


@login_required
def stats_series(request):
    today = _today()
    start7 = today - timedelta(days=6)
    qs7 = DailyStat.objects.filter(user=request.user, date__range=[start7, today]).order_by('date')

    start30 = today - timedelta(days=29)
    qs30 = DailyStat.objects.filter(user=request.user, date__range=[start30, today]).order_by('date')

    pack = lambda qs: [
        {
            'd': d.date.isoformat(),
            'min': d.minutes,
            'kcal': d.calories,
            'w': d.workouts
        } for d in qs
    ]

    return JsonResponse({'last7': pack(qs7), 'last30': pack(qs30)})


@login_required
def complete_exercise(request, exercise_id):
    if request.method != "POST":
        return HttpResponseBadRequest("POST required")

    Exercise = __get__model('Exercise')
    if Exercise is None:
        return HttpResponse("yogafeatures.Exercise model not found.", status=400)

    ex = get_object_or_404(Exercise, id=exercise_id)

    # create or mark done for today
    ep, created = ExerciseProgress.objects.get_or_create(
        user=request.user,
        exercise=ex,
        course=ex.course,
        date=timezone.localdate(),
        defaults={"done": True}
    )
    if not ep.done:
        ep.done = True
        ep.save()

    # update daily stats
    add_min = int(request.POST.get("minutes", 10) or 10)
    add_kcal = int(request.POST.get("kcal", 30) or 30)
    stat, _ = DailyStat.objects.get_or_create(user=request.user, date=timezone.localdate())
    stat.minutes += add_min
    stat.calories += add_kcal
    stat.workouts += 1
    stat.save()

    # update course progress
    total = ex.course.exercises.count() or 1
    done_count = ExerciseProgress.objects.filter(
        user=request.user, course=ex.course, done=True
    ).values("exercise").distinct().count()
    percent = round((done_count / total) * 100, 2)

    cp, _ = CourseProgress.objects.get_or_create(user=request.user, course=ex.course)
    cp.percent_complete = percent
    if percent >= 100 and cp.completed_at is None:
        cp.completed_at = timezone.now()
    cp.save()

    return redirect("progress:progress_tracker")


def meditate_view(request):
    return render(request, 'progress/meditate.html')