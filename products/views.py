from math import prod
from multiprocessing import context
from os import name
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from products.models import Product


# Create your views here.
def get_home(request):
    return HttpResponse(f"<h1>Welcome to the website!</h1>")


# def get_product(request, product_id):
#     product = Product.objects.get(id=product_id)
#     return HttpResponse(
#         f"""
#     <p>{product.id}</p>
#     <p>{product.name}</p>
#     <p>{product.price}</p>
#     """
#     )


def get_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except:
        raise Http404
    context = {
        "product": {
            "name": product.name,
            "description": product.description,
            "price": product.price,
        }
    }
    return render(request, "product_detail.html", context)
