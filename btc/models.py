from django.db import models
# Create your models here.
class BTC(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    fiat = models.CharField(max_length=10)
    crypto = models.DecimalField(decimal_places=8, max_digits=18, default=0)

    def __str__(self):
        return self.fiat



