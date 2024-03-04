from app.service.posts.post import obtener_posts, crear_post, actualizar_post, eliminar_post
from app.service.photos.photo import obtener_photos
from string import Template

def app():
    ##algoritmo base o funcional del programa, todo entro por aca, por app
    #print("App!!")
    #posts= obtener_posts()
    
    # mi_post = {
    #     "userId": 1,
    #     "id": 103,
    #     "title": "Titulo de prueba",
    #     "body": "Body de prueba"
    # }
    
    
    # c_post=crear_post(post=mi_post)
    # print(c_post)
    
    # a_post=actualizar_post(post=mi_post, id="4")
    # print(a_post)
    
    # d_post=eliminar_post(id="4")
    # print(d_post)
    
    #print("mis posts: ", posts)
    #print(type(posts["data"]))
    
    # for post in posts["data"]:
    #     print(f"ID: {post['id']} - Titulo: {post['title']}")
    
    ###EJEMLPO 2
    mis_photos = obtener_photos(cantidad=5)
    #print(mis_photos)
    
    img_template = Template('<img src="$url" />')
    #imagen = img_template.substitute(url = "hola mundo")
    
    html_template = Template('''
                             <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                    <title>Document</title>
                                </head>
                                <body>
                                    <h1> Mi primera pagina con python tszzzz!! </h1>
                                    $body
                                </body>
                                </html>
                             ''')
    #print([photo["url"] for photo in mis_photos])
    
    lista_urls = [photo["url"] for photo in mis_photos]
    texto_img = ""
    for url in lista_urls:
        texto_img += img_template.substitute(url = url) + "\n"
    
    #print(texto_img)
    html = html_template.substitute(body = texto_img)
    print(html)
    
    
    #print(imagen)
    