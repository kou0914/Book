from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = "account/sigunp.html"
    success_url = reverse_lazy("index")
# Create your views here.
