from livraria.models import Editora
from livraria.serializers import EditoraSerializer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    #permission_classes = [IsAuthenticated]
