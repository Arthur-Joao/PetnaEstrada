from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):

        if "usuario_id" not in request.session:
            return redirect("login")

        context = {
            'animais': Animal.objects.all(),
            'tipos': Tipo.objects.all(),
            'status_list': Status.objects.all(),
            'bairros': Bairro.objects.all(),
        }

        return render(request, 'index.html', context)
    
class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):

        email = request.POST.get("email")
        senha = request.POST.get("senha")

        try:
            usuario = Usuario.objects.get(email=email, senha=senha)

            request.session["usuario_id"] = usuario.id
            request.session["usuario_nome"] = usuario.nome

            return redirect("index")

        except Usuario.DoesNotExist:
            messages.error(request, "E-mail ou senha inválidos.")
            return redirect("login")

class LogoutView(View):

    def get(self, request):
        request.session.flush()
        return redirect("login")

class FeedbackView(View):

    def get(self, request):

        context = {
            "feedbacks": Feedback.objects.all()
        }

        return render(request, "feedback.html", context)


    def post(self, request):

        usuario = Usuario.objects.get(id=request.session["usuario_id"])

        Feedback.objects.create(
            estrelas=request.POST.get("estrelas"),
            comentario=request.POST.get("comentario"),
            usuario=usuario
        )

        messages.success(request, "Feedback enviado com sucesso!")

        return redirect("feedback")

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