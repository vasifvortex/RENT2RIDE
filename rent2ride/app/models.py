from django.db import models

class Cycle(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField()
    image = models.URLField()
    class Meta:
        db_table = 'cycle'
    def __str__(self):
        return self.name