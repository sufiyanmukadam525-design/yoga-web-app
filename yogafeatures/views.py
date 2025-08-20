from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Exercise, YogaPlan, YogaCourse
from .forms import ExerciseForm

def exercise_list(request, course_id):
    course = get_object_or_404(YogaCourse, id=course_id)
    exercises = course.exercises.all()
    return render(request, 'yogafeatures/exercise_list.html', {'course': course, 'exercises': exercises})


def plans_list(request):
    print(YogaPlan.objects.all())
    plans = YogaPlan.objects.all()

    return render(request, 'yogafeatures/plans.html', {'plans': plans})

def plan_detail(request, plan_id):
    plan = get_object_or_404(YogaPlan, id=plan_id)
    courses = plan.courses.all()
    return render(request, 'yogafeatures/plan_detail.html', {'plan': plan, 'courses': courses})


@login_required
def exercise_detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('plans')  # or wherever you want after saving
    else:
        form = ExerciseForm()
    return render(request, 'yogafeatures/exercise_detail.html', {'form': form})