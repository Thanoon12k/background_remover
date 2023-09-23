from django.shortcuts import render
from django.http import HttpResponse
from .remover import api_remove_bg,Py_remove_background
import requests
from base.settings import BASE_DIR

def Index(request):
     print("new request arrive >>> ")
     if request.method == 'POST':

            print("it iss post request  >>> ")
            if  request.FILES.get('image') :     # post request to remove bakground
               IMG = request.FILES['image']
               save_path = str(BASE_DIR)+"/media/input.png"
               print("requested image to start save >>> ",save_path)
               with open(save_path, 'wb') as f:

                    f.write(IMG.read())
               print("image saved  to >>> ",save_path)
               removed_path=api_remove_bg()

               return render(request, 'index.html',{
                'input_image':save_path,
               'output_image':removed_path

               })

            elif 'download_image' in request.POST:#post rerquest to download
               output_path = str(BASE_DIR)+"/media/removedBg_out.png"
               with open(output_path, 'rb') as f:
                    response = HttpResponse(f.read(), content_type='image/png')
                    response[f'Content-Disposition'] = f'attachment; filename="output.png"'
                    return response
            print("error in post request  >>> ")
     return render(request, 'index.html')


