from .utils.views_handler import ExpirationDisplayer, ExpirationSaver, MenuDisplayer
from django.views.decorators.cache import cache_page


def index(request):
     
    display_menu = MenuDisplayer(request)
    http_response = display_menu.render_menu()
    return http_response

@cache_page(60 * 15)
def display_expirations(request):
    
    handler = ExpirationDisplayer(request)
    http_response = handler.get_filtered_and_paginated_validades()
    return http_response

def add_expiration(request):

    handler = ExpirationSaver(request)
    http_response = handler.validate_form()
    return http_response

