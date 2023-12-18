from django import forms
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 


class F_Profil(forms.Form):
    nik = forms.IntegerField(
        label_suffix = ' ',
        label = ' ',
        widget=forms.TextInput(attrs={
            'placeholder' : 'NIK'
        })
    )
    nama = forms.CharField(
        max_length=30,
        label=' ', 
        label_suffix=' ',
        widget=forms.TextInput(attrs={
            'placeholder' : 'Nama Lengkap'
        })
    )
    namaibu = forms.CharField(
        max_length=30,
        label = '',
        label_suffix='',
        widget=forms.TextInput(attrs= {
            'placeholder' : 'Nama Ibu'
        })
    )
    nikibu = forms.IntegerField(
        required=True,
        label_suffix='',
        label = '',
        widget = forms.TextInput(attrs = {
            'placeholder' : 'NIK Ibu'
        })
    )
    pilihandusun = [
        ('Kerjo', 'Kerjo'),
        ('Sumberejo', 'Sumberejo'),
        ('Plandakan', 'Plandakan'),
        ('Kadipeso', 'Kadipeso'),
        ('Dumpul', 'Dumpul'),
        ('Derso', 'Derso')
    ]
    dusun = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class' : 'dusun'
        }),
        required = True,
        choices=pilihandusun,
        label = 'Dusun',
    )
    tgl = forms.DateField(
        label=' ', 
        label_suffix=' ',
        widget=forms.DateInput(attrs={
            'placeholder' : 'Tanggal Lahir',
            'class' : 'tgl',
            'type' : 'date'
        }))
    
    pilihankelamin = [
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan')
    ]
    kelamin = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices = pilihankelamin,
        label = "Jenis Kelamin "
    )   
