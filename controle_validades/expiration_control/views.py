import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Validade, Produto
from django.shortcuts import redirect, render
from django.db.models import Q
from .forms import ValidadeForm
from .utils.database.alterdata_handler import build_connection
from django.conf import settings

def index(request):  
    return HttpResponse(render(request, "index.html"))

def expiration_list(request):
    search_query = request.GET.get('search', '')
    validades = Validade.objects.order_by('dtvalidade').all()
    if search_query:
        validades = validades.filter(
            Q(dtvalidade__icontains=search_query) |
            Q(qtestoque__icontains=search_query) |
            Q(produto__cdprincipal__icontains=search_query) |
            Q(produto__dsdetalhe__icontains=search_query)
        )
    
    paginator = Paginator(validades, 3)  
    page = request.GET.get('page')

    try:
        validades_paginadas = paginator.page(page)
    except PageNotAnInteger:
        validades_paginadas = paginator.page(1)
    except EmptyPage:
        validades_paginadas = paginator.page(paginator.num_pages)

    return render(request, 'expiration_list.html', {'validades_paginadas': validades_paginadas})

def expiration_form(request):

    if request.method == 'POST':
        form = ValidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expiration_list')
    else:
        form = ValidadeForm()
    return render(request, 'expiration_form.html', {'form': form})

def seed_db(request):
    
    alterdata_db = build_connection()
    with alterdata_db.connect():
        
        path = settings.STATICFILES_DIRS[0] + '/validades_database.json'
        with open(path, 'r') as file:
            data = json.load(file)
        
        for info in data:
            dtvalidade = info[1]
            qtestoque = info[2]
            info = info[0]
            foto = alterdata_db.get_image(info['iddetalhe'])
            
            produto = Produto(
                iddetalhe=info['iddetalhe'], cdprincipal=info['cdprincipal'],
                dsdetalhe= info['dsdetalhe']
            )
            if foto:
                foto: memoryview = foto[0]['foto']
                produto.save_image_from_base64(foto)
            produto.save()
            validade = Validade(produto=produto, dtvalidade=dtvalidade, qtestoque=qtestoque)
            validade.save()
            