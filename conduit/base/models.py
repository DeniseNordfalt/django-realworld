from django.db import models

# Create your models here.

# class Item(models.Model):
#     name = models.CharField(max_length=200)
#     created = models.DateTimeField(auto_now_add=True)
#     def __str__(self) :
#         return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField( default=0)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.name
    class Meta:
        db_table = 'User'
        ordering = ['name', 'age', 'created']