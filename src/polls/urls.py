from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:version>/item/<str:id>/", views.get_item, name="get_item"),
    path("<str:version>/block/<str:id>/", views.get_block, name="get_block"),
    path("<str:version>/effect/<str:id>/", views.get_effect, name="get_effect"),
    #path("<str:version>/biome/<str:id>/", views.index_id, name="get_biome"),
]