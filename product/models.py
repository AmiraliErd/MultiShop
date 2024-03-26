from django.db import models


class Size(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    cover = models.ImageField(upload_to='products')
    size = models.ManyToManyField(Size, blank=True, related_name='products')
    color = models.ManyToManyField(Color, blank=True, related_name='products')

    def __str__(self):
        return self.title


class Information(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='informations')
    text = models.TextField()

    def __str__(self):
        return self.text[:60]


class Image(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, related_name='images')
    file = models.ImageField(upload_to='products')

    def __str__(self):
        return self.file.url
