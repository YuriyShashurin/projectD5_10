from django.contrib import admin
from pets import models


# Register your models here.
@admin.register(models.Pet)
class PetAdmin (admin.ModelAdmin):
    fields = ('nickname', 'sex', 'breed', 'description', 'date_enter', 'type','year','photo', 'vetpasport')
    list_display = ('nickname', 'sex', 'year', 'pk', 'date_enter', 'like')

@admin.register(models.Breed)
class BreedAdmin (admin.ModelAdmin):
    pass

@admin.register(models.Animal)
class AnimalAdmin (admin.ModelAdmin):
    fields = ('type', 'icon')
    list_display = ('type','slug')


@admin.register(models.Blog)
class BlogAdmin (admin.ModelAdmin):
    fields = ('title', 'date', 'blogpost')
    list_display = ('title', 'date', 'small_decc')