from django.shortcuts import render

def lista_post(request):
    return render(request, 'postagens/lista_post.html')
