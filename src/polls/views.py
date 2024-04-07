from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import minecraft_data

MAX_ITEMS = 13
MAX_PAGNATION = 5

MAIN_PAGES = {
    "Items": "get_list_item", 
    "Blocks": "get_list_block", 
    "Effects": "get_list_effect", 
    "Biomes": "get_list_biome",
    "Entities": "get_list_entity",
    "Windows": "get_list_window"
}

# Utility methods
def getById(request, type, data, id):
    context = {
        "data": data[id],
    }
    return render(request, f"{type}/index.html", context)

def getItemsById(request, version, link, data, max_items, sort_using = "displayName", should_sort = True):
    sorted_data = sorted(data, key=lambda x: x[sort_using]) if should_sort else data
    offset = int(request.GET.get('offset', 0))
    
    start_offset = offset * max_items
    end_offset = start_offset + max_items
    data_size = len(sorted_data)
    
    if end_offset >= data_size:
        end_offset = data_size
        
    page_num = (data_size - (data_size % max_items)) / max_items
    nearest_page = offset - (offset % MAX_PAGNATION)
    
    context = {
        "link": link,
        "main_pages": MAIN_PAGES,
        "version": version,
        "offset": offset,
        "pagnation_list": [i for i in range(nearest_page, nearest_page + MAX_PAGNATION) if i <= page_num],
        "data_size": page_num,
        "data": sorted_data[start_offset : end_offset],
    }
    return render(request, f"listdata.html", context)

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def get_list_item(request, version):
    minecraft = minecraft_data(version)
    return getItemsById(request, version, "get_item", minecraft.items_list, MAX_ITEMS)

def get_list_block(request, version):
    minecraft = minecraft_data(version)
    return getItemsById(request, version, "get_block", minecraft.blocks_list, MAX_ITEMS)

def get_list_effect(request, version):
    minecraft = minecraft_data(version)
    return getItemsById(request, version, "get_effect", minecraft.effects_list, MAX_ITEMS)

def get_list_biome(request, version):
    minecraft = minecraft_data(version)
    return getItemsById(request, version, "get_biome", minecraft.biomes_list, MAX_ITEMS)

def get_list_entity(request, version):
    minecraft = minecraft_data(version)
    return getItemsById(request, version, "get_entity", minecraft.entities_list, MAX_ITEMS)

def get_list_window(request, version):
    minecraft = minecraft_data(version)
    return getItemsById(request, version, "get_window", minecraft.windows_list, MAX_ITEMS, "name")


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
    return getById(request, "biome", minecraft.biomes_name, id)

def get_entity(request, version, id):
    minecraft = minecraft_data(version)
    return getById(request, "entity", minecraft.entities_name, id)

def get_window(request, version, id):
    minecraft = minecraft_data(version)
    return getById(request, "window", minecraft.windows_name, id)