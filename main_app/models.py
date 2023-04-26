from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Kid(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('kid_detail', kwargs={'kid_id': self.id})
    
class Feeding(models.Model):
    MEALS = (
        ('M', 'Milk/Formula'),
        ('BF', 'Baby Food/Puree'),
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
        ('S', 'Snack'),
    )
    
    date = models.DateField('feeding date')
    time = models.TimeField('feeding time')
    meal = models.CharField(max_length=2, choices=MEALS, default=MEALS[5][0], verbose_name='meal type')
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ('-date',)