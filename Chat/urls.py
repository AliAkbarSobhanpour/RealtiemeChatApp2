# urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # ...
    path('auth/register/', views.Register, name='register-page'),
    # ...
    path("auth/login", LoginView.as_view(template_name="Chat/login.html"), name="login-page"),
    # ...
    path("auth/logout", LogoutView.as_view(), name="logout-page"),
    # ...
]