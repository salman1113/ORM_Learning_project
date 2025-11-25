from django.db import models

# Create your models here.

class StudentManager(models.Manager):
    def active(self):
        return self.filter(is_active = True)

class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-name"]

    objects = StudentManager()


    def __str__(self):
        return self.name
    
