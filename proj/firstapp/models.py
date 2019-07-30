from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class FirstappModel(models.Model):
    name=models.CharField(max_length=230)
    completed=models.BooleanField(default=False)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def get_absolute_url(self):
        return reverse("detail",kwargs={"pk":self.pk})

    def __str__(self):
        return self.name