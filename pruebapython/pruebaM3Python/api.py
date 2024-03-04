from requests import request
from json import loads

URL="https://jsonplaceholder.typicode.com/posts"

payload={}
headers={}

response= request("GET",URL,headers=headers, data=payload)

##el tipo de dato que es
#print(type(loads(response.text)))
##el primer objeto del diccionario
print(loads(response.text))
##para saber que codigo imprime, "codigo de respuesta"
#print("status: ",response.status_code)
dicc_post=loads(response.text)

#for data in dicc_post:
    ##ojo con las comillas las simples son para el string
    #print(f'{data["userId"]}-{data["title"]}')

# for data in dicc_post:
#     print(f'{data["userId"]}-{data["id"]}-{data["title"]}')

##este sirve para imprimir solo titles
#print([valor["title"] for valor in dicc_post])
