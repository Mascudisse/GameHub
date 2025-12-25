from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    
   path('aksiyon_macera/',views.aksiyon_macera_view,name="aksiyon_macera"),
   path('ana_oyunlar/',views.ana_oyunlar_view,name="ana_oyunlar"),
   path('hayatta_kalma/',views.hayatta_kalma_view,name="hayatta_kalma"),
   path('korku/',views.korku_view,name="korku"),
   path('mmorpg/',views.mmorpg_view,name="mmorpg"),
   path('platform/',views.platform_view,name="platform"),
   path('rol_yapma/',views.rol_yapma_view,name="rol_yapma"),
   path('simulasyon/',views.simulasyon_view,name="simulasyon"),
   path('spor/',views.spor_view,name="spor"),
   path('strateji/',views.strateji_view,name="strateji"),
   path('god_of_war2/',views.god_of_war2_view,name="god_of_war2")

   

]