from django.db import models

class OyuncuIlan(models.Model):
    oyun_adi = models.CharField(max_length=100)
    oyuncu_adi = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    platform = models.CharField(max_length=30)
    aciklama = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.oyuncu_adi} - {self.oyun_adi}"
