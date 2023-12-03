from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)
    carbohydrates = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    fiber = models.FloatField()
    calories = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Consume(models.Model):
    food = models.ForeignKey(Food, on_delete=models.SET(f'deleted food'))
    user = models.ForeignKey(User, on_delete=models.SET(f'deleted user'))
    consumed_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.user} ate {self.food}'