from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from .forms import ProductForm, UserCreationForm
from django.urls import reverse_lazy
from .models import Products
# Create your views here.
class Main(TemplateView):
    template_name = 'main.html'

class MainView(ListView):
    model = Products
    template_name = 'main.html'
    context_object_name = 'Product'

class DetView(DetailView):
    model = Products
    template_name = 'detail.html'
    context_object_name = 'Product'


class ProductView(CreateView):
    form_class = ProductForm
    template_name = 'product.html'
    success_url = reverse_lazy('main')

def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form.save()
        return redirect("main")

    else:
        form = UserCreationForm()

    return render(request, "registration/registration.html", {'form': form})

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
