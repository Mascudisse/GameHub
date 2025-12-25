from django.shortcuts import render, get_object_or_404, redirect
from .models import OyuncuIlan


def ilan_listesi(request):
    ilanlar = OyuncuIlan.objects.all().order_by("-id")
    return render(
        request,
        "oyuncu_ilanlari/ilan_listesi.html",
        {"ilanlar": ilanlar}
    )


def ilan_duzenle(request, id):
    ilan = get_object_or_404(OyuncuIlan, id=id)

    if request.method == "POST":
        ilan.oyun_adi = request.POST.get("oyun_adi")
        ilan.oyuncu_adi = request.POST.get("oyuncu_adi")
        ilan.rank = request.POST.get("rank")
        ilan.platform = request.POST.get("platform")
        ilan.aciklama = request.POST.get("aciklama")
        ilan.save()

        return redirect("oyuncu_ilanlari:ilan_listesi")

    return render(
        request,
        "oyuncu_ilanlari/ilan_duzenle.html",
        {"ilan": ilan}
    )


def ilan_sil(request, id):
    ilan = get_object_or_404(OyuncuIlan, id=id)
    ilan.delete()
    return redirect("oyuncu_ilanlari:ilan_listesi")
from django.shortcuts import render, redirect
from .models import OyuncuIlan

def ilan_ekle(request):
    if request.method == "POST":
        # Formdan gelen verileri alıyoruz
        oyun_adi = request.POST.get('oyun_adi')
        oyuncu_adi = request.POST.get('oyuncu_adi')
        rank = request.POST.get('rank')
        platform = request.POST.get('platform')
        aciklama = request.POST.get('aciklama')

        # Veritabanına yeni kaydı oluşturuyoruz
        OyuncuIlan.objects.create(
            oyun_adi=oyun_adi,
            oyuncu_adi=oyuncu_adi,
            rank=rank,
            platform=platform,
            aciklama=aciklama
        )
        # Kayıt bittikten sonra ilan listesine geri dönüyoruz
        return redirect('oyuncu_ilanlari:ilan_listesi')

    # Eğer istek GET ise (sayfa ilk açılıyorsa) formu göster
    return render(request, 'oyuncu_ilanlari/ilan_ekle.html')