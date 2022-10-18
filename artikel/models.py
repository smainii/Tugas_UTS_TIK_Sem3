from django.db import models

# Create your models here.
class Volume_jurtik(models.Model):
    volume_nomor_issue = models.CharField(max_length=50)
    judul = models.CharField(max_length=100)
    keterangan = models.TextField()

    def __str__(self):
        return self.judul

class Jurnal_artikel_matematika(models.Model):
    judul = models.CharField(max_length=100)
    nama_penulis = models.CharField(max_length=50)
    tahun_publikasi = models.CharField(max_length=50)
    volume_nomor_issue = models.ForeignKey(Volume_jurtik, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.judul