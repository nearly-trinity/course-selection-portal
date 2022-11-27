from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=20)
    
class ClassData(models.Model):
    course = models.CharField(max_length=9)
    title = models.CharField(max_length=150)
    credits = models.IntegerField()

    # store list of prereqs as a comma seperated string
    prereqs = models.TextField(max_length=None)

    def __str__(self):
        return f"{self.course}: {self.title}"