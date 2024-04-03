from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import minecraft_data

# Utility methods
def getById(request, type, data, id):
    context = {
        "data": data[id],
    }
    return render(request, f"{type}/index.html", context)

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_item(request, version, id):
    minecraft = minecraft_data(version)
    return getById(request, "item", minecraft.items_name, id)

def get_block(request, version, id):
    minecraft = minecraft_data(version)
    return getById(request, "block", minecraft.blocks_name, id)

def get_effect(request, version, id):
    minecraft = minecraft_data(version)
    return getById(request, "effect", minecraft.effects_name, id)

def get_biome(request, version, id):
    minecraft = minecraft_data(version)
    return getById(request, "biome", minecraft.biomes, id)