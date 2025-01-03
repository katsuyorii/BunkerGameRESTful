from django.contrib import admin
from .models import Profession, Health, Hobby, Phobia, Trait, Physique, Baggage, AdditionalInfo, SpecialAction, BunkerRooms, BunkerItems, Bunker, Catastrophe


# Переопределние поля NULL на значение - «---пусто---» в админ панеле django.
admin.AdminSite.empty_value_display = "---пусто---"


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Health)
class HealthAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Phobia)
class PhobiaAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Trait)
class TraitAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Physique)
class PhysiqueAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Baggage)
class BaggageAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ['description']


@admin.register(SpecialAction)
class SpecialActionAdmin(admin.ModelAdmin):
    list_display = ['description']


@admin.register(BunkerRooms)
class BunkerRoomsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(BunkerItems)
class BunkerItemsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Bunker)
class BunkerAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(Catastrophe)
class CatastropheAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']