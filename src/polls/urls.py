from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    path("<str:version>/item/", views.get_list_item, name="get_list_item"),
    path("<str:version>/block/", views.get_list_block, name="get_list_block"),
    path("<str:version>/effect/", views.get_list_effect, name="get_list_effect"),
    path("<str:version>/biome/", views.get_list_biome, name="get_list_biome"),
    
    path("<str:version>/item/<str:id>/", views.get_item, name="get_item"),
    path("<str:version>/block/<str:id>/", views.get_block, name="get_block"),
    path("<str:version>/effect/<str:id>/", views.get_effect, name="get_effect"),
    path("<str:version>/biome/<str:id>/", views.get_biome, name="get_biome"),
]