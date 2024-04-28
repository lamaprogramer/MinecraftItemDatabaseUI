from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_page, name="index"),
    path("<str:version>/", views.versions, name="versions"),
    
    path("<str:version>/item/", views.get_list_item, name="get_list_item"),
    path("<str:version>/block/", views.get_list_block, name="get_list_block"),
    path("<str:version>/effect/", views.get_list_effect, name="get_list_effect"),
    path("<str:version>/biome/", views.get_list_biome, name="get_list_biome"),
    path("<str:version>/entity/", views.get_list_entity, name="get_list_entity"),
    path("<str:version>/window/", views.get_list_window, name="get_list_window"),
    
    path("<str:version>/item/<str:id>/", views.get_item, name="get_item"),
    path("<str:version>/block/<str:id>/", views.get_block, name="get_block"),
    path("<str:version>/effect/<str:id>/", views.get_effect, name="get_effect"),
    path("<str:version>/biome/<str:id>/", views.get_biome, name="get_biome"),
    path("<str:version>/entity/<str:id>/", views.get_entity, name="get_entity"),
    path("<str:version>/window/<str:id>/", views.get_window, name="get_window"),
]