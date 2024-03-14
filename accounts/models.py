from django.db import models
from django.contrib.auth.models import User
from drinks.models import Drink


# Create your models here.
class Account(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    favourites = models.BooleanField(default=False)
    recent = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    db_table = "account"

class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Drink, on_delete=models.CASCADE)

    class Meta:
        db_table = "favourites"


class Recents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Drink, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "recents"
