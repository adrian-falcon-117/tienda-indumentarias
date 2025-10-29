from django.shortcuts import render

from .models import Remera


def catalogo(request):
    remeras = Remera.objects.all()
    ctx = {"remeras": remeras}
    return render(request, "shop/catalogo.html", ctx)


def inicio(request):
    return render(request, "shop/inicio.html")
