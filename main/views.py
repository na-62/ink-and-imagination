from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Ink & Imagination',
        'npm' : '2306226391',
        'name': 'Nafisa Arrasyida',
        'class': 'PBP E',
        'product_name':'A5 Sketchbook',
        'product_price': 120000,
        'product_description':'hot pressed, 60 pages',
        'product_media':'watercolor, ink, graphite'
    }

    return render(request, "main.html", context)