from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
import minecraft_data

MAX_ITEMS = 10
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

def render404Page(version, message):
    context = {
        "message": message
    }
    context.update(sidebarData(version))
    return context

def sidebarData(version):
    return {
        "main_pages": MAIN_PAGES,
        "version": version,
    }
    
def pagnationData(sorted_data, offset):
    data_size = len(sorted_data)
    
    page_num = (data_size - (data_size % MAX_ITEMS)) / MAX_ITEMS
    nearest_page = offset - (offset % MAX_PAGNATION)
    
    return {
        "offset": offset,
        "pagnation_list": [i for i in range(nearest_page, nearest_page + MAX_PAGNATION) if i <= page_num],
        "data_size": page_num,
    }

def getById(request, version, type, data, id):
    try:
        context = {
            "data": data[id],
        }
        context.update(sidebarData(version))
        return render(request, f"{type}/index.html", context)
    except KeyError:
        return render(request, f"error404.html", render404Page(version, f"Data for {type} \"{id}\" not Found"))
        #raise Http404(f"{type} does not exist")

def getItemsById(request, version, link, data, max_items, sort_using = "displayName", should_sort = True):
    sorted_data = sorted(data, key=lambda x: x[sort_using]) if should_sort else data
    offset = int(request.GET.get('offset', 0))
    
    start_offset = offset * max_items
    end_offset = start_offset + max_items
    data_size = len(sorted_data)
    
    if end_offset >= data_size:
        end_offset = data_size
        
    # search data
    search_data = {}
    for d in sorted_data:
        search_data[d["name"]] = ""
    
    context = {
        "link": link,
        "offset": offset,
        "data": sorted_data[start_offset : end_offset],
        "search_data": search_data
    }
    
    context.update(sidebarData(version))
    context.update(pagnationData(sorted_data, offset))
    return render(request, f"listdata.html", context)

# Create your views here.
def main_page(request):
    return redirect(reverse("get_list_item", kwargs={'version': "1.19"}))

def versions(request, version):
    return redirect(reverse("get_list_item", kwargs={'version': version}))


def get_list_item(request, version):
    try:
        minecraft = minecraft_data(version)
    except KeyError:
        return render(request, f"error404.html", render404Page("?", f"Version {version} not Found"))
    return getItemsById(request, version, "get_item", minecraft.items_list, MAX_ITEMS)

def get_list_block(request, version):
    try:
        minecraft = minecraft_data(version)
    except KeyError:
        return render(request, f"error404.html", render404Page("?", f"Version {version} not Found"))
    return getItemsById(request, version, "get_block", minecraft.blocks_list, MAX_ITEMS)

def get_list_effect(request, version):
    try:
        minecraft = minecraft_data(version)
    except KeyError:
        return render(request, f"error404.html", render404Page("?", f"Version {version} not Found"))
    return getItemsById(request, version, "get_effect", minecraft.effects_list, MAX_ITEMS)

def get_list_biome(request, version):
    try:
        minecraft = minecraft_data(version)
    except KeyError:
        return render(request, f"error404.html", render404Page("?", f"Version {version} not Found"))
    return getItemsById(request, version, "get_biome", minecraft.biomes_list, MAX_ITEMS)

def get_list_entity(request, version):
    try:
        minecraft = minecraft_data(version)
    except KeyError:
        return render(request, f"error404.html", render404Page("?", f"Version {version} not Found"))
    return getItemsById(request, version, "get_entity", minecraft.entities_list, MAX_ITEMS)

def get_list_window(request, version):
    try:
        minecraft = minecraft_data(version)
    except KeyError:
        return render(request, f"error404.html", render404Page("?", f"Version {version} not Found"))
    return getItemsById(request, version, "get_window", minecraft.windows_list, MAX_ITEMS, "name")


def get_item(request, version, id):
    try:
        minecraft = minecraft_data(version)
    except KeyError:
        return render(request, f"error404.html", render404Page("?", f"Version {version} not Found"))
    return getById(request, version, "item", minecraft.items_name, id)

def get_block(request, version, id):
    try:
        minecraft = minecraft_data(version)
    except KeyError:
        return render(request, f"error404.html", render404Page("?", f"Version {version} not Found"))
    return getById(request, version, "block", minecraft.blocks_name, id)

def get_effect(request, version, id):
    try:
        minecraft = minecraft_data(version)
    except KeyError:
        return render(request, f"error404.html", render404Page("?", f"Version {version} not Found"))
    return getById(request, version, "effect", minecraft.effects_name, id)

def get_biome(request, version, id):
    try:
        minecraft = minecraft_data(version)
    except KeyError:
        return render(request, f"error404.html", render404Page("?", f"Version {version} not Found"))
    return getById(request, version, "biome", minecraft.biomes_name, id)

def get_entity(request, version, id):
    try:
        minecraft = minecraft_data(version)
    except KeyError:
        return render(request, f"error404.html", render404Page("?", f"Version {version} not Found"))
    return getById(request, version, "entity", minecraft.entities_name, id)

def get_window(request, version, id):
    try:
        minecraft = minecraft_data(version)
    except KeyError:
        return render(request, f"error404.html", render404Page("?", f"Version {version} not Found"))
    return getById(request, version, "window", minecraft.windows_name, id)