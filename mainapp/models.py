from django.db import models


class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    name = models.CharField(verbose_name='имя категории', max_length=255, unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    category = models.ForeignKey(ProductCategory, verbose_name='категория товара', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='кратко', max_length=60, blank=True, null=True)
    description = models.TextField(verbose_name='подробно', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='склад', default=0)

    def __str__(self):
        return self.name + ' (' + self.category.name + ')'
