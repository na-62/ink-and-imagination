from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    media = models.TextField()

    @property
    def is_professional(self):
        return self.price >= 500000