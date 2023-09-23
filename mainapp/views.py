from django.shortcuts import render
from django.http import HttpResponse
import os
from .remover import api_remove_bg,Py_remove_background
import requests
from django.shortcuts import render, redirect


def Index(request):
    input_image = request.GET.get('input_image')
    output_image = request.GET.get('output_image')
    
    return render(request, 'index.html', {
        'input_image': input_image,
        'output_image': output_image
    })


def ProcessImage(request):
    if request.method == 'POST' and request.FILES.get('image'):
        IMG = request.FILES['image']
        save_path = 'media/' + 'input.png'
        with open(save_path, 'wb') as f:
            f.write(IMG.read())

        removed_path = api_remove_bg()
        
        # Redirect to index with parameters
        return redirect(f"/?input_image={save_path}&output_image={removed_path}")


def DownloadImage(request):
    output_path = 'media/removedBg_out.png'
    with open(output_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/png')
        response[f'Content-Disposition'] = f'attachment; filename="output.png"'
        return response
