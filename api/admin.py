from django.contrib import admin
from .models import Programer 
from django.db.models.query import QuerySet
import os

admin.site.register(Programer)


@admin.register(Programer)
class ProgramerAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        if not isinstance(obj, QuerySet):
            obj = [obj]  # Convertir a lista si no es iterable
        for item in obj:
            if os.path.isfile(item.image.path):
                os.remove(item.image.path)
        super().delete_model(request, obj)