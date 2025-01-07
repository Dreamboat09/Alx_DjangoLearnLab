from django.db import models

# Create your models here.
# setting up RBAC system
from django.contrib.auth.models import User
    
class UserProfile(models.Model):
    Roles = [
        ('Admin', 'admin'),
        ('Librarian', 'librarian'),
        ('Member', 'member'),
        ]
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    role = models.CharField(max_length=9, choices=Roles, default='Member')
    
    def __str__(self):
        return f'{self.user.username} - {self.role}'