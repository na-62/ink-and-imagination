from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Ink & Imagination',
        'npm' : '2306226391',
        'name': 'Nafisa Arrasyida',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)