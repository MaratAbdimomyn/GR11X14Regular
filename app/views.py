from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

class ActionView(ListView):
    model = Action
    template_name = 'home.html'
    context_object_name = 'actions'

class AboutAction(DetailView):
    model = Action
    template_name = 'about.html'
    context_object_name = 'action'
    pk_url_kwarg = 'id'

class CreateAction(CreateView):
    model = Action
    form_class = ActionForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')

class DeleteAction(DeleteView):    
    model = Action
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')