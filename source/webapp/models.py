
from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


    

class Product(models.Model):
    
    class CategoryChoices(models.TextChoices):
        OTHER = 'other', 'Разное'
        TV = 'tv', 'Телевизор'
        SMARTPHONE = 'Smartphone', 'Смартфон'
        LAPTOP = 'Laptop', 'Ноутбук'
    
    name = models.CharField(verbose_name='Наименование', max_length=100, blank=False, null=False)
    description = models.TextField(verbose_name='Описание',max_length=2000, null=True, blank=True)
    image = models.CharField(verbose_name='Фото', max_length=100, blank=False, null=False)
    category = models.CharField(verbose_name='Категория',choices=CategoryChoices.choices, default=CategoryChoices.OTHER ,max_length=50, blank=False, null=False)
    balance = models.IntegerField(verbose_name='Остаток',validators=[MinValueValidator(0)],blank=False, null=False)
    price = models.DecimalField(verbose_name='Стоимость',max_digits=7, decimal_places=2,blank=False, null=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    
    class Meta:
        ordering = ('category','name')