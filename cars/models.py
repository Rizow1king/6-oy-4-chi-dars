from django.db import models


class Brands(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Cars(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=150)
    year = models.IntegerField()
    count = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='media/photos', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    price = models.IntegerField(default=100.000)

    def __str__(self):
        return self.name
