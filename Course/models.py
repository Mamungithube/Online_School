from django.db import models
from django.contrib.auth.models import User
class Course(models.Model):
    enrolled_users = models.ForeignKey(User, on_delete = models.CASCADE,null = True,blank = True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="Course/images/")
    month = models.IntegerField()
    Course_fee = models.IntegerField()

    def __str__(self):
        return self.name
