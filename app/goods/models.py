from django.db import models

# Create your models here. Model = table

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'



    def __str__(self):
        return self.name
    

class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='deps/images/goods/', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Скидка в %', blank=True, null=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')






    def __str__(self):
        return self.name
    

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'