from django.db import models
from django.contrib.auth.models import User

class OyunDegerlendirme(models.Model):
    oyun_adi = models.CharField(max_length=100)
    puan = models.IntegerField()
    yorum = models.TextField()

    kullanici = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.oyun_adi
