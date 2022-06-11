from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(
        max_length=222,
        blank=True,
        null=True,
        db_index= True,
        default='No name'
        )

    description = models.TextField( blank=True)

    image= models.ImageField(
        upload_to='images',
        blank=True
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    is_published = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class Price(models.Model):

    name = models.CharField(
        max_length=222,
        blank=True,
        null=True,
        db_index= True,
        default='No name'
        )

    description = models.TextField( blank=True)

    price= models.IntegerField(
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['price']
