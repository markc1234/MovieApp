from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


# Create your views here.
class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm # segun defini CustomUser, es necesario ingresar email, usuario y contraseña(obligatorio)
    success_url = reverse_lazy('login') # redirecciona al template login
    template_name = 'signup.html'
