from django.db import models


class Product(models.Model):
    title = models.CharField("Название", max_length=50)
    text = models.TextField("Описание")
    price = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        verbose_name = 'Товар'

    def __str__(self):
        return self.title

