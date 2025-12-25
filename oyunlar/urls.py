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
   path('god_of_war2/',views.god_of_war2_view,name="god_of_war2"),
   path('spiderman2/',views.spiderman2_view,name="spiderman2"),
   path('we_were_here_together/',views.we_were_here_together_view,name="we_were_here_together"),
   path('battlefield6/',views.battlefield6_view,name="battlefield6"),
   path('thelastofus/',views.thelastofus_view,name="thelastofus"),
   path('robocop/',views.robocop_view,name="robocop"),
   path('first_life/',views.first_life_view,name="first_life"),
   path('bloodlines2/',views.bloodlines2_view,name="bloodlines2"),
   path('uncharted/',views.uncharted_view,name="uncharted"),
   path('hogwarts_legacy/',views.hogwarts_legacy_view,name="hogwarts_legacy"),
   path('europa4/',views.europa4_view,name="europa4"),
   path('crusader_kings3/',views.crusader_kings3_view,name="crusader_kings3"),
   path('civilization6/',views.civilization6_view,name="civilization6"),
   path('frostpunk2/',views.frostpunk2_view,name="frostpunk2"),
   path('hearts_of_iron4/',views.hearts_of_iron4_view,name="hearts_of_iron4"),
   path('age_of_mythology/',views.age_of_mythology_view,name="age_of_mythology"),
   path('manor_lords/',views.manor_lords_view,name="manor_lords"),
   path('age_of_empires/',views.age_of_empires_view,name="age_of_empires"),
   path('anno1800/',views.anno1800_view,name="anno_1800"),
   path('company_of_heroes2/',views.company_of_heroes2_view,name="company_of_heroes2"),
   path('witcher3/',views.witcher3_view,name="witcher3"),
   path('chrono_cross/',views.chrono_cross_view,name="chrono_cross"),
   path('legend_of_grimrock/',views.legend_of_grimrock_view,name="legend_of_grimrock"),
   path('final_fantasy9/',views.final_fantasy9_view,name="final_fantasy9"),
   path('persona5/',views.persona5_view,name="persona5"),
   path('baldurs_gate2/',views.baldurs_gate2_view,name="baldurs_gate2"),
   path('mass_effect2/',views.mass_effect2_view,name="mass_effect2"),
   path('disco_elysium/',views.disco_elysium_view,name="disco_elysium"),
   path('stardew_valley/',views.stardew_valley_view,name="stardew_valley"),
   path('pillars_of_eternity/',views.pillars_of_eternity_view,name="pillars_of_eternity"),
   path('amnesia/',views.amnesia_view,name="amnesia"),
   path('dying_light/',views.dying_light_view,name="dying_light"),
   path('visage/',views.visage_view,name="visage"),
   path('phasmophobia/',views.phasmophobia_view,name="phasmophobia"),
   path('outlast/',views.outlast_view,name="outlast"),
   path('dead_space/',views.dead_space_view,name="dead_space"),
   path('resident_evil/',views.resident_evil_view,name="resident_evil"),
   path('silent_hill2/',views.silent_hill2_view,name="silent_hill2"),
   path('alien_isolation2/',views.alien_isolation2_view,name="alien_isolation2"),
   path('huntdown/',views.huntdown_view,name="huntdown"),
   path('stranded_deep/',views.stranded_deep_view,name="stranded_deep"),
   path('forest/',views.forest_view,name="forest"),
   path('green_hell/',views.green_hell_view,name="green_hell"),
   path('rust/',views.rust_view,name="rust"),
   path('valheim/',views.valheim_view,name="valheim"),
   path('ark/',views.ark_view,name="ark"),
   path('outward/',views.outward_view,name="outward"),
   path('dont_starve_together/',views.dont_starve_together_view,name="dont_starve_together"),
   path('astroneer/',views.astroneer_view,name="astroneer"),
   path('conan_exiles/',views.conan_exiles_view,name="conan_exiles"),
   path('matchpoint/',views.matchpoint_view,name="matchpoint"),
   path('grand_mountain/',views.grand_mountain_view,name="grand_mountain"),
   path('fifa23/',views.fifa23_view,name="fifa23"),
   path('pes2018/',views.pes2018_view,name="pes2018"),
   path('wrc9/',views.wrc9_view,name="wrc9"),
   path('football_manager2026/',views.football_manager2026_view,name="football_manager2026"),
   path('ea_sports26/',views.ea_sports26_view,name="ea_sports26"),
   path('wwe/',views.wwe_view,name="wwe"),
   path('undisputed/',views.undisputed_view,name="undisputed"),
   path('way_of_the_hunter/',views.way_of_the_hunter_view,name="way_of_the_hunter")
   




   

]