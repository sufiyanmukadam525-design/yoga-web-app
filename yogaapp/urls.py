from django.urls import path
<<<<<<< HEAD
from .views import HomeView, ProfileEdit, Register, Login, Logout, Base
=======
from .views import HomeView, Register, Login, Logout, Base
>>>>>>> 378cfd2d643889c1b7f817a9487d8e62135be505
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', Register.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('base/', Base.as_view(), name='base'),
    path('profile/', views.profile_view, name='profile'),
<<<<<<< HEAD
    path('profile/edit/', ProfileEdit.as_view(), name='profile_edit'),
=======
>>>>>>> 378cfd2d643889c1b7f817a9487d8e62135be505
]
