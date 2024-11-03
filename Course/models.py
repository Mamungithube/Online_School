from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User,Group, Permission
class Course(models.Model):
    enrolled_users = models.ForeignKey(User, on_delete = models.CASCADE,null = True,blank = True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="Course/images/")
    month = models.IntegerField()
    Course_fee = models.IntegerField()

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    ROLES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    user_role = models.CharField(max_length=50, choices=ROLES, null=True, blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Custom related name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Custom related name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username
