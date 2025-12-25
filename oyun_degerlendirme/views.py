from django.shortcuts import render, redirect, get_object_or_404
from .models import OyunDegerlendirme

def degerlendirme_listesi(request):
    degerlendirmeler = OyunDegerlendirme.objects.all().order_by("-id")
    return render(request, "oyun_degerlendirme/liste.html", {
        "degerlendirmeler": degerlendirmeler
    })


def degerlendirme_ekle(request):
    if request.method == "POST":
        OyunDegerlendirme.objects.create(
            oyun_adi=request.POST["oyun_adi"],
            puan=request.POST["puan"],
            yorum=request.POST["yorum"],
            kullanici=request.user if request.user.is_authenticated else None
        )
        return redirect("oyun_degerlendirme:liste")

    return render(request, "oyun_degerlendirme/ekle.html")


def degerlendirme_duzenle(request, id):
    degerlendirme = get_object_or_404(OyunDegerlendirme, id=id)

    if request.method == "POST":
        degerlendirme.oyun_adi = request.POST["oyun_adi"]
        degerlendirme.puan = request.POST["puan"]
        degerlendirme.yorum = request.POST["yorum"]
        degerlendirme.save()
        return redirect("oyun_degerlendirme:liste")

    return render(request, "oyun_degerlendirme/duzenle.html", {
        "degerlendirme": degerlendirme
    })


def degerlendirme_sil(request, id):
    if request.method == "POST":
        degerlendirme = get_object_or_404(OyunDegerlendirme, id=id)
        degerlendirme.delete()
    return redirect("oyun_degerlendirme:liste")

