from django.db import models


class Items(models.Model):
    _tablename_ = 'Site_Products'

    name = models.CharField(max_length=100)
    item_number = models.CharField(max_length=12)
    product = models.CharField(max_length=100)

    def products(self, *args, **kwargs):
        self.product = self.item_number + '-' + self.name
        super(Items, self).products(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.product = self.item_number + '-' + self.name

        super(Items, self).save(*args, **kwargs)

    def __str__(self):
        return self.item_number + ' ' + self.name
