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
        return reverse('kids_detail', kwargs={'kid_id': self.id})