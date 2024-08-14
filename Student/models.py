from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='Student/images/')
    email = models.CharField(max_length = 30)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"