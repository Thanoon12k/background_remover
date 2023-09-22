
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from mainapp.remover import Py_remove_background, api_remove_bg
from .serializers import ImageUploadSerializer


class ImageProcessingView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        
        if serializer.is_valid():
            IMG = serializer.validated_data['image']
            save_path = 'media/input.png'
            
            with open(save_path, 'wb') as f:
                f.write(IMG.read())
            
            removed_path = api_remove_bg()
           
            
            # To send back the removed background image for preview
            with open(removed_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='image/png')
                response['Content-Disposition'] = 'attachment; filename="output.png"'
                return response
        
        return Response(serializer.errors, status=400)
