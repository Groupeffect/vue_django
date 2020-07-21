from django.db import models

# Create your models here.

class User(AbstractUser):
    REQUIRED_FIELDS = ['email']
    email = models.EmailField( unique=True )
