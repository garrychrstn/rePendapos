from django.shortcuts import render
from . forms import *
from . models import *

# Create your views here.
def index(response):
    return render(response, 'index.html')

def insert(response):
    if response.method == 'POST':
        form = F_Profil(response.POST)

        if form.is_valid():
            nik = form.cleaned_data['nik']
            nama = form.cleaned_data['nama']
            nikibu = form.cleaned_data['nikibu']
            tgl = form.cleaned_data['tgl']
            kelamin = form.cleaned_data['kelamin']
            namaibu = form.cleaned_data['namaibu']
            dusun = form.cleaned_data['dusun']

            p = Profil(nik=nik, nama=nama, tgl=tgl, nikibu=nikibu, dusun=dusun, kelamin=kelamin, namaibu=namaibu)
            p.save()

            form = F_Profil()

        context = { 'form' : form }

        return render(response, 'insert.html', context)
    else:
        form = F_Profil()
    
    return render(response, 'insert.html', {'form' : form})

def inputPosyandu(response):
    return render(response, 'inputposyandu.html')