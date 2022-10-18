from cgitb import html
from django.shortcuts import render

# Create your views here.
def pemb3(request):
    judul = ["Latihan Soal Lingkaran", "Latihan Soal Bangun Ruang", "Latihan Soal Bangun Datar", "Latihan Soal Matriks", "Latihan Soal Mean, Median, dan Modus", "Latihan Soal Induksi Matematika"]

    konteks = {
        'title': judul
    }

    return render(request, 'indexlat.html', konteks)
