import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Validade
from django.shortcuts import redirect, render
from django.db.models import Q
from .forms import ValidadeForm


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