from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from . forms import CustomUserCreationForm, OtpCreationForm
from datetime import datetime, timezone
import secrets



# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('auth_otp')
    template_name = "signup.html"

# class OtpVerificationView(CreateView):
#     form_class = OtpCreationForm
#     success_url = reverse_lazy('login')
#     template_name = "authentificate/auth_otp.html"



# OTP PASSWORD GENERATOR
def generateOTP():
    secrets_generate = secrets.SystemRandom()
    otp = secrets_generate.randrange(1000, 9999)
    sms = f"######################################################## \n\t\tFAKE SMS)) \n\t\tВаш OTP - пароль: {str(otp)} \n########################################################"
    print(sms)

def OtpAuthentificateView(request):
    form = OtpCreationForm()
    if request.method == 'GET':
        generateOTP()

    if request.method == 'POST':
        return HttpResponseRedirect(reverse_lazy('login'))

    context = {'form': form}
    return render(request, 'authentificate/auth_otp.html', context)
