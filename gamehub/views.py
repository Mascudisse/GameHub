from django.shortcuts import render


def home(request):
    return render(request,"home.html")


def hakkimizda_view(request):
    return render(request,"hakkimizda.html")


def iletisim_view(request):
    return render(request,"iletisim.html")

def kategori_view(request):
    return render(request,"kategoriler.html")



