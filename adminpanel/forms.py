from django import forms
from django.contrib.auth import get_user_model
from .models import AdminProfile, Announcement

User = get_user_model()

class RoleAssignForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label='Select user')
    role = forms.ChoiceField(choices=AdminProfile.ROLE_CHOICES, label='Assign role')

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'message']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Announcement title'}),
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write message...'}),
        }
