from django.urls import path
from rapidog import views


urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='signup')
]
