from django.forms import ModelForm
from .models import Products
from django.contrib.auth.forms import UserCreationForm



class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ('title', 'price','image','rubric')

