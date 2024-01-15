from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Produto, Validade
from django.shortcuts import render
from django.db.models import Q
from .forms import ValidadeForm
import json

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

    paginator = Paginator(validades, 5)  
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
        form = request.POST
        print(**form)
        

    return render(request, 'expiration_form.html', {'form': form})