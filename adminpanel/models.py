from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class AdminProfile(models.Model):
    ROLE_SUPERADMIN = 'SUPERADMIN'
    ROLE_CONTENT = 'CONTENT'
    ROLE_SUPPORT = 'SUPPORT'

    ROLE_CHOICES = [
        (ROLE_SUPERADMIN, 'Super Admin'),
        (ROLE_CONTENT, 'Content Admin'),
        (ROLE_SUPPORT, 'Support'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_SUPPORT)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='announcements')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


