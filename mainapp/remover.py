from rembg import remove
from PIL import Image
import os
import requests


my_rmbg_api_key = os.environ.get('REMOVE_Background_API_KEY')

def api_remove_bg():
    saved_path='media/'+'input.png'
    removed_path = 'media/'+"removedBg_out.png"
    
    url = 'https://api.remove.bg/v1.0/removebg'
    api_key = my_rmbg_api_key
    image=open(saved_path, 'rb')
    headers = {'X-API-Key': api_key}
    data = {
        'size': 'auto',
    }
    files={'image_file': image}


    response = requests.post(url, headers=headers, data=data,files=files)

    with open(removed_path, 'wb') as f:
        f.write(response.content)
    
    return removed_path

def Py_remove_background():
    saved_path='media/'+'input.png'
    removed_path = 'media/'+"py_removedBg_out.png"
    
    IMG = Image.open(saved_path)
    output_image = remove(IMG)
    
    output_image.save(removed_path)
    return removed_path

# Example usage

