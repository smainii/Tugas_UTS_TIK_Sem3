from cgitb import html
from django.shortcuts import render

# Create your views here.
def pemb5(request):
    judul = ["Video Materi Lingkaran", "Video Materi Bangun Ruang", "Video Materi Bangun Datar", "Video Materi Matriks", "Video Materi Mean, Median, dan Modus", "Video Materi Induksi Matematika"]
    
    konteks = {
        'title': judul
    }

    return render(request, 'indexvid.html', konteks)
