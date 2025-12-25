from django.urls import path
from . import views

app_name = "oyun_degerlendirme"

urlpatterns = [
    path("", views.degerlendirme_listesi, name="liste"),
    path("ekle/", views.degerlendirme_ekle, name="ekle"),
    path("duzenle/<int:id>/", views.degerlendirme_duzenle, name="duzenle"),
    path("sil/<int:id>/", views.degerlendirme_sil, name="sil"),
]
