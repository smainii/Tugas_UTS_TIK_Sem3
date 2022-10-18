from cgitb import html
from django.shortcuts import render

# Create your views here.
def pemb2(request):
    judul = ["Contoh Soal Lingkaran", "Contoh Soal Bangun Ruang", "Contoh Soal Bangun Datar", "Contoh Soal Matriks", "Contoh Soal Mean, Median, dan Modus", "Contoh Soal Induksi Matematika"]

    konteks = {
        'title': judul
    }

    return render(request, 'indexcon.html', konteks)
