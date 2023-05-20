from django.contrib import admin
from pet.resources import EspecieResource, RacaResource
from import_export.admin import ImportExportModelAdmin

from pet.models import Especie, Raca


class EspecieAdmin(ImportExportModelAdmin):
    resource_classes = [EspecieResource]


admin.site.register(Especie, EspecieAdmin)


class RacaAdmin(ImportExportModelAdmin):
    resource_classes = [RacaResource]


admin.site.register(Raca, RacaAdmin)
