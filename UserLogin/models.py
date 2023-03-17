from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return "User#" + str(self.user_id)