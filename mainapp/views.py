from django.shortcuts import render
from django.http import HttpResponse
import os
from .remover import api_remove_bg,Py_remove_background

def Index(request):
     if request.method == 'POST':
          print('post:',request.POST)
         
          if  request.FILES.get('image_file') :     # post request to remove bakground
               IMG = request.FILES['image_file']
               save_path = 'media/'+'input.png'
               with open(save_path, 'wb') as f:
                    f.write(IMG.read())
               
               removed_path=api_remove_bg()# remove via BG API *limited requests 50 per day
               # py_removed_path=Py_remove_background() # remove from python  *unlimited requests
               return render(request, 'index.html',{
                'input_image':save_path,
               'output_image':removed_path
              
               })
          
          elif 'download_image' in request.POST:#post rerquest to download
               output_path ='media/removedBg_out.png'
               with open(output_path, 'rb') as f:
                    response = HttpResponse(f.read(), content_type='image/png')
                    response[f'Content-Disposition'] = f'attachment; filename="output.png"'
                    return response
     return render(request, 'index.html')


