from django.db import models

# Create your models here.
class Submateri(models.Model):
    kode_submateri = models.CharField(max_length=50)
    materi = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.materi
        
class Materi_pembelajaran(models.Model):
    kode_submateri = models.ForeignKey(Submateri, on_delete=models.CASCADE, null=True)
    judul = models.CharField(max_length=100)
    penulis = models.CharField(max_length=50)
    penerbit = models.CharField(max_length=50)
    tanggal_rilis = models.DateField()

    def __str__(self):
        return self.judul