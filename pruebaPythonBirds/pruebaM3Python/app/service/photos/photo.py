import app.service.repository.api_manager as api_manager

URL_PHOTOS = "https://jsonplaceholder.typicode.com/photos"

def obtener_photos(id:str = None, cantidad:int = 0):
    url =  URL_PHOTOS if id is None else f"{URL_PHOTOS}{id}"
    respuesta = api_manager.get(url)
    return respuesta[:cantidad] if type(respuesta) == list and cantidad <= len(respuesta) else respuesta 
