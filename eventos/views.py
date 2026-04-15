from django.shortcuts import render

# Create your views here.]

lista_eventos = [

]

def index(request):
    if request.method == 'POST':
        nome_evento = request.POST.get('evento')
        nome_local = request.POST.get('local')
        lista_eventos.append({'nome_evento': nome_evento, 'nome_local': nome_local})
    return render(request, 'novo/novo.html')

def dashboard(request):
    return render(request, "home/home.html", context={'lista_eventos': lista_eventos})