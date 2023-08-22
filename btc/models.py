from django.db import models
# Create your models here.
class BTC(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    fiat = models.CharField(max_length=10)
    crypto = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return self.fiat



