from django.db import models
class Course(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="Course/images/" , blank=True, null=True)
    month = models.IntegerField()
    Course_fee = models.IntegerField()

    def __str__(self):
        return self.name



