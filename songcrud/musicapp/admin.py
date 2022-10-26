from django.contrib import admin
from .models import Artiste, Song, Lyric

# Register your models here.

@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    pass


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass


@admin.register(Lyric)
class LyricAdmin(admin.ModelAdmin):
    list_display = ('content', 'songid')