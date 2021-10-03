from django.db import models
from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator

class Point(models.Model):
    """
    Un Point est un objet dans la base donnée, un point est définit par
    latitude : compris entre 90 et -90, 0 à l'équateur
    longitude : compris entre 180 et -180, 0 à Greenwich
    element_name : Nom de l'objet a marquer
    comment : Non utilisé
    date : Date de la marque
    """
    element_name = models.CharField(max_length=128, null=False, blank=False)
    longitude = models.FloatField(blank=False,
            validators=[
                MaxValueValidator(180.0),
                MinValueValidator(-180.0)
            ])
    latitude = models.FloatField(blank=False,
            validators=[
                MaxValueValidator(90.0),
                MinValueValidator(-90.0)
            ])
    comment = models.CharField(max_length=128, blank=True, default='')
    date = models.DateField(null=False)

class PointSerializer(serializers.HyperlinkedModelSerializer):
    """
    Cette Class permet de serializer les données entre Models et API
    Aucune modification n'est nécessaire pour cette app de demo
    """
    class Meta:
        model = Point
        fields = ('id', 'element_name', 'longitude', 'latitude', 'comment', 'date')


