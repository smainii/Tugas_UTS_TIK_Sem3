from cgitb import html
from django.shortcuts import render

# Create your views here.
def pemb4(request):
    judul = ["Materi Lingkaran", "Materi Bangun Ruang", "Materi Bangun Datar", "Materi Matriks", "Materi Mean, Median, dan Modus", "Materi Induksi Matematika"]

    konteks = {
        'title': judul
    }

    return render(request, 'indexmateri.html', konteks)
