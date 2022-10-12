from os import name
from django.shortcuts import render
from django.http import HttpResponse

from products.models import Product


# Create your views here.
def get_home(request):
    return HttpResponse(f"<h1>Welcome to the website!</h1>")


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return HttpResponse(
        f"""
    <p>{product.id}</p>
    <p>{product.name}</p>
    <p>{product.price}</p>
    """
    )
