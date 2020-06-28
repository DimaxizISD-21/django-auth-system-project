from django.urls import path
from . views import SignUpView, HomePageView
from . import views

urlpatterns = [
    path('otp/', views.OtpAuthentificateView, name='auth_otp'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home'),
]