from django.shortcuts import render

def listar_publicaciones(request):
    return render(request, 'blog/listar_publicaciones.html', {})
