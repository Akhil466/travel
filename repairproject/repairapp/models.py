from django.db import models


class Edit(models.Model):
    name = models.CharField(max_length=250)
    descriptn = models.TextField()
    image = models.ImageField(upload_to='pics')


    def __str__(self):
        return self.name

class team(models.Model):
    name = models.CharField(max_length=250)
    descr = models.TextField()
    image = models.ImageField(upload_to='team')
    def __str__(self):
        return self.name