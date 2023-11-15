from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Kid(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    description = models.CharField(max_length=200, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('kid_detail', kwargs={'kid_id': self.id})
    

class Event(models.Model):
    EVENTS = (
        ('A', 'Activity'),
        ('D', 'Diaper'),
        ('F', 'Feeding'),
        ('M', 'Medicine'),
        ('N', 'Nap'),
        ('S', 'Sick'),
    )
    
    event = models.CharField(max_length=1, choices=EVENTS, default=EVENTS[0][0], verbose_name='event type')
    description = models.CharField(max_length=250, verbose_name='event description')
    date = models.DateField('event date')
    time = models.TimeField('event time')
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_event_display()} on {self.date}"
    
    class Meta:
        ordering = ('-date', '-time',)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for kid_id: {self.kid_id} @{self.url}"