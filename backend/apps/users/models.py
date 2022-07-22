import uuid
from django.db import models
import uuid

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    info = models.CharField(max_length=256,blank=True,null=True)
