from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):

        context = {
            'animais': Animal.objects.all(),
            'tipos': Tipo.objects.all(),
            'status_list': Status.objects.all(),
            'bairros': Bairro.objects.all(),
        }

        return render(request, 'index.html', context)

    # def get(self, request, *args, **kwargs):
    #     animais = Animal.objects.all()
    #     return render(request, 'index.html', {'animais': animais})
    
    # def cadastrar_animal(request):

    #     context = {
    #         'tipos': Tipo.objects.all(),
    #         'status_list': Status.objects.all(),
    #         'bairros': Bairro.objects.all(),
    #     }

    #     return render(request, 'cadastro_animal.html', context)