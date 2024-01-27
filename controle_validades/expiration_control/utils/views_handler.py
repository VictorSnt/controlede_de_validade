from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render
from django.db.models import Q

from ..forms import ValidadeForm
from ..models import Validade


class ViewHandler:
    pass

class MenuDisplayer(ViewHandler):

    def __init__(self, request):
        self.request = request
    
    def render_menu(self):
        return render(self.request, "index.html")

class ExpirationDisplayer(ViewHandler):
    
    def __init__(self, request):
        self.request = request
        self.search_query = self.get_search_or_blank()

    def get_search_or_blank(self) -> str:
        
        return self.request.GET.get('search', '')

    def filter_validades(self, validades, search_query):
        return validades.filter(
            Q(dtvalidade__icontains=search_query) |
            Q(qtestoque__icontains=search_query) |
            Q(produto__cdprincipal__icontains=search_query) |
            Q(produto__dsdetalhe__icontains=search_query)
        )

    def get_paginated_validades(self, validades, page_size=3):
        paginator = Paginator(validades, page_size)
        page = self.request.GET.get('page')

        try:
            validades_paginadas = paginator.page(page)
        except PageNotAnInteger:
            validades_paginadas = paginator.page(1)
        except EmptyPage:
            validades_paginadas = paginator.page(paginator.num_pages)

        return validades_paginadas

    def get_filtered_and_paginated_validades(self):
        validades = Validade.objects.order_by('dtvalidade').all()

        if self.search_query:
            validades = self.filter_validades(validades, self.search_query)
        validades_paginadas = self.get_paginated_validades(validades)
        
        return render(
        self.request, 'expiration_list.html', 
        {'validades_paginadas': validades_paginadas}
        )


class ExpirationSaver(ViewHandler):
    
    def __init__(self, request):
        self.request = request
    
    def validate_form(self):     
        if self.request.method == 'POST':
            form = ValidadeForm(self.request.POST)
            if form.is_valid():
                form.save()
                return redirect('expiration_list')
        else:
            form = ValidadeForm()
        return render(self.request, 'expiration_form.html', {'form': form})
