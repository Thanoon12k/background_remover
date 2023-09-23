from django.shortcuts import render
from django.http import HttpResponse
import os
from .remover import api_remove_bg,Py_remove_background
import requests
from django.shortcuts import render, redirect


def Index(request):
    # Clear session data (if you want to start fresh every time the index is loaded)
    if 'input_image' in request.session:
        del request.session['input_image']
    if 'output_image' in request.session:
        del request.session['output_image']

    return render(request, 'index.html')

def ProcessImage(request):
    if request.method == 'POST' and request.FILES.get('image'):
        IMG = request.FILES['image']
        save_path = 'media/' + 'input.png'
        with open(save_path, 'wb') as f:
            f.write(IMG.read())

        removed_path = api_remove_bg()

        request.session['input_image'] = save_path
        request.session['output_image'] = removed_path

    return redirect('index')

def DownloadImage(request):
    output_path = 'media/removedBg_out.png'
    with open(output_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/png')
        response[f'Content-Disposition'] = f'attachment; filename="output.png"'
        return response
