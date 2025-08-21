from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.db.models import Count

from .forms import RoleAssignForm, AnnouncementForm
from .models import AdminProfile, Announcement

User = get_user_model()

def user_is_admin(user):
    if not user.is_authenticated:
        return False
    if user.is_superuser or user.is_staff:
        return True
    prof = getattr(user, 'admin_profile', None)
    return bool(prof and prof.is_active)

@login_required
def admin_dashboard(request):
    if not user_is_admin(request.user):
        messages.error(request, "You don't have admin access.")
        return redirect('login')
    context = {
        'total_users': User.objects.count(),
        'total_admins': AdminProfile.objects.filter(is_active=True).count(),
        'total_announcements': Announcement.objects.count(),
        'latest_announcements': Announcement.objects.select_related('created_by')[:5],
    }
    return render(request, 'adminpanel/admin_dashboard.html', context)

@login_required
def user_management_dashboard(request):
    if not user_is_admin(request.user):
        messages.error(request, "You don't have admin access.")
        return redirect('login')

    if request.method == 'POST':
        form = RoleAssignForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            role = form.cleaned_data['role']
            profile, _ = AdminProfile.objects.get_or_create(user=user)
            profile.role = role
            profile.is_active = True
            profile.save()
            messages.success(request, f"Assigned {role} role to {user.username}")
            return redirect('adminpanel:user_mgmt')
    else:
        form = RoleAssignForm()

    context = {
        'form': form,
        'admins': AdminProfile.objects.select_related('user').all(),
        'users': User.objects.all()[:50],
    }
    return render(request, 'adminpanel/user_management_dashboard.html', context)

@login_required
def content_dashboard(request):
    if not user_is_admin(request.user):
        messages.error(request, "You don't have admin access.")
        return redirect('login')

    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            ann = form.save(commit=False)
            ann.created_by = request.user
            ann.save()
            messages.success(request, 'Announcement published successfully!')
            return redirect('adminpanel:content')
    else:
        form = AnnouncementForm()

    context = {
        'form': form,
        'announcements': Announcement.objects.select_related('created_by')[:20],
    }
    return render(request, 'adminpanel/plan_moderation_dashboard.html', context)

@login_required
def reports_dashboard(request):
    if not user_is_admin(request.user):
        messages.error(request, "You don't have admin access.")
        return redirect('login')

    context = {
        'user_counts': User.objects.aggregate(total=Count('id')),
        'announcement_count': Announcement.objects.count(),
        'latest_announcements': Announcement.objects.all()[:5],
    }
    return render(request, 'adminpanel/reports_dashboard.html', context)
