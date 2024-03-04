import app.service.repository.api_manager as api_manager

URL_POSTS = "https://jsonplaceholder.typicode.com/posts/"
response = {
    "data": None,
    "message": ""   
}


def obtener_posts(id:str = None):
    # posts = [{
    #             "userId": 1,
    #             "id": 1,
    #             "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    #             "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    #         }]
    #print("obteniendo posts!!!")
    data={}
    url = URL_POSTS if id is None else f"{URL_POSTS}{id}"
    if id is not None:

        if id.isdigit() and int(id) > 0:
            data = api_manager.get(url)
            return obtener_response(data=data)
        else:
            return obtener_response(data=data, tipo="error", message="servicio con error" )
            
    else:
        data = api_manager.get(url)
        return obtener_response(data=data)    

def crear_post(post: dict):
    headers = {'Content-Type': 'application/json'}
    return api_manager.post(url=URL_POSTS,headers=headers, payload=post)

def actualizar_post(post: dict, id:str):
    headers = {'Content-Type': 'application/json'}
    url= f"{URL_POSTS}{id}"
    return api_manager.put(url=url,headers=headers, payload=post)

def eliminar_post(id:str):
    headers = {'Content-Type': 'application/json'}
    url= f"{URL_POSTS}{id}"
    return api_manager.delete(url=url,headers=headers)


def obtener_response(data,tipo:str="OK",message:str=""):
    response["data"]=data
    response["message"]= f"{tipo}: {message}" if tipo != "ok" else f"{tipo}: peticion exitosa "
    return response

