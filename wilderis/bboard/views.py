from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView
from .forms import UserCreationForm,ProductForm
from django.urls import reverse_lazy
from .models import Products
# Create your views here.

class FirstView(TemplateView):
    template_name = 'start.html'
class ProductsView(ListView):
    model = Products
    context_object_name = 'product'
    template_name = 'main.html'
class ProductsDetailView(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'producti.html'

def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form.save()
        return redirect("main")

    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {'form': form})

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registr.html'
    success_url = reverse_lazy('login')

class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'productcreate.html'
    success_url = reverse_lazy('main')