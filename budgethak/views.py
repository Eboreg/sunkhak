# -*- coding: utf-8 -*-

import json
from ipware import get_client_ip
from django.conf import settings
from django.shortcuts import render, reverse
from django.views.generic.base import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PlaceSerializer, PlaceListSerializer, PlaceUserEditSerializer
from .forms import PlaceForm
from .models import Place, PlaceUserEdit

"""
REST-API.
Åtkomst via /api/places/.
"""
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.only_visible()
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == "retrieve":
            return PlaceSerializer
        elif self.action == "list":
            return PlaceListSerializer
        elif self.action == "update":
            return PlaceUserEditSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        place = self.queryset.get(slug=kwargs.pop("slug"))
        instance = PlaceUserEdit(place=place, ip_address=get_client_ip(request)[0])
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if not serializer.is_valid():
            errors = serializer.errors.copy()
            try:
                for idx in range(0, len(errors['opening_hours'])):
                    for key, value in errors['opening_hours'][idx].items():
                        errors[key+'-'+str(idx)] = value
            except:
                pass
            return Response(data=errors, status=400)
        elif serializer.has_changed():
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response(serializer.initial_data)


"""
Langar upp templates/index.html med lämplig context.
"""
class IndexView(TemplateView):
    template_name = 'budgethak/index.html'
    queryset = Place.objects.only_visible()
    
    """
    Hämtar samma lista som PlaceViewSet.list(), men som JSON, så att vi kan bootstrappa in den i Backbone
    """
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        serializer = PlaceListSerializer(self.queryset, many=True)
        context['places'] = json.dumps(serializer.data, separators=(',', ':', ))
        image_upload_kwargs = {
            'upload_to': settings.AJAXIMAGE['UPLOAD_DIR'],
            'max_width': settings.AJAXIMAGE['MAX_WIDTH'],
            'max_height': settings.AJAXIMAGE['MAX_HEIGHT'],
            'crop': int(settings.AJAXIMAGE['CROP']),
        }
        context['image_upload_url'] = reverse('ajaximage', kwargs=image_upload_kwargs)
        return context


"""
Kan fyllas på med vad man nu önskar testa.
"""
class TestView(TemplateView):
    template_name = 'budgethak/test.html'
