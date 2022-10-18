from cgitb import html
from django.shortcuts import render

# Create your views here.
def pemb1(request):
    judul = ["Kesulitan Belajar Matematika", "Pemrograman Linear", "Literasi dalam Pembelajaran Matematika"]

    konteks = {
        'title': judul
    }

    return render(request, 'indexart.html', konteks)
