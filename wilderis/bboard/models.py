from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.FileField(upload_to='uploads/', null=True)
    date = models.DateTimeField(auto_now_add=True)
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT)

class Rubric(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.title}'