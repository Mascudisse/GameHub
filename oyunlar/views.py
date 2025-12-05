from django.shortcuts import render

# Create your views here.


def aksiyon_macera_view(request):
    return render(request,"aksiyon_macera.html")

def ana_oyunlar_view(request):
    return render(request,"ana_oyunlar.html")

def hayatta_kalma_view(request):
    return render(request,"hayatta_kalma.html")

def korku_view(request):
    return render(request,"korku.html")

def mmorpg_view(request):
    return render(request,"mmorpg.html")

def platform_view(request):
    return render(request,"platform.html")

def rol_yapma_view(request):
    return render(request,"rol_yapma.html")

def simulasyon_view(request):
    return render(request,"simulasyon.html")

def spor_view(request):
    return render(request,"spor.html")

def strateji_view(request):
    return render(request,"strateji.html")

def god_of_war2_view(request):
    return render(request,"god_of_war2.html")




