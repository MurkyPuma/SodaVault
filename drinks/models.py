# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid


class Drink(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    unique_slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if (
            self.thumbnail == ""
            or self.thumbnail is None
            or self.thumbnail == "default.png"
        ):
            self.thumbnail = "default.png"
            # if not self.slug:  # Only set the slug when the object is first created.

            unique_suffix = uuid.uuid4().hex[:8]
            self.unique_slug = slugify(self.name) + "_" + unique_suffix
            self.slug = slugify(self.name)
            # self.slug = slugify(self.name)  # This will replace unwanted characters.
        super(Drink, self).save(*args, **kwargs)  # Call the "real" save() method.

    alcoholic = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(
        default="default.png",
        upload_to="drink_images/",
        blank=True,
        null=True,
    )
    glass = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    ingredient1 = models.TextField(blank=True, null=True)
    ingredient2 = models.TextField(blank=True, null=True)
    ingredient3 = models.TextField(blank=True, null=True)
    ingredient4 = models.TextField(blank=True, null=True)
    ingredient5 = models.TextField(blank=True, null=True)
    ingredient6 = models.TextField(blank=True, null=True)
    ingredient7 = models.TextField(blank=True, null=True)
    ingredient8 = models.TextField(blank=True, null=True)
    ingredient9 = models.TextField(blank=True, null=True)
    measurement1 = models.TextField(blank=True, null=True)
    measurement2 = models.TextField(blank=True, null=True)
    measurement3 = models.TextField(blank=True, null=True)
    measurement4 = models.TextField(blank=True, null=True)
    measurement5 = models.TextField(blank=True, null=True)
    measurement6 = models.TextField(blank=True, null=True)
    measurement7 = models.TextField(blank=True, null=True)
    measurement8 = models.TextField(blank=True, null=True)
    measurement9 = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        db_table = "drink"
