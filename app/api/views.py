# coding: utf-8
from .models import Point
from .models import PointSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
import geojson


class GeoJson(APIView):
    """
    Endpoint spécific de l'API, lors d'un appel GET sur ce endpoint
    Les données de la base sont renvoyées sous forme de GeoJSON
    cf : https://fr.wikipedia.org/wiki/GeoJSON
    Si plusieurs points ont le même element_name, passage en LineString
    Si le point dispose d'un element_name unique, passage en Point
    """

    def get(self, request):    
        # Récupération des objets triés par date ascendante
        queryset = Point.objects.all().order_by('-date')
        
        # Création d'un catalogue permettant sur les clefs element_name
        # catalog['NomVille'] = [(long, lat)]
        # catalog['AbeilleBourbon'] = [(long,lat),(lat,long)]
        catalog = {}
        attributes = {}
        for p in queryset:
            serp = PointSerializer(p)
            url = reverse('points-detail', args=[serp.data['id']], request=request)
            # Si non présent dans le catalog création d'un enregistrement
            if p.element_name not in catalog.keys():
                catalog[p.element_name] = [(p.longitude, p.latitude)]
                attributes[p.element_name] = { "url": url,
                                               "name": p.element_name }
            # Sinon, ajout du point à la clef
            else:
                catalog[p.element_name].append((p.longitude, p.latitude))

        # Transformation du catalog en objet GeoJSON
        elements = []
        for key in catalog.keys():
            e = catalog[key]
            if len(e) > 1:
                # Cas d'un element_name avec plusieurs Point
                # Transformation en LineString
                # + un Point pour le premier élément
                line = geojson.LineString(e)
                point = geojson.Point(e[0])
                # Add trajectory
                feature = geojson.Feature(geometry=line)
                elements.append(feature)
                # Add marker for first position
                feature = geojson.Feature(geometry=point,
                                          properties=attributes[key])
                elements.append(feature)
            else:
                # Cas d'un élement 
                point = geojson.Point(e[0])
                feature = geojson.Feature(geometry=point,
                                          properties=attributes[key])
                elements.append(feature)
        geo_collection = geojson.FeatureCollection(elements)
        return Response(geo_collection)



class PointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows adding and removing Point
    """
    queryset = Point.objects.all()
    serializer_class = PointSerializer
