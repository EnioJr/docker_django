from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    # Usuario se cadastra
    form_class = UserCreationForm
    # Usuario e direcionado para o login
    success_url = reverse_lazy('login')
    # defini o template(register) na pasta raiz do projeto em templates
    template_name = 'registration/register.html'
