from django.db import models
from django.contrib.auth.models import User


# Create your models here.

"""
1.Recipe
id
name
description
instructions
prep-time
cook-time
image-url
views
ingredients
2.Category
category-id
name
3.Userprofile
user-id
username
email
password
4.Feedback
email
phone.no
review(textfield)
rating(floatfield)

"""
class Category(models.Model):
    name=models.CharField(max_length=30)


class Recipe(models.Model):
    name=models.CharField(max_length=30)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.TextField(max_length=1000)
    instructions=models.TextField(max_length=2000)
    prep_time=models.IntegerField(null=True,blank=True)
    cook_time=models.IntegerField(null=True,blank=True)
    image_url=models.ImageField
    number_of_views=models.IntegerField(default=0)
    ingredients=models.TextField(max_length=3000)
    
class Userprofile(models.Model):
   recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
   name=models.CharField(max_length=30)
   email=models.EmailField()
   mobilenumber=models.IntegerField(max_length=15)
   review=models.TextField(max_length=200)
   rating=models.FloatField(default=0)
   
   
    
    
    
    