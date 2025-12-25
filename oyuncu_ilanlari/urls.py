from django.urls import path
from . import views

app_name = "oyuncu_ilanlari"

urlpatterns = [
    path("", views.ilan_listesi, name="ilan_listesi"),
    path("ekle/", views.ilan_ekle, name="ilan_ekle"),  # Bu satırı ekledik
    path("duzenle/<int:id>/", views.ilan_duzenle, name="ilan_duzenle"),
    path("sil/<int:id>/", views.ilan_sil, name="ilan_sil"),
]