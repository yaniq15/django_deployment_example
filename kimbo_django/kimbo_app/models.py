from django.db import models


# Create your models here.
on_delete=models.DO_NOTHING,

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True) # on deternine le model un champ de car avec une limite

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic= models.ForeignKey(Topic, on_delete=models.CASCADE) # la colonne de notre tableau avec une cle de notre topic

    name = models.CharField(max_length=264, unique=True) # deux colonne
    url = models.URLField(unique=True) # troisiemme colone

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)

    date = models.DateField()

    def __str__(self):
        return str(self.date)