# from rembg import remove
# from PIL import Image
import os
import requests
from base.settings import BASE_DIR


def api_remove_bg():
    saved_path =str(BASE_DIR)+"/media/input.png"
    removed_path = str(BASE_DIR)+"/media/removedBg_out.png"

    url = 'https://api.remove.bg/v1.0/removebg'
    api_key = 'yhvSjcuwRePKoohDWTK3bcRq'
    image=open(saved_path, 'rb')
    headers = {'X-API-Key': api_key}
    data = {
        'size': 'auto',
    }
    files={'image_file': image}


    response = requests.post(url, headers=headers, data=data,files=files)

    if response.status_code==402:  #your couta finished
        print("your today coutta finished ! ")
        return Py_remove_background()
    elif response.status_code==402:
        print("error in network ")
        return Py_remove_background()
    else:
        IMG=response.content
        with open(removed_path, 'wb') as f:
            f.write(IMG)
        return removed_path

def Py_remove_background():
    saved_path =str(BASE_DIR)+"/media/input.png"
    removed_path = str(BASE_DIR)+"/media/removedBg_out.png"

    # IMG = Image.open(saved_path)
    # output_image = remove(IMG)

    # output_image.save(removed_path)
    return removed_path

