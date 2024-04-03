from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import minecraft_data

MAX_ITEMS = 15

# Utility methods
def getById(request, type, data, id):
    context = {
        "data": data[id],
    }
    return render(request, f"{type}/single/index.html", context)

def getItemsById(request, type, data, offset, max_items):
    start_offset = offset * max_items
    end_offset = start_offset + max_items
    data_size = len(data)
    
    if end_offset >= data_size:
        end_offset = len(data) -1
    
    context = {
        "data_size": (data_size - (data_size % max_items)) / max_items,
        "data": data[start_offset : end_offset],
    }
    return render(request, f"{type}/main.html", context)

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def get_list_item(request, version, offset):
    minecraft = minecraft_data(version)
    return getItemsById(request, "item", minecraft.items_list, offset, MAX_ITEMS)

def get_list_block(request, version, offset):
    minecraft = minecraft_data(version)
    return getItemsById(request, "block", minecraft.blocks_list, offset, MAX_ITEMS)

def get_list_effect(request, version, offset):
    minecraft = minecraft_data(version)
    return getItemsById(request, "effect", minecraft.effects_list, offset, MAX_ITEMS)

def get_list_biome(request, version, offset):
    minecraft = minecraft_data(version)
    return getItemsById(request, "biome", minecraft.biomes_list, offset)


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