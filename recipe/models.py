from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    user = models.ForeignKey(User , on_delete = models.SET_NULL , null = True , blank = True)
    recipe_name = models.CharField(max_length= 100)
    recipe_decription = models.TextField()
    recipe_image = models.ImageField(upload_to = "image") #upload_to is a variable that create folder for storing image

    def __str__(self) -> str:
        return self.recipe_name







